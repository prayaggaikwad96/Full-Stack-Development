# Repository health audit — 2026-10-27

## Current verified remote state
- Repository: `prayaggaikwad96/Full-Stack-Development`; default branch `main`.
- `main`, `Developer`, `github-sync`, and `archive/developer-before-sync-2026-10-27` currently point to commit `edb4ad2aaf9d154a3b5e78b80a85fc476a66c5a2`; `main` and `Developer` compare as identical.
- Latest root gitignore validation passed on this commit: [run 40550740609](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40550740609).
- CodePilot tests passed on `feat/codepilot-free-app` in [run 40544782665](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40544782665) for Python 3.10 and 3.12. Historical failures remain in earlier run history, but later tests passed.
- `feat/codepilot-free-app` has independent files and 36 commits ahead / 85 behind `main`; preserve it, do not force-sync or delete it.
- `backup/legacy-tree-before-cleanup-2026-10-27` remains at an older recovery point and is not an off-site backup.

## Exact nested-tree inventory
The recursive Git tree was compared at `71b7eef2e53c8008134053c1a0b05ac48a4ff6d4` between `Prayag Gaikwad/` and `Full-Stack-Development/Prayag Gaikwad/` (the inventory is still valid for the paths and hashes in that commit; latest commits only changed docs).

- Canonical entries: 546; nested entries: 549.
- Shared paths: 545; identical Git objects: 177.
- Different shared entries: 368 — 364 file blobs and 4 directory/tree hashes.
- Nested-only entries: 4 (two empty placeholder files plus their two parent directories).
- Canonical-only entry: one empty placeholder file.
- These exact path/SHA inventories are available at [comparison JSON](nested-tree-comparison-2026-10-27.json), [comparison CSV](nested-tree-comparison-2026-10-27.csv), and [differing blob pairs](nested-tree-differing-blobs-2026-10-27.json).
- Sampled file pairs match after normalizing CRLF/CR to LF; only a small sample has been checked this way. The full normalized comparison of all 364 differing blobs is not completed, so do not delete or overwrite the nested tree yet.

## Windows local repositories
Remote GitHub inspection cannot read the Windows disk. Actual status, remotes, checked-out commits, dirty worktrees, submodule state, and backup integrity of `C:\\Prayag Gaikwad` and `C:\\Prayag Gaikwad\\Full-Stack-Development` remain unverified until the read-only audit script is run and its output reviewed: [windows audit script](windows-repository-audit.ps1).

## Branch deletion
The connected GitHub toolset supports branch ref updates but not branch deletion. No branch was deleted. `github-sync` and `archive/developer-before-sync-2026-10-27` are aligned aliases of main, but check local checkouts/scripts before deleting them in GitHub's branches UI. Keep `main`, `Developer`, and `feat/codepilot-free-app`; retain the older backup until an independent backup is confirmed.

## Completion status
Remote branch synchronization and the latest main validation are verified. The full normalized content comparison, Windows local verification, and final branch deletion are not complete or claimed.
