# Repository health audit — 2026-10-27

## Current verified remote state
- Repository: `prayaggaikwad96/Full-Stack-Development`; default branch `main`.
- `main`, `Developer`, `github-sync`, and `archive/developer-before-sync-2026-10-27` are currently identical at `7a0b9e70225eadc6f2962af4c5bf8b6c1b20de66`.
- Latest `main` gitignore validation passed: [run 40551308631](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40551308631).
- New normalized tree workflow passed: [run 40551308262](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40551308262).
- CodePilot test workflow passed for Python 3.10 and 3.12 in [run 40544782665](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40544782665). Historical failures remain in old run history, but later runs passed.
- `feat/codepilot-free-app` has independent app/test files and is 36 commits ahead / 85 behind `main`; preserve it and do not force-sync it.
- `backup/legacy-tree-before-cleanup-2026-10-27` remains at an older recovery point and is not an off-site backup.

## Nested tree normalized comparison — completed by GitHub Actions
Workflow: [Audit nested project tree](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40551308262)

It compared the file contents of `Prayag Gaikwad/` and `Full-Stack-Development/Prayag Gaikwad/`, normalizing CRLF and CR to LF for UTF-8 text while preserving all other characters; binary files were compared byte-for-byte.

- Canonical file count: 525
- Nested file count: 526
- Union of relative file paths compared: 527
- Exact identical files: 160
- Line-ending-only differences: 364
- Substantive text differences: 0
- Binary differences: 0
- Canonical-only files: 1 empty `.gitkeep.txt` at `Prayag Gaikwad CSS/Projects/.gitkeep.txt`
- Nested-only files: 2 empty placeholder files under `Advanced Projects/.gitkeep.txt` and `Intermediate Projects/.gitkeep.txt`

Full normalized reports are available in the workflow artifact [nested-tree-normalized-comparison](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40551308262/artifacts/12754478961), and in the repository's exact path/SHA inventory: [CSV](nested-tree-comparison-2026-10-27.csv), [JSON](nested-tree-comparison-2026-10-27.json), and [differing blob pairs](nested-tree-differing-blobs-2026-10-27.json).

**Interpretation:** The 364 matching relative file pairs differ only by line endings; the automated comparison found no content differences in those shared files. Do not delete the nested tree as a cleanup shortcut. It has two extra empty placeholder files while the canonical tree has a different empty placeholder. Choose a canonical structure only after considering links, local submodule relationships, and backup needs.

## Windows local repositories
Remote GitHub cannot inspect the PC's live working trees. The remotes, checked-out commits, dirty files, submodule state, and independent backup integrity at `C:\\Prayag Gaikwad` and `C:\\Prayag Gaikwad\\Full-Stack-Development` remain unverified until the local read-only audit is run. Updated script: [docs/windows-repository-audit.ps1](windows-repository-audit.ps1). It prints both Git states and writes the normalized local file comparison to a CSV under `%TEMP%`.

## Branch deletion
The connected GitHub tools can inspect and fast-forward refs but do not expose branch deletion. No remote branch has been deleted. `github-sync` and `archive/developer-before-sync-2026-10-27` are redundant aliases of `main`, but check local branch checkouts/scripts before removing them from the [GitHub branches page](https://github.com/prayaggaikwad96/Full-Stack-Development/branches). Keep `main`, `Developer`, and the active `feat/codepilot-free-app` branch. Preserve `backup/legacy-tree-before-cleanup-2026-10-27` until an independent backup is confirmed.

## Completion status
Remote branch synchronization, latest main validation, CodePilot workflow success, and the normalized remote file comparison are verified. Local Windows repository state and branch deletion remain outstanding because they require local output and a branch-delete operation unavailable to this connector.
