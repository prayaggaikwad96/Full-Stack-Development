# Repository health audit — 2026-10-27

## Scope and confidence

This audit was performed against the live GitHub repository. It does not inspect the Windows working copy at `C:\Prayag Gaikwad`; local changes, untracked files, and local branch configuration must be audited separately before any destructive sync.

## Branches and pull requests

At the initial audit, `main` and `Developer` pointed to the same commit (`bf06c312fa969da6eca7b32deea6d579bf2abcd4`). The remote updates made on October 27, 2026, are being propagated to `Developer` after verification.

- `github-sync` was an ancestor of `main`, 54 commits behind at the initial audit, with no unique commits relative to `main`.
- `archive/developer-before-sync-2026-10-27` was an ancestor of `main`, 84 commits behind at the initial audit. Its current tree has only `README.md`; it is not a complete source backup.
- `feat/codepilot-free-app` has 34 commits not on `main` at the initial audit and contains a separate CodePilot project and tests. Retain it until the project is intentionally merged or retired.
- No open pull requests were found at the initial audit.

The available GitHub connection can read and update refs but does not expose a branch-deletion operation. These stale branches therefore have not been deleted by this audit.

## Duplicate source trees

The root `Prayag Gaikwad/` tree is the documented canonical location. In the GitHub tree at the start of this audit:

- Canonical tree: 525 files.
- Nested legacy tree at `Full-Stack-Development/Prayag Gaikwad/`: 526 files.
- Shared paths: 524.
- Identical Git blob IDs among shared paths: 160.
- Shared paths with different blob IDs: 364.
- Legacy-only files: two empty `.gitkeep.txt` placeholders.
- Canonical-only file: one empty `.gitkeep.txt` placeholder.

An inspected HTML pair became identical after normalizing CRLF to LF, suggesting line-ending conversion accounts for at least some differing blobs. The 364 pairs have **not** all been normalized and compared; do not assume every difference is only line endings. Do not delete the legacy folder or copy it over the canonical tree until a complete comparison and a verified local backup are available.

## Validation and CI

The root `.gitignore` ignores common Python caches and virtual environments, Node/build output, logs, editor/OS files, and environment files while allowing `.env.example` and `.env.sample`.

The workflow `.github/workflows/gitignore-check.yml` now runs for relevant pushes to `main`, pull requests targeting `main`, and manual dispatch. Before this change, it did not have a push trigger, and no status checks were reported for the current `main` commit. A successful run on the latest `main` commit must be confirmed separately.

The CodePilot test workflow has a recent successful run on its feature branch, but this is not a test of the canonical learning archive.

## Safe next steps

1. Create a full local backup and a Git bundle before changing the Windows repositories.
2. Capture `git status --short --branch` for both `C:\Prayag Gaikwad` and `C:\Prayag Gaikwad\Full-Stack-Development`.
3. Compare local branches and remotes against GitHub before fetching, merging, resetting, deleting, or replacing any paths.
4. Normalize and compare all 364 shared files before deciding whether the nested copy can be removed.
5. After the remote sync is verified locally, delete stale remote branches only after confirming their tips are reachable from `main`. Keep `feat/codepilot-free-app` while its unique work is still needed.
