# Repository health audit — 2026-10-27

## Verified remote state
- Repository: `prayaggaikwad96/Full-Stack-Development`; default branch `main`.
- Current `main`, `Developer`, and `feat/codepilot-free-app` all point to `cb7bbe968825fcc1a39b92e14c3d6107812d33fe` as of the latest remote check on 2026-10-28; GitHub compare confirms both working branches are identical to `main`.
- CodePilot Free is integrated on `main` by [merged PR #8](https://github.com/prayaggaikwad96/Full-Stack-Development/pull/8), merge commit `b58350197c9d277c6b5389bb8a0ac1540e5842a4`. It includes the application, tests, MIT license, Windows launcher, and GitHub Actions workflow.
- CodePilot tests passed on Python 3.10 and 3.12 at commit `963bf05`: [main run 40566789588](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40566789588), [feature-branch run 40566914231](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40566914231). The latest audit-note-only commit is `cb7bbe9`.
- The nested-tree comparison and root gitignore validation passed on commit `963bf05`: [nested tree audit](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40566789686), [gitignore validation](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40566789602).
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
- Current `main`, `Developer`, and `feat/codepilot-free-app` point to `cb7bbe968825fcc1a39b92e14c3d6107812d33fe` as of the latest check on 2026-10-28 and compare as identical.
- CodePilot tests passed on current `main`; nested-tree audit, `.gitignore` validation, and guarded branch cleanup passed on the same commit. The matching feature-branch CodePilot test run is tracked above and should be checked for its final result.
- The guarded cleanup workflow no longer has a duplicated special-case deletion block. It checks ancestry before removing any of the explicitly named redundant aliases.
- `docs/windows-repository-audit.ps1` is a read-only script intended to be run on the Windows machine. It inspects both repositories, remotes, branch tracking, submodules, dirty paths, and normalized file-level differences. The script's output has not been supplied, so local checkout state remains unverified.

## Completion status
Verified remotely: integration PR #8, tests on `main` and the synchronized CodePilot branch, `main`/`Developer`/CodePilot branch synchronization, nested-tree comparison, `.gitignore` checks, and guarded cleanup workflow. Local Windows synchronization remains unverified because GitHub cannot inspect the live working tree.

## Latest follow-up — 2026-10-28
The Windows audit script had duplicate output statements, which have been removed. The current synchronization point before this documentation refresh was `cb7bbe968825fcc1a39b92e14c3d6107812d33fe`. All four checks passed on `963bf05`; the note itself is documentation-only. Check the [Actions dashboard](https://github.com/prayaggaikwad96/Full-Stack-Development/actions) for the newest run results.
