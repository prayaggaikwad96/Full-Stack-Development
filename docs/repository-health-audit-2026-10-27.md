# Repository health audit — 2026-10-27

## Verified remote state
- Repository: `prayaggaikwad96/Full-Stack-Development`; default branch `main`.
- Current `main`, `Developer`, and `feat/codepilot-free-app` all point to `79a988fc279fdb174d05c88cfe2b34556d317376` as of the latest remote check on 2026-10-28; GitHub compare confirms both working branches are identical to `main`.
- CodePilot Free is integrated on `main` by [merged PR #8](https://github.com/prayaggaikwad96/Full-Stack-Development/pull/8), merge commit `b58350197c9d277c6b5389bb8a0ac1540e5842a4`. It includes the application, tests, MIT license, Windows launcher, and GitHub Actions workflow.
- CodePilot tests passed on Python 3.10 and 3.12 on the current `main` tip `79a988f`: [run 40566305724](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40566305724). A run for the synchronized `feat/codepilot-free-app` branch is underway: [run 40566383624](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40566383624).
- The latest nested-tree comparison and root gitignore validation passed on the current commit: [nested tree audit](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40566305675), [gitignore validation](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40566305867).
- The redundant branches `github-sync` and `archive/developer-before-sync-2026-10-27` were deleted after guarded ancestry checks.
- The original CodePilot feature history remains preserved at `archive/codepilot-feature-history-before-sync-2026-10-27`, tip `6c68a09756d30a004f2519dab06c9da7494005c8`. Its active `feat/codepilot-free-app` branch now matches `main`.
- `backup/legacy-tree-before-cleanup-2026-10-27` remains an older recovery reference and is not an off-site backup.

## Nested tree normalized comparison
Workflow: [Audit nested project tree](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40553807989)

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

All 364 matching relative file pairs differ only by line endings. The nested root also has an older README and duplicate workflow file outside the compared learning-directory contents. No learning files were deleted.

## Windows local repositories
GitHub cannot inspect live local working trees. Actual remotes, checked-out commits, dirty files, submodule state, and local backup integrity under `C:\\Prayag Gaikwad` and `C:\\Prayag Gaikwad\\Full-Stack-Development` remain unverified until the local read-only audit is run and its output reviewed: [Windows audit script](windows-repository-audit.ps1). It inspects both repositories and writes a normalized per-file CSV under `%TEMP%`.

## Updated remote verification — 2026-10-28
- Current `main`, `Developer`, and `feat/codepilot-free-app` point to `fcc56c5f34e3283b21ca7b0eea4638d7e475bb83` as of the latest check on 2026-10-28 and compare as identical.
- CodePilot tests passed on current `main`; nested-tree audit, `.gitignore` validation, and guarded branch cleanup passed on the same commit. A CodePilot test run on the synchronized feature branch is still in progress at last check.
- The guarded cleanup workflow no longer has a duplicated special-case deletion block. It checks ancestry before removing any of the explicitly named redundant aliases.
- `docs/windows-repository-audit.ps1` is a read-only script intended to be run on the Windows machine. It inspects both repositories, remotes, branch tracking, submodules, dirty paths, and normalized file-level differences. The script's output has not been supplied, so local checkout state remains unverified.

## Completion status
Verified remotely: integration PR #8, tests on `main` and the synchronized CodePilot branch, `main`/`Developer`/CodePilot branch synchronization, nested-tree comparison, `.gitignore` checks, and guarded cleanup workflow. Local Windows synchronization remains unverified because GitHub cannot inspect the live working tree.

## Latest follow-up — 2026-10-28
The Windows audit script had duplicate output statements, which have been removed. The final synchronized remote commit is `fcc56c5f34e3283b21ca7b0eea4638d7e475bb83`; CI has been triggered for this latest script-only update. Check the [Actions dashboard](https://github.com/prayaggaikwad96/Full-Stack-Development/actions) for the newest run results.
