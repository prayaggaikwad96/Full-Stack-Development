# Repository health audit — 2026-10-27

## Live GitHub status

This audit was refreshed against the live GitHub repository on October 27, 2026. It does not inspect the Windows working copy at `C:\Prayag Gaikwad`; local changes, untracked files, index state, and local branches must still be audited separately before any destructive local synchronization.

- Repository: `prayaggaikw96/Full-Stack-Development`
- Default branch: `main`
- `main` and `Developer` are identical at commit `895cfd749c5851c8de9d2a655106d423e305aed7`.
- `github-sync` and `archive/developer-before-sync-2026-10-27` currently point to that same commit too. They have no unique commit history relative to `main`, but are redundant refs, not a complete independent backup.
- `feat/codepilot-free-app` is intentionally retained. Compared with `main`, it has 34 commits only on that branch and 72 commits only on `main`. It includes a separate CodePilot project, test suite, and workflow. Do not delete it unless this separate work is intentionally retired or preserved elsewhere.
- No open pull requests were found during this check.

## Duplicate source trees

The root `Prayag Gaikwad/` tree is the documented canonical location. Existing GitHub tree comparison records:

- Canonical tree: 525 files.
- Nested legacy tree at `Full-Stack-Development/Prayag Gaikwad/`: 526 files.
- Shared paths: 524.
- Identical Git blob IDs among shared paths: 160.
- Shared paths with different blob IDs: 364.
- Legacy-only files: two empty `.gitkeep.txt` placeholders.
- Canonical-only file: one empty `.gitkeep.txt` placeholder.

One sampled HTML pair became identical after normalizing CRLF to LF, suggesting line endings explain at least some differences. All 364 differing pairs have not been compared after normalization. Do not delete the nested folder or overwrite either tree until a complete comparison and verified local backup are available.

## Validation and CI

- GitHub Actions run [40542403116](https://github.com/prayaggaikw96/Full-Stack-Development/actions/runs/40542403116), titled “ci: run gitignore validation on relevant main pushes,” completed successfully on a push to `main` at commit `db5888b235cc3ea1619d2439549e1dc178834041`.
- That run verifies the root `.gitignore` workflow; it does not test every learning example or the separate CodePilot project.
- The CodePilot branch has its own workflow and tests. Preserve that branch and its unique work while reviewing or completing its integration.
- A successful run on the latest `main` commit should be checked again after future changes.

## Safe next steps

1. Create a full local backup and a Git bundle before changing the Windows repositories.
2. Capture `git status --short --branch` for both `C:\Prayag Gaikwad` and `C:\Prayag Gaikwad\Full-Stack-Development`.
3. Compare local branches and remotes against GitHub before fetching, merging, resetting, deleting, or replacing paths.
4. Normalize and compare all 364 shared files before deciding whether the nested copy can be removed.
5. The two redundant remote refs can be deleted after a separate confirmation that no external workflow, deployment, or collaborator depends on them. This connector does not expose a branch-deletion operation, so they have not been deleted here.
6. Keep `main` and `Developer` aligned. Retain `feat/codepilot-free-app` while its unique work remains useful.
