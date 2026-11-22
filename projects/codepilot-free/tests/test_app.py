"""Standard-library integration tests for CodePilot's local API."""
from __future__ import annotations

import io
import json
import socket
import struct
import threading
import unittest
import zipfile
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import app as codepilot


class FakeOllamaHandler(BaseHTTPRequestHandler):
    last_chat_request = None
    omit_done = False

    def do_GET(self):
        if self.path != "/api/tags":
            self.send_error(404)
            return
        body = json.dumps({"models": [{"name": "test-coder:latest"}]}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        if self.path != "/api/chat":
            self.send_error(404)
            return
        length = int(self.headers.get("Content-Length", "0"))
        type(self).last_chat_request = json.loads(self.rfile.read(length).decode())
        chunks = [
            {"model": "test-coder:latest", "message": {"role": "assistant", "content": "hello "}, "done": False},
            {"model": "test-coder:latest", "message": {"role": "assistant", "content": "from the test model"}, "done": not type(self).omit_done, "total_duration": 1_500_000_000},
        ]
        body = b"".join(json.dumps(chunk).encode() + b"\n" for chunk in chunks)
        self.send_response(200)
        self.send_header("Content-Type", "application/x-ndjson")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        pass


class CodePilotApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original_ollama_url = codepilot.OLLAMA_BASE_URL
        cls.fake_ollama = ThreadingHTTPServer(("127.0.0.1", 0), FakeOllamaHandler)
        cls.fake_ollama_thread = threading.Thread(target=cls.fake_ollama.serve_forever, daemon=True)
        cls.fake_ollama_thread.start()
        codepilot.OLLAMA_BASE_URL = f"http://127.0.0.1:{cls.fake_ollama.server_port}"
        handler_class = getattr(codepilot, "CodePilotHandler", getattr(codepilot, "Handler", None))
        if handler_class is None:
            raise RuntimeError("The CodePilot HTTP handler was not found")
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), handler_class)
        cls.server_thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.server_thread.start()
        cls.base = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.server_thread.join(timeout=2)
        cls.fake_ollama.shutdown()
        cls.fake_ollama.server_close()
        cls.fake_ollama_thread.join(timeout=2)
        codepilot.OLLAMA_BASE_URL = cls.original_ollama_url

    def request(self, path, method="GET", payload=None, raw=None, content_type="application/json"):
        data = raw if raw is not None else (
            json.dumps(payload).encode("utf-8") if payload is not None else None
        )
        request = Request(
            self.base + path, data=data, method=method,
            headers={"Content-Type": content_type},
        )
        try:
            with urlopen(request, timeout=3) as response:
                return response.status, response.headers.get_content_type(), response.read()
        except HTTPError as error:
            return error.code, error.headers.get_content_type(), error.read()

    def test_static_workspace_is_served(self):
        status, content_type, body = self.request("/")
        self.assertEqual(status, 200)
        self.assertEqual(content_type, "text/html")
        self.assertIn(b"CodePilot Free", body)
        self.assertEqual(self.request("/app.js")[0], 200)
        self.assertEqual(self.request("/styles.css")[0], 200)

    def test_health_and_model_discovery(self):
        status, _, body = self.request("/api/health")
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(body)["ollama"], "online")
        self.assertEqual(json.loads(body)["models"], ["test-coder:latest"])
        status, _, body = self.request("/api/models")
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(body)["models"], ["test-coder:latest"])

    def test_chat_proxies_request_and_returns_answer(self):
        status, content_type, body = self.request(
            "/api/chat", "POST",
            {"model": "test-coder:latest", "stream": True, "messages": [
                {"role": "user", "content": "Say hello"},
                {"role": "system", "content": "This role is not accepted from clients"},
            ]},
        )
        self.assertEqual(status, 200)
        self.assertEqual(content_type, "text/event-stream")
        packets = [json.loads(line[6:]) for line in body.decode().splitlines() if line.startswith("data: ")]
        self.assertEqual("".join(packet.get("delta", "") for packet in packets), "hello from the test model")
        self.assertEqual(packets[-1]["duration_ms"], 1500)
        sent = FakeOllamaHandler.last_chat_request
        self.assertEqual(sent["model"], "test-coder:latest")
        self.assertEqual(sent["messages"][0]["role"], "system")
        self.assertTrue(all(item["role"] in {"system", "user", "assistant"} for item in sent["messages"]))
        self.assertNotIn("This role is not accepted from clients", str(sent["messages"]))


    def test_chat_reports_incomplete_when_ollama_omits_done_chunk(self):
        original = FakeOllamaHandler.omit_done
        try:
            FakeOllamaHandler.omit_done = True
            status, content_type, body = self.request(
                "/api/chat", "POST",
                {"model": "test-coder:latest", "messages": [{"role": "user", "content": "Hi"}]},
            )
        finally:
            FakeOllamaHandler.omit_done = original

        self.assertEqual(status, 200)
        self.assertEqual(content_type, "text/event-stream")
        packets = [
            json.loads(line[6:])
            for line in body.decode().splitlines()
            if line.startswith("data: ")
        ]
        self.assertFalse(packets[-1]["done"])
        self.assertIn("ended before", packets[-1]["error"])

    def test_chat_returns_json_error_when_ollama_is_offline(self):
        original = codepilot.OLLAMA_BASE_URL
        try:
            codepilot.OLLAMA_BASE_URL = "http://127.0.0.1:1"
            status, content_type, body = self.request(
                "/api/chat", "POST",
                {"model": "test-coder:latest", "messages": [{"role": "user", "content": "Hi"}]},
            )
        finally:
            codepilot.OLLAMA_BASE_URL = original
        self.assertEqual(status, 503)
        self.assertEqual(content_type, "application/json")
        self.assertIn("Local AI connection failed", json.loads(body)["error"])

    def test_invalid_chat_requests_are_rejected(self):
        status, _, body = self.request("/api/chat", "POST", {"model": "", "messages": []})
        self.assertEqual(status, 400)
        self.assertIn("model", json.loads(body)["error"].lower())
        status, _, _ = self.request("/api/chat", "POST", {"model": "test-coder", "messages": []})
        self.assertEqual(status, 400)
        status, _, _ = self.request("/api/chat", "POST", raw=b"{bad json")
        self.assertEqual(status, 400)

    def test_chat_skips_messages_with_non_string_roles(self):
        status, _, _ = self.request(
            "/api/chat", "POST",
            {"model": "test-coder:latest", "messages": [
                {"role": "user", "content": "Say hello"},
                {"role": [], "content": "Malformed list role"},
                {"role": {"name": "user"}, "content": "Malformed object role"},
            ]},
        )
        self.assertEqual(status, 200)
        self.assertEqual(
            FakeOllamaHandler.last_chat_request["messages"][1:],
            [{"role": "user", "content": "Say hello"}],
        )

    def test_project_export_and_zip_import_round_trip(self):
        project = {"index.html": "<h1>Hello</h1>", "src/main.js": "console.log('hi')"}
        status, content_type, body = self.request("/api/project/export", "POST", {"files": project})
        self.assertEqual(status, 200)
        self.assertEqual(content_type, "application/zip")
        with zipfile.ZipFile(io.BytesIO(body)) as archive:
            self.assertEqual(archive.read("index.html").decode(), project["index.html"])
            self.assertEqual(archive.read("src/main.js").decode(), project["src/main.js"])
        status, _, response_body = self.request("/api/project/import-zip", "POST", raw=body, content_type="application/zip")
        self.assertEqual(status, 200)
        self.assertEqual(json.loads(response_body)["files"], project)


    def test_project_export_rejects_files_over_import_limit(self):
        oversized = "x" * (2 * 1024 * 1024 + 1)
        status, _, body = self.request(
            "/api/project/export", "POST", {"files": {"large.py": oversized}}
        )
        self.assertEqual(status, 413)
        self.assertIn("2 MiB or smaller", json.loads(body)["error"])

    def test_project_export_rejects_reserved_manifest_filename(self):
        status, _, body = self.request(
            "/api/project/export", "POST",
            {"files": {"__codepilot_manifest__.json": "user supplied data"}},
        )
        self.assertEqual(status, 400)
        self.assertIn("manifest filename is reserved", json.loads(body)["error"])


    def test_project_export_rejects_normalized_path_collisions(self):
        status, _, body = self.request(
            "/api/project/export", "POST",
            {"files": {"src/main.py": "first", "src//main.py": "second"}},
        )
        self.assertEqual(status, 400)
        self.assertIn("duplicate or colliding", json.loads(body)["error"])

    def test_zip_import_rejects_normalized_path_collisions(self):
        memory = io.BytesIO()
        with zipfile.ZipFile(memory, "w") as archive:
            archive.writestr("__codepilot_manifest__.json", json.dumps({"format": "codepilot-project-v1"}))
            archive.writestr("src/main.py", "first")
            archive.writestr("src//main.py", "second")
        with self.assertRaisesRegex(ValueError, "duplicate or colliding project paths"):
            codepilot.read_zip_files(memory.getvalue())

    def test_zip_import_rejects_oversized_project_manifest_before_reading(self):
        memory = io.BytesIO()
        with zipfile.ZipFile(memory, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.writestr(
                codepilot.MANIFEST_NAME,
                "x" * (codepilot.MAX_MANIFEST_BYTES + 1),
            )
            archive.writestr("src/main.py", "print('safe')")

        blob = memory.getvalue()
        self.assertLess(len(blob), codepilot.MAX_ZIP_BYTES)
        with self.assertRaisesRegex(ValueError, "manifest exceeds the 4 KiB safety limit"):
            codepilot.read_zip_files(blob)

    def test_zip_import_rejects_forged_uncompressed_size_metadata(self):
        memory = io.BytesIO()
        with zipfile.ZipFile(memory, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.writestr(codepilot.MANIFEST_NAME, "x" * (8 * 1024 * 1024))
            archive.writestr("src/main.py", "print('safe')")

        # Forge the advertised uncompressed sizes in both ZIP headers while
        # retaining the original compressed payload. The importer must reject malformed size metadata rather than accept
        # a truncated entry or rely only on ZipInfo.file_size.
        blob = bytearray(memory.getvalue())
        local_header = blob.find(b"PK\x03\x04")
        central_directory = blob.find(b"PK\x01\x02")
        self.assertGreaterEqual(local_header, 0)
        self.assertGreaterEqual(central_directory, 0)
        struct.pack_into("<I", blob, local_header + 22, 0)
        struct.pack_into("<I", blob, central_directory + 24, 0)

        with self.assertRaisesRegex(ValueError, "not a valid ZIP archive"):
            codepilot.read_zip_files(bytes(blob))

    def test_zip_import_rejects_excessive_central_directory_entries_before_parsing(self):
        memory = io.BytesIO()
        entry_count = codepilot.MAX_FILES * 3 + 1
        with zipfile.ZipFile(memory, "w", compression=zipfile.ZIP_STORED) as archive:
            for index in range(entry_count):
                archive.writestr(f"ignored/{index:05}.bin", b"")

        # Under-report the count in the EOCD record. The importer must count
        # actual central-directory records before zipfile allocates ZipInfo objects.
        blob = bytearray(memory.getvalue())
        eocd = blob.rfind(b"PK\x05\x06")
        self.assertGreaterEqual(eocd, 0)
        struct.pack_into("<H", blob, eocd + 8, 1)
        struct.pack_into("<H", blob, eocd + 10, 1)

        original_zipfile = codepilot.zipfile.ZipFile
        codepilot.zipfile.ZipFile = lambda *_args, **_kwargs: self.fail(
            "ZipFile must not parse an excessive central directory"
        )
        try:
            with self.assertRaisesRegex(ValueError, "ZIP contains too many entries"):
                codepilot.read_zip_files(bytes(blob))
        finally:
            codepilot.zipfile.ZipFile = original_zipfile

    def test_export_rejects_unsafe_paths_and_bad_zip(self):
        status, _, body = self.request("/api/project/export", "POST", {"files": {"../escape.js": "bad"}})
        self.assertEqual(status, 400)
        self.assertIn("Invalid project file path", json.loads(body)["error"])
        status, _, body = self.request("/api/project/import-zip", "POST", raw=b"not-a-zip", content_type="application/zip")
        self.assertEqual(status, 400)
        self.assertIn("valid ZIP", json.loads(body)["error"])

    def test_github_import_only_accepts_public_repo_urls(self):
        for url in ["http://github.com/owner/repo", "https://example.com/owner/repo", "https://github.com/owner/repo/tree/main/src", "https://user:pass@github.com/owner/repo"]:
            status, _, body = self.request("/api/github/import", "POST", {"url": url})
            self.assertEqual(status, 400, url)
            self.assertIn("repository URL", json.loads(body)["error"])

    def test_github_import_rejects_non_repository_paths_and_invalid_hosts(self):
        invalid_urls = [
            "https://github.com/owner/repo/issues",
            "https://github.com/owner/repo/tree/main",
            "https://github.com.evil.example/owner/repo",
            "https://github.com/owner/repo?tab=readme",
            "https://github.com/owner/repo#readme",
            "https://github.com/../repo",
        ]
        for url in invalid_urls:
            with self.subTest(url=url):
                status, _, body = self.request(
                    "/api/github/import", "POST", {"url": url}
                )
                self.assertEqual(status, 400)
                self.assertIn("repository URL", json.loads(body)["error"])

    def test_oversized_body_and_unknown_api_are_rejected(self):
        # Send only headers: reject the declared size before reading a body.
        with socket.create_connection(("127.0.0.1", self.server.server_port), timeout=3) as sock:
            sock.sendall((
                "POST /api/chat HTTP/1.1\r\nHost: localhost\r\n"
                "Content-Type: application/json\r\nContent-Length: 2097153\r\n"
                "Connection: close\r\n\r\n"
            ).encode())
            chunks = []
            while True:
                part = sock.recv(4096)
                if not part:
                    break
                chunks.append(part)
        response = b"".join(chunks)
        headers, body = response.split(b"\r\n\r\n", 1)
        self.assertIn(b" 413 ", headers.split(b"\r\n", 1)[0])
        self.assertIn(b"2 MiB", body)
        status, _, body = self.request("/api/not-a-route")
        self.assertEqual(status, 404)
        self.assertIn("not found", json.loads(body)["error"].lower())


    def test_safe_project_path_rejects_traversal_and_absolute_paths(self):
        self.assertEqual(codepilot.safe_project_path("src/main.py"), "src/main.py")
        for unsafe in ["../escape.py", "/absolute.py", "folder/../escape.py", "folder\\\\escape.py", ""]:
            with self.subTest(path=unsafe):
                self.assertIsNone(codepilot.safe_project_path(unsafe))

    def test_zip_import_skips_unsafe_and_unsupported_entries(self):
        memory = io.BytesIO()
        with zipfile.ZipFile(memory, "w") as archive:
            archive.writestr("project/src/main.py", "print('safe')")
            archive.writestr("../escape.py", "print('unsafe')")
            archive.writestr("project/image.exe", "not source")
        imported = codepilot.read_zip_files(memory.getvalue())
        self.assertEqual(imported, {"project/src/main.py": "print('safe')"})

    def test_zip_import_rejects_archives_without_supported_text_files(self):
        memory = io.BytesIO()
        with zipfile.ZipFile(memory, "w") as archive:
            archive.writestr("project/image.exe", "not source")
        with self.assertRaisesRegex(ValueError, "No supported UTF-8 source files"):
            codepilot.read_zip_files(memory.getvalue())


if __name__ == "__main__":
    unittest.main()
