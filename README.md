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
- `Full-Stack-Development/` — retained legacy copy from the previous repository/submodule conversion. Its files are not guaranteed to match the primary copy; compare before deleting or consolidating anything.
- `.github/workflows/` — repository automation.
- `.gitignore` — excludes common generated files, local environments, and secrets.

**Canonical working directory:** use `Prayag Gaikwad/` for new learning notes and examples unless you are intentionally updating the legacy copy. Keep related assets together and use descriptive filenames.

## Branch workflow

- `main` is the default branch and source of truth for the published repository.
- `Developer` is retained as the development branch. Update it from `main` before starting new work; merge changes back through a pull request when practical.
- `archive/developer-before-sync-2026-10-27` is a recovery snapshot. Keep it until the repository's folder history has been reviewed and verified.
- `github-sync` is a historical synchronization branch. Do not use it as the base for new work.
- `feat/codepilot-free-app` contains a separate CodePilot project. Preserve it unless the project is deliberately retired or safely relocated.

Avoid force-pushing or deleting branches as a way to resolve divergent histories. Compare commits and inspect file changes first.

## Adding examples

- Keep each example focused on one topic.
- Include setup and run instructions when dependencies are required.
- Update the relevant documentation when a project's structure changes.
- Do not commit API keys, tokens, passwords, real environment files, or private data. Use `.env.example` for non-secret configuration templates.
- Respect licenses and notices for third-party code.

## Validation

A GitHub Actions workflow checks representative `.gitignore` rules. Run the relevant tests for any executable project before merging changes.

This is a learning archive; examples may be educational rather than production-ready. Verify behavior using the toolchain and instructions documented for each project.
