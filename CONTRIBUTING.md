# Contributing

Thank you for helping improve this learning archive and its projects.

## Before opening a pull request

1. Start from the latest `main` and create a focused topic branch.
2. Keep each change small enough to review. Explain the problem, the approach, and any behavior or compatibility impact.
3. Add or update tests when behavior changes. Update the relevant README when setup, dependencies, limitations, or project structure changes.
4. Never commit API keys, tokens, passwords, private data, real `.env` files, generated caches, or local build output. Use example configuration files for non-secret placeholders.
5. Preserve unrelated files and meaningful Git history. Do not force-push shared branches or delete recovery branches as part of routine cleanup.

## CodePilot Free checks

From the repository root, run:

```bash
cd projects/codepilot-free
python -m py_compile app.py tests/test_app.py
node --check static/app.js
python -m unittest discover -s tests -v
```

GitHub Actions also tests Python 3.12–3.15 with Node.js 22 and 24. The workflow matrix is the authoritative CI result for a pull request.

## Learning-material changes

Keep examples focused, label educational shortcuts or limitations, and include toolchain/setup instructions where needed. Preserve third-party license and copyright notices. Do not add a repository-wide license without reviewing the provenance and intended licensing of the existing learning archive.

## Pull requests

Open a pull request against `main`. Complete the repository pull-request template, link any relevant issue, summarize the verification performed, and explain when a check is not applicable. Address review comments or document why a suggestion is not adopted before merging.

`Developer` is intended to mirror `main`; fast-forward it only when it has no commits unique to itself. Historical archive branches are intentional recovery points and must not be force-updated or deleted without review.
