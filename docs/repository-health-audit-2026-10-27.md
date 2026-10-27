# Repository health audit — 2026-10-27

## Current verified remote state

- Repository: `prayaggaikwad96/Full-Stack-Development`; default branch: `main`.
- `main`, `Developer`, `github-sync`, and `archive/developer-before-sync-2026-10-27` have been checked and are identical at `65e07ef614b70e6a17fa21cd32c4c87233eb5427`.
- Latest main validation passed: [run 40550067574](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40550067574).
- CodePilot tests passed on branch `feat/codepilot-free-app` on Python 3.10 and 3.12 in [run 40544782665](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40544782665). Older historical failures remain in the run history, but later runs passed.
- `feat/codepilot-free-app` is 36 commits ahead and 85 behind `main`, with separate application files; preserve it and do not force-sync or delete it.
- `backup/legacy-tree-before-cleanup-2026-10-27` remains a historical recovery reference at an older commit. It is not an independent off-site backup.

## Nested duplicate tree: exact recursive Git object audit

At commit `65e07ef614b70e6a17fa21cd32c4c87233eb5427`, a non-truncated recursive Git tree was retrieved and compared by relative path and Git object SHA between:

- Canonical: `Prayag Gaikwad/`
- Nested: `Full-Stack-Development/Prayag Gaikwad/`

Results:

- Canonical entries: 546
- Nested entries: 549
- Shared relative paths: 545
- Identical objects: 177
- Differing shared entries: 368, including 364 file/blob differences and 4 directory/tree hash differences (directory hash differences follow from changed children and are not an additional set of files).
- Nested-only entries: 4 (two placeholder files and their two parent directories for empty Advanced Projects and Intermediate Projects).
- Canonical-only entries: 1 empty placeholder file under `Prayag Gaikwad CSS/Projects/.gitkeep.txt`.

These are exact Git object identity results, not yet a normalized content diff. Text files with different line endings or whitespace may hash differently. Do not delete/overwrite the nested copy until blob contents for all 364 differing file paths are compared after line-ending normalization and any substantive difference is reviewed. The nested tree contains real learning materials.

## Windows repositories

The remote audit cannot observe the local disk. The status/remotes/branch tips/submodule state and dirty worktrees at `C:\\Prayag Gaikwad` and `C:\\Prayag Gaikwad\\Full-Stack-Development` remain unverified until the read-only script is executed locally and its output reviewed. The script is [docs/windows-repository-audit.ps1](https://github.com/prayaggaikwad96/Full-Stack-Development/blob/main/docs/windows-repository-audit.ps1).

## Branch cleanup

The available GitHub connector does not expose a delete-branch operation. The two now-aligned historical refs were not deleted. Keep `main`, `Developer`, and `feat/codepilot-free-app`; preserve `backup/legacy-tree-before-cleanup-2026-10-27` until the local/off-site backup and normalized file comparison are checked. `github-sync` and `archive/developer-before-sync-2026-10-27` are now redundant aliases of `main` and may be removed through GitHub's branches UI only after confirming no local scripts or checkouts depend on them.

## Completion status

Remote synchronization of the four identical refs and the current main validation are verified. CodePilot is preserved and its latest cited tests pass. The normalized content diff, Windows local repositories, and final branch deletion are not claimed complete because they require local data review or a branch-delete operation unavailable to this connector.
