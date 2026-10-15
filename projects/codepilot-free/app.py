"""Local-first CodePilot backend. Standard-library-only Python server."""
from __future__ import annotations
import json
import os
import urllib.error
import urllib.request
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
STATIC_DIR = ROOT / "static"
OLLAMA_BASE_URL = os.environ.get("OLLAMA_BASE_URL", "http://127.0.0.1:11434").rstrip("/")
MAX_BODY_BYTES = 2 * 1024 * 1024
SYSTEM_PROMPT = (
    "You are CodePilot, a careful and practical programming assistant. "
    "Explain assumptions, prefer secure maintainable code, and give complete examples when asked. "
    "Flag destructive operations. Do not claim that you ran code or tests unless you actually did."
)

def encoded(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False).encode("utf-8")

class Handler(SimpleHTTPRequestHandler):
    server_version = "CodePilotFree/1.0"

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
        request = urllib.request.Request(f"{OLLAMA_BASE_URL}/api/tags")
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

    def do_POST(self) -> None:
        if urlparse(self.path).path != "/api/chat":
            self.send_json(404, {"error": "API endpoint not found"})
            return
        try:
            size = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            self.send_json(400, {"error": "Invalid Content-Length"})
            return
        if size <= 0 or size > MAX_BODY_BYTES:
            self.send_json(413, {"error": "Request body must be between 1 byte and 2 MiB"})
            return
        try:
            payload = json.loads(self.rfile.read(size).decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            self.send_json(400, {"error": "Request body must be valid JSON"})
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
        body = encoded({"model": model.strip(), "messages": clean, "stream": False,
                        "options": {"temperature": 0.2}})
        request = urllib.request.Request(f"{OLLAMA_BASE_URL}/api/chat", data=body,
            headers={"Content-Type": "application/json", "Accept": "application/json"}, method="POST")
        try:
            with urllib.request.urlopen(request, timeout=240) as response:
                result = json.loads(response.read(8 * 1024 * 1024).decode("utf-8"))
            answer = result.get("message", {}).get("content", "")
            if not isinstance(answer, str) or not answer.strip():
                self.send_json(502, {"error": "Model returned an empty answer. Try again."})
                return
            self.send_json(200, {"answer": answer, "model": result.get("model", model),
                "duration_ms": round(result.get("total_duration", 0) / 1_000_000)})
        except urllib.error.HTTPError as exc:
            self.send_json(502, {"error": f"Ollama returned HTTP {exc.code}",
                "detail": exc.read(1200).decode("utf-8", errors="replace")})
        except urllib.error.URLError as exc:
            self.send_json(503, {"error": "Cannot connect to Ollama. Check that it is running and the model is installed.",
                "detail": str(exc.reason)[:200]})
        except (TimeoutError, json.JSONDecodeError, UnicodeDecodeError, ValueError) as exc:
            self.send_json(502, {"error": "Could not complete the model request", "detail": str(exc)[:200]})

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
