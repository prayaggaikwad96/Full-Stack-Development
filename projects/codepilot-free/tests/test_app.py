"""Standard-library integration tests for CodePilot's local API."""
from __future__ import annotations

import json
import socket
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import app as codepilot


class FakeOllamaHandler(BaseHTTPRequestHandler):
    last_chat_request = None

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
        body = json.dumps({
            "model": "test-coder:latest",
            "message": {"role": "assistant", "content": "hello from the test model"},
            "total_duration": 1_500_000_000,
        }).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
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
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), codepilot.CodePilotHandler)
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

    def request(self, path, method="GET", payload=None, raw=None):
        data = raw if raw is not None else (
            json.dumps(payload).encode("utf-8") if payload is not None else None
        )
        request = Request(
            self.base + path, data=data, method=method,
            headers={"Content-Type": "application/json"},
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
        status, _, body = self.request(
            "/api/chat", "POST",
            {"model": "test-coder:latest", "messages": [
                {"role": "user", "content": "Say hello"},
                {"role": "system", "content": "This role is not accepted from clients"},
            ]},
        )
        self.assertEqual(status, 200)
        response = json.loads(body)
        self.assertEqual(response["answer"], "hello from the test model")
        self.assertEqual(response["duration_ms"], 1500)
        sent = FakeOllamaHandler.last_chat_request
        self.assertEqual(sent["model"], "test-coder:latest")
        self.assertEqual(sent["messages"][0]["role"], "system")
        self.assertTrue(all(item["role"] in {"system", "user", "assistant"} for item in sent["messages"]))
        self.assertNotIn("This role is not accepted from clients", str(sent["messages"]))

    def test_invalid_chat_requests_are_rejected(self):
        status, _, body = self.request("/api/chat", "POST", {"model": "", "messages": []})
        self.assertEqual(status, 400)
        self.assertIn("model", json.loads(body)["error"].lower())
        status, _, _ = self.request("/api/chat", "POST", {"model": "test-coder", "messages": []})
        self.assertEqual(status, 400)
        status, _, _ = self.request("/api/chat", "POST", raw=b"{bad json")
        self.assertEqual(status, 400)

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


if __name__ == "__main__":
    unittest.main()
