# Full-Stack Development

A hands-on full-stack learning archive with web-development exercises and CodePilot Free, a local-first coding workspace built with Python, browser JavaScript, and Ollama. CI validates Python 3.12–3.15 against Node.js 22 and 24, plus browser JavaScript and API integration tests.

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

The archived nested-tree audit report covers 524 shared file paths: 160 files were byte-identical and 364 differed after line-ending normalization; no substantive text or binary differences were found in that report. It also found two empty placeholders only in the nested copy and one only in the canonical tree. These counts describe that audit run, not a guarantee that the trees remain unchanged. Keep the nested copy until Windows repository/submodule state and local backups are checked.

## Branch workflow

- `main` is the default branch and source of truth for the published repository.
- `Developer` is not currently synchronized with `main`. The latest GitHub comparison confirms a shared merge base but divergent branch tips; ahead/behind counts are live values and can change with every push. Compare the exact refs before any integration. Do not force-push, reset, or overwrite either ref. Run `docs/windows-repository-audit.ps1` from the local Windows checkout, verify backups and unique commits on both sides, then reconcile intentionally through a reviewable candidate and tests.
- `archive/codepilot-feature-history-before-sync-2026-10-27` is a historical recovery branch containing CodePilot files and history not reachable from the current `main` comparison. PR #8 integrated a CodePilot implementation into `main`, but that does not make this separate historical branch disposable. Preserve it until its unique commits are reviewed and independently backed up.
- Preserve recovery references and project-specific feature branches until local backups, unique work, and repository state are verified.
- Do not delete or overwrite branches or project files until their unique work is preserved elsewhere.

## Adding examples

- Keep each example focused on one topic.
- Include setup and run instructions when dependencies are required.
- Update documentation when project structure changes.
- Do not commit API keys, tokens, passwords, real environment files, or private data. Use `.env.example` for non-secret configuration templates.
- Respect licenses and notices for third-party code.

## Validation

GitHub Actions checks the CodePilot Python backend and browser JavaScript, runs integration tests on Python 3.12, 3.13, 3.14, and 3.15, validates representative `.gitignore` rules, and compares the canonical and legacy learning trees. The CodePilot test matrix runs on every pull request so its result remains available when repository branch rules are configured; push-triggered runs for that project remain path-filtered.

This is a learning archive; examples may be educational rather than production-ready. Verify behavior using each project's documented toolchain and instructions.

## Quality, security, and contributions

- [Contributing guide](CONTRIBUTING.md) — branch workflow, local validation commands, and review expectations.
- [Security policy](SECURITY.md) — how to disclose a vulnerability privately.
- [Repository health and synchronization audit](docs/repository-health-audit-2026-10-29.md) — timestamped remote snapshot; use the live GitHub comparison for current branch counts and check status. Includes tested CI evidence and outstanding local/security checks.
- [CodeQL analysis workflow](.github/workflows/codeql.yml) scans GitHub Actions workflows, JavaScript/TypeScript, and Python on pushes, pull requests, and a weekly schedule.
- [Dependabot configuration](.github/dependabot.yml) requests weekly GitHub Actions dependency updates. Review its pull requests before merging.
- Use `.github/pull_request_template.md` to record tests, security hygiene, documentation, and compatibility considerations.
