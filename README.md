# Full Stack Development

A personal learning archive for full-stack web development, with hands-on examples, practice files, and small projects.

## Learning path

1. HTML and CSS fundamentals
2. JavaScript and browser APIs
3. Git and GitHub
4. React and other frontend frameworks
5. Backend development and APIs
6. SQL and NoSQL databases
7. Testing, debugging, and deployment

## Repository layout

- `Prayag Gaikwad/` — primary learning materials and exercises.
- `Full-Stack-Development/` — a retained legacy snapshot from the previous repository/submodule conversion. Files inside it are not guaranteed to match the primary copy.
- `.github/workflows/` — repository automation.
- `.gitignore` — excludes common generated files, local environments, and secrets.

**Canonical working directory:** use `Prayag Gaikwad/` for new learning notes and examples. The legacy copy is retained for recovery and comparison; do not copy it over the primary directory automatically because 364 overlapping files have different Git blob contents.

## Branch workflow

- `main` is the default branch and source of truth for the published repository.
- `Developer` is synchronized with `main` as of October 27, 2026. Keep the two aligned by fast-forwarding `Developer` from `main` before beginning new work, then use a pull request for meaningful changes when practical.
- `archive/developer-before-sync-2026-10-27` preserves the previous development tip for recovery.
- `github-sync` is an older synchronization branch, 53 commits behind `main`; do not use it as the base for new work.
- `feat/codepilot-free-app` contains a separate CodePilot project and tests. Keep it separate from the learning archive unless deliberately integrating the project.

Avoid force-pushing or deleting branches as a way to resolve divergent histories. Compare commits and inspect file changes first.

## Adding examples

- Keep each example focused on one topic.
- Include setup and run instructions when dependencies are required.
- Update the relevant documentation when a project's structure changes.
- Do not commit API keys, tokens, passwords, real environment files, or private data. Use `.env.example` for non-secret configuration templates.
- Respect licenses and notices for third-party code.

## Validation

The GitHub Actions workflow checks representative `.gitignore` rules. Run the relevant tests for executable projects before merging changes.

This is a learning archive; examples may be educational rather than production-ready. Verify behavior using the toolchain and instructions documented for each project.
