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

The legacy nested copy has 524 shared file paths with the canonical project tree. GitHub Actions compared every shared file after normalizing CRLF/CR to LF: 160 files are byte-identical and 364 differ only by line endings; no substantive text or binary differences were found. The nested copy has two empty placeholder files that the canonical tree lacks, and the canonical tree has one empty placeholder the nested copy lacks. The report is available in the [normalized comparison artifact](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40551308262/artifacts/12754478961). Keep the nested copy until the Windows repository/submodule state and local backup have been checked.

## Branch workflow

- `main` is the default branch and source of truth for the published repository.
- `Developer` was synchronized to the same commit as `main` on October 27, 2026. Keep it aligned with `main`; use a pull request for meaningful changes when practical.
- `github-sync` and `archive/developer-before-sync-2026-10-27` are redundant refs currently aligned with `main`; do not use them for new work. Their deletion awaits the local branch-reference check because the connected GitHub integration cannot delete refs.
- `backup/legacy-tree-before-cleanup-2026-10-27` is a historical Git recovery ref, not an independent/off-site backup. Preserve it until local backups and the duplicate-tree comparison are confirmed.
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
