"""CodePilot Free: local-first coding assistant with a standard-library backend."""
from __future__ import annotations

import io
import json
import os
import re
import urllib.error
import urllib.request
import zipfile
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import PurePosixPath, Path
from typing import Any
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
STATIC_DIR = ROOT / "static"
OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://127.0.0.1:11434").rstrip("/")
MAX_CHAT_BYTES = 2 * 1024 * 1024
MAX_PROJECT_BYTES = 12 * 1024 * 1024
MAX_ZIP_BYTES = 24 * 1024 * 1024
MAX_FILES = 500
MAX_UNPACKED_BYTES = 12 * 1024 * 1024
TEXT_SUFFIXES = {
    ".html", ".htm", ".css", ".js", ".mjs", ".cjs", ".ts", ".tsx", ".jsx",
    ".py", ".md", ".txt", ".json", ".jsonc", ".yaml", ".yml", ".toml", ".xml",
    ".svg", ".sql", ".sh", ".bat", ".ps1", ".java", ".c", ".h", ".cpp", ".hpp",
    ".go", ".rs", ".php", ".vue", ".svelte", ".scss", ".sass", ".less", ".ini",
    ".cfg", ".conf", ".gitignore", ".env.example", ".dockerfile",
}
SYSTEM_PROMPT = (
    "You are CodePilot, a careful and practical programming assistant. Explain assumptions, "
    "prefer secure maintainable code, and give complete examples when asked. Flag destructive "
    "operations. Do not claim you ran code or tests unless you actually did."
)


def encoded(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False).encode("utf-8")


def safe_project_path(value: Any) -> str | None:
    if not isinstance(value, str) or not value or len(value) > 240 or "\\" in value or "\x00" in value:
        return None
    path = PurePosixPath(value)
    if path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts) or value.endswith("/"):
        return None
    return path.as_posix()


def is_text_file(path: str) -> bool:
    name = PurePosixPath(path).name.lower()
    return name in {"dockerfile", "makefile", ".gitignore", ".editorconfig", ".env.example"} or PurePosixPath(path).suffix.lower() in TEXT_SUFFIXES


def read_zip_files(blob: bytes) -> dict[str, str]:
    if not blob or len(blob) > MAX_ZIP_BYTES:
        raise ValueError("ZIP must be smaller than 24 MiB")
    result: dict[str, str] = {}
    unpacked = 0
    try:
        with zipfile.ZipFile(io.BytesIO(blob)) as archive:
            entries = archive.infolist()
            if len(entries) > MAX_FILES * 3:
                raise ValueError("ZIP contains too many entries")
            own_archive = False
            try:
                marker = json.loads(archive.read("__codepilot_manifest__.json").decode("utf-8"))
                own_archive = marker.get("format") == "codepilot-project-v1"
            except (KeyError, UnicodeDecodeError, json.JSONDecodeError, AttributeError):
                pass
            regular = [i for i in entries if not i.is_dir() and i.filename != "__codepilot_manifest__.json"]
            parts_list = [PurePosixPath(i.filename).parts for i in regular]
            wrapper_root = None
            if not own_archive and parts_list and all(len(parts) >= 2 for parts in parts_list):
                roots = {parts[0] for parts in parts_list}
                if len(roots) == 1:
                    wrapper_root = next(iter(roots))
            for info in entries:
                if info.is_dir() or info.flag_bits & 0x1 or info.filename == "__codepilot_manifest__.json":
                    continue
                parts = PurePosixPath(info.filename).parts
                candidate = PurePosixPath(*parts[1:]).as_posix() if wrapper_root and len(parts) > 1 and parts[0] == wrapper_root else PurePosixPath(info.filename).as_posix()
                safe = safe_project_path(candidate)
                if not safe or not is_text_file(safe) or info.file_size > 2 * 1024 * 1024:
                    continue
                unpacked += info.file_size
                if unpacked > MAX_UNPACKED_BYTES or len(result) >= MAX_FILES:
                    raise ValueError("ZIP exceeds the text-project limits")
                try:
                    result[safe] = archive.read(info).decode("utf-8-sig")
                except UnicodeDecodeError:
                    continue
    except zipfile.BadZipFile as exc:
        raise ValueError("That file is not a valid ZIP archive") from exc
    if not result:
        raise ValueError("No supported UTF-8 source files were found in the ZIP")
    return result


