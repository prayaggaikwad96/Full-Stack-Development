# Full-Stack Development

A hands-on full-stack learning archive with web-development exercises and CodePilot Free, a local-first coding workspace built with Python, browser JavaScript, and Ollama. CI validates Python 3.12–3.15, browser JavaScript, and API integration tests.

## Learning path

1. HTML and CSS fundamentals
2. JavaScript and browser APIs
3. Git and GitHub
4. React and other frontend frameworks
5. Backend development and APIs
6. SQL and NoSQL databases
7. Testing, debugging, and deployment

## Featured project: CodePilot Free

[CodePilot Free](projects/codepilot-free/README.md) is a local-first coding workspace built with Python's standard library, browser JavaScript, and Ollama. It supports a browser-based workspace, live HTML preview, project import/export, and local-model chat.

- [Read the CodePilot README](projects/codepilot-free/README.md)
- [Run the CodePilot test workflow](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/workflows/codepilot-tests.yml)

## Repository layout

- `Prayag Gaikwad/` — canonical learning materials and exercises. Use this path for new work.
- `Full-Stack-Development/` — legacy nested copy from an earlier repository/submodule conversion. Do not use it for new work or copy it over the canonical folder automatically.
- `.github/workflows/` — repository automation.
- `.gitignore` — excludes common generated files, local environments, and secrets.

The legacy nested copy has 524 shared file paths with the canonical project tree. GitHub Actions compared every shared file after normalizing CRLF/CR to LF: 160 files were byte-identical and 364 differed only by line endings; no substantive text or binary differences were found in that report. The nested copy has two empty placeholder files that the canonical tree lacks, and the canonical tree has one empty placeholder the nested copy lacks. Keep the nested copy until the Windows repository/submodule state and local backup have been checked.

## Branch workflow

- `main` is the default branch and source of truth for the published repository.
- `Developer` and `main` are synchronized at the same commit in the current remote comparison. Re-check both refs before future releases or local pushes. Use pull requests for meaningful changes when practical.
- `archive/codepilot-feature-history-before-sync-2026-10-27` is a historical recovery branch containing 36 commits not reachable from `main`; its current tip is 137 commits behind `main`. This divergence is intentional for recovery, not synchronization failure. Preserve it until its unique work is reviewed and independently backed up.
- Preserve recovery references and project-specific feature branches until local backups, unique work, and repository state are verified.
- Do not delete or overwrite branches or project files until their unique work is preserved elsewhere.

## Adding examples

- Keep each example focused on one topic.
- Include setup and run instructions when dependencies are required.
- Update documentation when project structure changes.
- Do not commit API keys, tokens, passwords, real environment files, or private data. Use `.env.example` for non-secret configuration templates.
- Respect licenses and notices for third-party code.

## Validation

GitHub Actions checks the CodePilot Python backend and browser JavaScript, runs integration tests on Python 3.12, 3.13, 3.14, and 3.15, validates representative `.gitignore` rules, and compares the canonical and legacy learning trees.

This is a learning archive; examples may be educational rather than production-ready. Verify behavior using each project's documented toolchain and instructions.
