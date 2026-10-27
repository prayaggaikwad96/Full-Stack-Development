# Repository health audit — 2026-10-27

## Verified remote state
- Repository: `prayaggaikwad96/Full-Stack-Development`; default branch `main`.
- `main` and `Developer` are aligned. Re-check current branch heads before relying on the exact SHA after future commits.
- The CodePilot app was integrated by merged [PR #8](https://github.com/prayaggaikwad96/Full-Stack-Development/pull/8), merge commit `b58350197c9d277c6b5389bb8a0ac1540e5842a4`. Current `main` includes `projects/codepilot-free/` and `.github/workflows/codepilot-tests.yml`.
- CodePilot syntax and API integration tests passed on Python 3.10 and 3.12 on the integration branch and again after the merge. Latest recorded main test: [run 40553590167](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40553590167).
- The post-merge nested-tree audit and .gitignore validation also passed: [nested-tree audit](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40553298925), [gitignore validation](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40553298805).
- The obsolete `github-sync` and `archive/developer-before-sync-2026-10-27` branches were deleted after guarded ancestry checks.
- `backup/legacy-tree-before-cleanup-2026-10-27` remains as an older recovery ref; it is not an off-site backup.
- The original `feat/codepilot-free-app` branch contains the development history for CodePilot. Its application code and tests are now on `main`; synchronize its active tip to `main` only after archiving the old tip, so the old history remains recoverable.

## Nested tree normalized comparison
Workflow: [Audit nested project tree](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40553298925)

Compared `Prayag Gaikwad/` with `Full-Stack-Development/Prayag Gaikwad/`, normalizing CRLF and CR to LF for UTF-8 text and preserving all other characters; binary files were compared byte-for-byte.

- Canonical file count: 525
- Nested file count: 526
- Relative file paths compared (union): 527
- Identical files: 160
- Line-ending-only differences: 364
- Substantive text differences: 0
- Binary differences: 0
- Canonical-only: one empty `.gitkeep.txt` under `Prayag Gaikwad CSS/Projects/`
- Nested-only: two empty placeholders under `Advanced Projects/` and `Intermediate Projects/`

Download the [normalized comparison artifact](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40551308262/artifacts/12754478961). Exact path/SHA inventories are in [CSV](nested-tree-comparison-2026-10-27.csv), [JSON](nested-tree-comparison-2026-10-27.json), and [differing blob pairs](nested-tree-differing-blobs-2026-10-27.json).

The 364 matching relative file pairs differ only by line endings. The nested root also has an older README and duplicate workflow file outside the compared learning-directory contents. No learning files were deleted.

## Windows local repositories
GitHub cannot inspect live local working trees. Actual remotes, checked-out commits, dirty files, submodule state, and local backup integrity under `C:\\Prayag Gaikwad` and `C:\\Prayag Gaikwad\\Full-Stack-Development` remain unverified until the local read-only audit is run and its output reviewed: [Windows audit script](windows-repository-audit.ps1). It inspects both repositories and writes a normalized per-file CSV under `%TEMP%`.

## Completion status
Verified remotely: CodePilot integration and passing tests, current main/Developer synchronization, normalized nested-tree comparison, and cleanup of redundant historical aliases. Local Windows synchronization remains unverified because the local audit output has not yet been supplied.