class Handler(SimpleHTTPRequestHandler):
    server_version = "CodePilotFree/1.2"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, directory=str(STATIC_DIR), **kwargs)

    def end_headers(self) -> None:
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def send_json(self, status: int, value: Any) -> None:
        body = encoded(value)
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def ollama_get(self) -> dict[str, Any]:
        request = urllib.request.Request(f"{OLLAMA_BASE_URL}/api/tags", headers={"Accept": "application/json"})
        with urllib.request.urlopen(request, timeout=5) as response:
            data = response.read(4 * 1024 * 1024)
        result = json.loads(data.decode("utf-8"))
        if not isinstance(result, dict):
            raise ValueError("Unexpected Ollama response")
        return result

    def do_GET(self) -> None:
        path = urlparse(self.path).path
        if path in {"/api/health", "/api/models"}:
            try:
                result = self.ollama_get()
                models = [m.get("name", "") for m in result.get("models", []) if m.get("name")]
                if path == "/api/health":
                    self.send_json(200, {"server": "ok", "ollama": "online", "models": models})
                else:
                    self.send_json(200, {"models": models})
            except Exception as exc:
                if path == "/api/health":
                    self.send_json(200, {"server": "ok", "ollama": "offline", "models": [],
                        "message": "Start Ollama, then refresh the app.", "detail": str(exc)[:200]})
                else:
                    self.send_json(503, {"error": "Ollama is not available", "detail": str(exc)[:200]})
            return
        if path.startswith("/api/"):
            self.send_json(404, {"error": "API endpoint not found"})
            return
        if path == "/":
            self.path = "/index.html"
        super().do_GET()

    def _read_json(self, maximum: int) -> dict[str, Any] | None:
        try:
            size = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self.send_json(400, {"error": "Invalid Content-Length"})
            return None
        if size <= 0 or size > maximum:
            self.send_json(413, {"error": f"Request must be between 1 byte and {maximum // (1024 * 1024)} MiB"})
            return None
        try:
            payload = json.loads(self.rfile.read(size).decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            self.send_json(400, {"error": "Request body must be valid JSON"})
            return None
        if not isinstance(payload, dict):
            self.send_json(400, {"error": "Request body must be a JSON object"})
            return None
        return payload

    def do_POST(self) -> None:
        path = urlparse(self.path).path
        if path == "/api/chat":
            self._chat()
        elif path == "/api/project/export":
            self._export_project()
        elif path == "/api/project/import-zip":
            self._import_zip()
        elif path == "/api/github/import":
            self._import_github()
        else:
            self.send_json(404, {"error": "API endpoint not found"})

    def _chat(self) -> None:
        payload = self._read_json(MAX_CHAT_BYTES)
        if payload is None:
            return
        model, messages = payload.get("model"), payload.get("messages")
        if not isinstance(model, str) or not model.strip() or len(model) > 160:
            self.send_json(400, {"error": "Choose an installed Ollama model first"})
            return
        if not isinstance(messages, list) or not messages or len(messages) > 80:
            self.send_json(400, {"error": "Messages must be a non-empty list of up to 80 items"})
            return
        clean = [{"role": "system", "content": SYSTEM_PROMPT}]
        chars = 0
        for item in messages:
            if not isinstance(item, dict):
                continue
            role, content = item.get("role"), item.get("content")
            if role not in {"user", "assistant"} or not isinstance(content, str):
                continue
            chars += len(content)
            if chars > 1_500_000:
                self.send_json(413, {"error": "Conversation too large. Start a new chat."})
                return
            clean.append({"role": role, "content": content})
        if len(clean) < 2:
            self.send_json(400, {"error": "Include at least one user message"})
            return
        body = encoded({"model": model.strip(), "messages": clean, "stream": True, "options": {"temperature": 0.2}})
        request = urllib.request.Request(f"{OLLAMA_BASE_URL}/api/chat", data=body,
            headers={"Content-Type": "application/json", "Accept": "application/x-ndjson"}, method="POST")
        headers_sent = False
        try:
            response = urllib.request.urlopen(request, timeout=240)
        except urllib.error.HTTPError as exc:
            detail = exc.read(1200).decode("utf-8", errors="replace")
            self._send_json(502, {"error": f"Ollama returned HTTP {exc.code}", "detail": detail[:400]})
            return
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            self._send_json(503, {"error": "Local AI connection failed", "detail": str(exc)[:300]})
            return

        try:
            with response:
                self.send_response(200)
                self.send_header("Content-Type", "text/event-stream; charset=utf-8")
                self.send_header("Cache-Control", "no-cache, no-transform")
                self.send_header("X-Accel-Buffering", "no")
                self.send_header("Connection", "close")
                self.close_connection = True
                self.end_headers()
                headers_sent = True
                done: dict[str, Any] = {"done": True, "model": model.strip(), "duration_ms": 0}
                for line in response:
                    if not line.strip():
                        continue
                    try:
                        chunk = json.loads(line.decode("utf-8"))
                    except (UnicodeDecodeError, json.JSONDecodeError):
                        continue
                    delta = chunk.get("message", {}).get("content", "")
                    if delta:
                        packet = json_bytes({"delta": delta})
                        self.wfile.write(b"data: " + packet + b"\n\n")
                        self.wfile.flush()
                    if chunk.get("done"):
                        done = {"done": True, "model": chunk.get("model", model.strip()), "duration_ms": round(chunk.get("total_duration", 0) / 1_000_000)}
                self.wfile.write(b"data: " + json_bytes(done) + b"\n\n")
                self.wfile.flush()
        except (urllib.error.URLError, TimeoutError, OSError, ValueError) as exc:
            message = {"error": f"Local AI stream interrupted: {str(exc)[:300]}"}
            if not headers_sent:
                self._send_json(503, message)
            else:
                try:
                    self.wfile.write(b"data: " + json_bytes(message) + b"\n\n")
                    self.wfile.flush()
                except (BrokenPipeError, ConnectionResetError, OSError):
                    pass

    def _export_project(self) -> None:
        payload = self._read_json(MAX_PROJECT_BYTES)
        if payload is None:
            return
        files = payload.get("files")
        if not isinstance(files, dict) or not files or len(files) > MAX_FILES:
            self.send_json(400, {"error": f"Provide between 1 and {MAX_FILES} project files"})
            return
        memory = io.BytesIO()
        total = 0
        with zipfile.ZipFile(memory, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.writestr("__codepilot_manifest__.json", encoded({"format": "codepilot-project-v1"}))
            for name, content in files.items():
                safe = safe_project_path(name)
                if not safe or not isinstance(content, str):
                    self.send_json(400, {"error": f"Invalid project file path or contents: {str(name)[:100]}"})
                    return
                data = content.encode("utf-8")
                total += len(data)
                if total > MAX_UNPACKED_BYTES:
                    self.send_json(413, {"error": "Project text exceeds the 12 MiB export limit"})
                    return
                archive.writestr(safe, data)
        result = memory.getvalue()
        self.send_response(200)
        self.send_header("Content-Type", "application/zip")
        self.send_header("Content-Disposition", 'attachment; filename="codepilot-project.zip"')
        self.send_header("Content-Length", str(len(result)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(result)

    def _import_zip(self) -> None:
        try:
            size = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self.send_json(400, {"error": "Invalid Content-Length"})
            return
        if size <= 0 or size > MAX_ZIP_BYTES:
            self.send_json(413, {"error": "ZIP upload must be smaller than 24 MiB"})
            return
        try:
            self.send_json(200, {"files": read_zip_files(self.rfile.read(size))})
        except ValueError as exc:
            self.send_json(400, {"error": str(exc)})

    def _import_github(self) -> None:
        payload = self._read_json(16 * 1024)
        if payload is None:
            return
        raw_url = payload.get("url")
        if not isinstance(raw_url, str) or len(raw_url) > 300:
            self.send_json(400, {"error": "Enter a public GitHub repository URL"})
            return
        parsed = urlparse(raw_url.strip())
        parts = [part for part in parsed.path.strip("/").split("/") if part]
        if parsed.scheme != "https" or parsed.hostname != "github.com" or parsed.username or len(parts) != 2:
            self.send_json(400, {"error": "Use a public repository URL like https://github.com/owner/repository"})
            return
        owner, repo = parts
        repo = repo[:-4] if repo.endswith(".git") else repo
        valid = re.compile(r"^[A-Za-z0-9_.-]{1,100}$")
        if not valid.fullmatch(owner) or not valid.fullmatch(repo) or owner in {".", ".."} or repo in {".", ".."}:
            self.send_json(400, {"error": "That repository URL is not valid"})
            return
        headers = {"User-Agent": "CodePilot-Free/1.2", "Accept": "application/vnd.github+json"}
        try:
            with urllib.request.urlopen(urllib.request.Request(f"https://api.github.com/repos/{owner}/{repo}", headers=headers), timeout=12) as response:
                metadata = json.loads(response.read(512 * 1024).decode("utf-8"))
            branch = metadata.get("default_branch", "main")
            if not isinstance(branch, str) or not re.fullmatch(r"[A-Za-z0-9_./-]{1,200}", branch) or ".." in PurePosixPath(branch).parts:
                self.send_json(502, {"error": "GitHub returned an invalid default branch"})
                return
            archive_url = f"https://codeload.github.com/{owner}/{repo}/zip/refs/heads/{branch}"
            with urllib.request.urlopen(urllib.request.Request(archive_url, headers={"User-Agent": "CodePilot-Free/1.2"}), timeout=25) as response:
                blob = response.read(MAX_ZIP_BYTES + 1)
            files = read_zip_files(blob)
            self.send_json(200, {"files": files, "count": len(files), "repository": f"{owner}/{repo}", "branch": branch})
        except urllib.error.HTTPError as exc:
            self.send_json(502, {"error": f"GitHub returned HTTP {exc.code}", "detail": exc.read(800).decode("utf-8", errors="replace")})
        except urllib.error.URLError as exc:
            self.send_json(502, {"error": "Could not download that public GitHub repository", "detail": str(exc.reason)[:200]})
        except (TimeoutError, json.JSONDecodeError, UnicodeDecodeError, ValueError) as exc:
            self.send_json(502, {"error": "Could not import the repository", "detail": str(exc)[:240]})

    def log_message(self, fmt: str, *args: Any) -> None:
        # Avoid dumping request bodies or query-string contents into terminal logs.
        super().log_message(fmt, *args)


def main() -> None:
    host = os.environ.get("CODEPILOT_HOST", "127.0.0.1")
    port = int(os.environ.get("CODEPILOT_PORT", "8000"))
    try:
        server = ThreadingHTTPServer((host, port), Handler)
    except OSError as exc:
        raise SystemExit(f"Could not start CodePilot on {host}:{port}: {exc}") from exc
    print(f"CodePilot Free: http://{host}:{port}  |  Ollama: {OLLAMA_BASE_URL}")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping CodePilot.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
