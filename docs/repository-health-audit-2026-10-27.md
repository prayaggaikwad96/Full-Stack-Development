# Repository health audit — 2026-10-27

## Current remote state

- Repository: `prayaggaikwad96/Full-Stack-Development`; default branch `main`.
- `main`, `Developer`, `github-sync`, and `archive/developer-before-sync-2026-10-27` were compared and aligned to the same SHA: `6ce4d5390d9e13f78b28d77b36f02a77ea5c20a6`.
- Latest main validation passed on that SHA: [run 40550464016](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40550464016).
- CodePilot's latest cited workflow run passed on Python 3.10 and 3.12: [run 40544782665](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40544782665). Older failed runs still appear in historical workflow history; later runs passed.
- `feat/codepilot-free-app` contains separate application/test files and is 36 commits ahead, 85 behind `main`. Keep it; do not force-sync or delete it.
- `backup/legacy-tree-before-cleanup-2026-10-27` remains an older recovery reference and is not an independent/off-site backup.

## Nested duplicate tree: exact recursive Git object audit

At the compared main commit, a non-truncated recursive Git tree was compared using relative paths and Git object IDs:

- Canonical prefix: `Prayag Gaikwad/`
- Nested prefix: `Full-Stack-Development/Prayag Gaikwad/`
- Canonical entries: 546
- Nested entries: 549
- Shared paths: 545
- Identical Git objects: 177
- Different shared entries: 368 (364 blob/file entries and 4 tree/directory hashes)
- Nested-only entries: 4: two empty placeholder files and their parent directories for Advanced Projects and Intermediate Projects.
- Canonical-only entry: one empty placeholder under `Prayag Gaikwad CSS/Projects/.gitkeep.txt`.

Sample blob contents were fetched from both trees and compared. For `Prayag Gaikwad CSS/Learnings/1 Examples in Each Chapter.html`, the difference was CRLF vs LF line endings; the rendered HTML content matched. This confirms that at least some changed blob IDs are line-ending-only, but does not establish that all 364 files are equivalent.

The nested copy contains real learning files. Do not remove it until all differing blob pairs are normalized to LF, diffed, and substantive differences reviewed. No files have been deleted or overwritten as part of this audit.

## Windows local repositories

GitHub cannot inspect the Windows disk. The actual state of `C:\\Prayag Gaikwad` and `C:\\Prayag Gaikwad\\Full-Stack-Development` (remotes, checked-out commits, dirty worktrees, and any submodule state) remains unverified until the read-only script is run locally and the output inspected. Script: [docs/windows-repository-audit.ps1](https://github.com/prayaggaikwad96/Full-Stack-Development/blob/main/docs/windows-repository-audit.ps1).

## Branch cleanup

The connected GitHub tools expose ref updates but not branch deletion. Branch deletion has therefore not been performed. `github-sync` and `archive/developer-before-sync-2026-10-27` are currently redundant aliases of main, but verify local checkouts/scripts before manually deleting them in the GitHub branches UI. Keep `main`, `Developer`, and `feat/codepilot-free-app`; preserve the older backup ref until an independent backup is confirmed.

## Completion status

Remote synchronization and latest main validation are verified. A recursive path/object comparison is complete and a sample confirms a line-ending difference; the full normalized comparison of all 364 differing file blobs is not complete. Windows local repository verification and final branch deletion are not complete or claimed.
