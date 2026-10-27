# Repository health audit — 2026-10-27

## Verified remote state
- Repository: `prayaggaikwad96/Full-Stack-Development`; default branch `main`.
- `main` and `Developer` are identical at `964dc8aa182927174df33afbfa8e956808f8d010`.
- The redundant branches `github-sync` and `archive/developer-before-sync-2026-10-27` were deleted by the guarded cleanup workflow after Git ancestry checks confirmed both tips were reachable from `main`: [cleanup run 40551866492](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40551866492).
- Remaining remote branches: `main`, `Developer`, `feat/codepilot-free-app`, and `backup/legacy-tree-before-cleanup-2026-10-27`.
- Latest main workflows passed: [root gitignore validation](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40551866652) and [nested tree audit](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40551866493).
- CodePilot tests passed for Python 3.10 and 3.12 in [run 40544782665](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40544782665). Earlier failed runs remain in workflow history, while later runs passed.
- `feat/codepilot-free-app` contains unique app/test files and is 36 commits ahead / 85 behind `main`. Preserve it; do not force-sync or delete it.
- `backup/legacy-tree-before-cleanup-2026-10-27` remains an older recovery ref. It is not an off-site backup, so retain it until an independent backup is confirmed.

## Nested tree normalized comparison — completed
Workflow: [Audit nested project tree](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40551308262)

Compared `Prayag Gaikwad/` (canonical) with `Full-Stack-Development/Prayag Gaikwad/` (nested), normalizing CRLF and CR to LF for UTF-8 text and preserving all other characters; binary files were compared byte-for-byte.

- Canonical file count: 525
- Nested file count: 526
- Relative file paths compared (union): 527
- Identical files: 160
- Line-ending-only differences: 364
- Substantive text differences: 0
- Binary differences: 0
- Canonical-only: one empty `.gitkeep.txt` under `Prayag Gaikwad CSS/Projects/`
- Nested-only: two empty placeholders under `Advanced Projects/` and `Intermediate Projects/`

Download the [normalized comparison artifact](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40551308262/artifacts/12754478961). Exact path/SHA inventory is also tracked in [CSV](nested-tree-comparison-2026-10-27.csv), [JSON](nested-tree-comparison-2026-10-27.json), and [differing blob pairs](nested-tree-differing-blobs-2026-10-27.json).

The paired files themselves are equivalent after line-ending normalization. The nested root also has an older, distinct README and duplicate nested workflow file; these are outside the compared learning-directory contents. No learning files have been deleted. The nested root should only be removed after confirming local submodule/checkouts and backup requirements.

## Windows local repositories
GitHub cannot inspect live local working trees. Actual remotes, checked-out commits, dirty files, submodule state, and local backup integrity under `C:\\Prayag Gaikwad` and `C:\\Prayag Gaikwad\\Full-Stack-Development` remain unverified until the local read-only audit is run and its output reviewed: [Windows audit script](windows-repository-audit.ps1). It inspects both repos and writes a normalized per-file CSV under `%TEMP%`.

## Completion status
Remote branch cleanup, main/Developer synchronization, latest GitHub Actions validation, and the full normalized comparison of the duplicated learning trees are verified. The nested directory has not been deleted, and local Windows repository verification remains outstanding. Do not claim whole-machine synchronization until the local audit output is reviewed.
