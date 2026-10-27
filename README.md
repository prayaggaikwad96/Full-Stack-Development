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

- `Prayag Gaikwad/` — canonical learning materials and exercises. Use this path for new work.
- `Full-Stack-Development/` — legacy nested copy from an earlier repository/submodule conversion. Do not use it for new work or copy it over the canonical folder automatically.
- `.github/workflows/` — repository automation.
- `.gitignore` — excludes common generated files, local environments, and secrets.

The legacy nested copy contains 524 paths shared with the canonical project tree, 160 of which have identical Git blob IDs and 364 of which have different blob IDs. A sampled HTML pair differed only in CRLF/LF line endings after normalization, but all differing pairs have not yet been verified. Keep the legacy copy until a complete normalized comparison and a local backup are confirmed.

## Branch workflow

- `main` is the default branch and source of truth for the published repository.
- `Developer` was synchronized to the same commit as `main` on October 27, 2026. Keep it aligned with `main`; use a pull request for meaningful changes when practical.
- `github-sync` is an obsolete ancestor of `main` with no commits unique to it. Do not use it as a base for new work.
- `archive/developer-before-sync-2026-10-27` is an older ancestor branch whose current tree contains only this README. It is **not** a complete source-code backup.
- `feat/codepilot-free-app` contains a separate CodePilot project and tests, including commits not present on `main`. Keep it unless that project is deliberately merged or retired.

Do not delete or overwrite branches or project files until you confirm their unique work is preserved elsewhere.

## Adding examples

- Keep each example focused on one topic.
- Include setup and run instructions when dependencies are required.
- Update the relevant documentation when a project's structure changes.
- Do not commit API keys, tokens, passwords, real environment files, or private data. Use `.env.example` for non-secret configuration templates.
- Respect licenses and notices for third-party code.

## Validation

The GitHub Actions workflow checks representative `.gitignore` rules. It runs for relevant changes on `main`, pull requests targeting `main`, and manual dispatch. Run the relevant tests for executable projects before merging changes.

This is a learning archive; examples may be educational rather than production-ready. Verify behavior using the toolchain and instructions documented for each project.
