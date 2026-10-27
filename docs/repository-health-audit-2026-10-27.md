# Repository health audit — 2026-10-27

## Verified remote state

- Repository: `prayaggaikwad96/Full-Stack-Development`
- Default branch: `main`
- `main` and `Developer` are identical at commit `8a96cb8d00fadf40dabebc330167386b42c8c42a`.
- `github-sync` and `archive/developer-before-sync-2026-10-27` still point to the previously aligned commit `0428e0661a8ed6513c51fc47ce2f51ec1a2359da`; they are ancestors of main, not ahead of it. Branch-deletion operations are not exposed by the current connector, so they have been left intact rather than misrepresented as deleted.
- `backup/legacy-tree-before-cleanup-2026-10-27` preserves the prior main commit `895cfd749c5851c8de9d2a655106d423e305aed7` before the most recent README/audit edits. It is a Git ref, not an independent off-site backup.
- `feat/codepilot-free-app` remains separate because it has unique CodePilot files and commits; do not delete it until its code is deliberately integrated or separately preserved.
- No open pull requests were found.

## Duplicate source trees

The canonical source directory is `Prayag Gaikwad/`. The nested path `Full-Stack-Development/Prayag Gaikwad/` is retained as a legacy copy.

- Canonical files: 525.
- Nested legacy files: 526.
- Shared paths: 524.
- Same blob IDs: 160.
- Different blob IDs: 364.
- Nested-only: two empty `.gitkeep.txt` placeholders under Advanced Projects and Intermediate Projects.
- Canonical-only: one empty `.gitkeep.txt` placeholder under Projects.

Several inspected HTML files become text-identical after normalizing CRLF/LF line endings. The connector's per-turn call limit prevented normalizing all 364 differing files, so the remaining differences are **not certified** as line-ending-only. No bulk overwrite or deletion of either source tree was performed.

## Validation

The root `.gitignore` covers common Python cache/virtual environment files, Node/build outputs, logs, editor/OS artifacts, and environment secrets while allowing `.env.example` and `.env.sample`.

The `.github/workflows/gitignore-check.yml` workflow now triggers for relevant pushes to `main`, pull requests targeting `main`, and manual dispatch. A previous run succeeded on commit `db5888b235cc3ea1619d2439549e1dc178834041`; that run predates the latest README/audit-only commits. A fresh run against the final main commit should be confirmed.

## Local Windows working copy

The local folder `C:\Prayag Gaikwad` and any nested worktree have not been inspected from this GitHub connection. Local index/staging state, untracked files, branch divergence, local edits, and configured remotes remain unverified.

Before destructive local synchronization, run the supplied read-only script `audit-local-repos.ps1` and review `git status --short --branch` for both repositories. Then back up the worktree and a Git bundle, run the supplied `reconcile-legacy-tree.ps1` to classify every paired file after newline normalization, and only then decide whether the nested copy can be removed. The scripts do not modify source files.

## Remaining completion criteria

1. Run a complete normalized compare on the local copy and review every true content mismatch.
2. Verify the local repository paths/remotes and preserve any uncommitted or unique commits before aligning local branches to remote `main`.
3. Re-run GitHub Actions on the latest `main` commit.
4. If desired, delete the two redundant refs via GitHub's branch UI after confirming the local copies no longer depend on them.

This audit describes what is actually verified and does not claim the whole repository or the local PC is fully synchronized while those checks remain outstanding.
