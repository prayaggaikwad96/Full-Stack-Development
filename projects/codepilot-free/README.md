# CodePilot Free

A local-first AI coding workspace built with plain HTML/CSS/JavaScript and Python's standard library. It includes a browser editor, starter files, live HTML preview, and AI chat through locally installed Ollama models.

## Cost model

CodePilot is free and open source. When you use a local Ollama model, there is no per-token API bill. You still need a compatible computer, storage, electricity, and the time to download a model. Hosted AI free quotas can change; this app does not depend on them.

## Features

- Streaming chat with models already installed in Ollama
- Include or exclude the active file as context
- Explain, debug, refactor, and test prompt shortcuts
- Browser-based multi-file workspace with lightweight syntax highlighting, auto-save, download, and live HTML preview
- Import a browser-selected folder or ZIP, export a whole project ZIP, or import text/source files from a public GitHub repository without a token
- No account, API key, telemetry, external JS framework, or CDN required
- Python backend proxy to avoid browser CORS problems when using local Ollama

## Windows setup

1. Install a supported Python version (3.12–3.15 are currently tested in CI) and [Ollama](https://ollama.com/download).
2. In PowerShell run: `ollama pull qwen2.5-coder:7b`
3. From this folder run: `python app.py` (or `py app.py`).
4. Open http://127.0.0.1:8000 and refresh the model list.

You can also double-click `run_windows.bat`.

## macOS/Linux

Install Python 3.10+ and Ollama, then run:

```bash
ollama pull qwen2.5-coder:7b
python3 app.py
```

Open http://127.0.0.1:8000.

## Configuration

- `CODEPILOT_HOST` (default `127.0.0.1`)
- `CODEPILOT_PORT` (default `8000`)
- `OLLAMA_BASE_URL` (default `http://127.0.0.1:11434`)

Keep the app bound to localhost unless you add suitable authentication and network controls. If you change `OLLAMA_BASE_URL` to a remote server, that server receives model prompts.

## Import/export and GitHub support

Use **Import folder** to select a folder in a supported desktop browser, **Import ZIP** to restore an archive, and **Export project ZIP** to back up the workspace. **Public GitHub repo** imports supported text/source files from a public repository URL; it does not need a GitHub token and does not push changes or read private repositories. Archives and imported projects are limited by size and file-count safety checks; binary assets are skipped.

## Privacy and limitations

There is no login, analytics, or telemetry. With a local model, prompts go to the local Ollama endpoint. Workspace files and chat history are stored in this browser's local storage; the server does not persist them. Download files you want to keep as browser storage is not a backup.

This is a useful starter, not a full VS Code replacement: the editor is a textarea with lightweight syntax coloring but no IntelliSense, diagnostics, debugger, or integrated Git commit/push. Folder import depends on browser support. The preview combines `index.html`, `style.css`, and `app.js`.

## License

MIT. See [LICENSE](LICENSE).

## Developer checks

The project includes standard-library integration tests using a fake Ollama server, so tests do not need a downloaded AI model:

```bash
python -m py_compile app.py tests/test_app.py
node --check static/app.js
python -m unittest discover -s tests -v
```

GitHub Actions runs these checks on relevant pull requests and pushes to `main`, plus manual dispatch. The CI matrix tests Python 3.12, 3.13, 3.14, and 3.15 with Node.js 20. The tests verify the static workspace, model discovery, chat proxy, request validation, size limits, and unknown API routes.
