# Repository health audit — 2026-10-27

## Live GitHub status — refreshed after subsequent branch movement

This audit was checked against live GitHub on October 27, 2026. It does not inspect the Windows working copy at `C:\Prayag Gaikwad`; local changes, untracked files, index state, and local branches remain unverified.

- Repository: `prayaggaikw96/Full-Stack-Development`
- Default branch: `main`
- At the latest comparison, `main` and `Developer` are identical at `72e7ab5cf8ddaf6fe48ab43def40a4422ddabeec`.
- `github-sync` and `archive/developer-before-sync-2026-10-27` are one commit behind `main`. They have no unique commits according to the compare endpoint, but they no longer point at the current `main` tip.
- `backup/legacy-tree-before-cleanup-2026-10-27` is two commits behind `main`, retaining an earlier history/tree state. Do not move or delete this ref until its backup purpose has been confirmed.
- `feat/codepilot-free-app` is intentionally retained. Compared with `main`, it has 34 commits only on that branch and 74 commits only on `main`. It includes a separate CodePilot project, test suite, and workflow. Keep it unless that work is intentionally retired or preserved elsewhere.
- No open pull requests were found during the latest check.
- GitHub reports `main` and `Developer` as unprotected.
- The most recent successful root-gitignore workflow found is run [40542403116](https://github.com/prayaggaikw96/Full-Stack-Development/actions/runs/40542403116), at earlier commit `db5888b235cc3ea1619d2439549e1dc178834041`. No status checks are currently recorded for the latest `main` commit; current-commit validation is not confirmed.

## Duplicate source trees

The root `Prayag Gaikwad/` tree is the documented canonical location. The nested folder remains preserved in the live tree for now. The earlier tree comparison recorded:

- Canonical tree: 525 files.
- Nested legacy tree at `Full-Stack-Development/Prayag Gaikwad/`: 526 files.
- Shared paths: 524.
- Identical Git blob IDs among shared paths: 160.
- Shared paths with different blob IDs: 364.
- Legacy-only files: two empty `.gitkeep.txt` placeholders.
- Canonical-only file: one empty `.gitkeep.txt` placeholder.

One sampled HTML pair became identical after normalizing CRLF to LF, suggesting line endings explain at least some differences. All 364 differing pairs have not been compared after normalization. Do not delete the nested folder or overwrite either tree until a complete comparison and verified local backup are available.

## Local PowerShell audit status

The provided PowerShell script is designed to back up both working directories, inspect their status and origin URLs, and fetch remote refs only if both working trees are clean and repository identities match. The user has pasted the script but has not provided its execution output. Therefore it is not established whether the backup was created, either repository passed the clean-tree checks, or the fetch completed. The local `git branch` output alone only establishes that local branch names exist; it does not establish their commit tips, working-tree cleanliness, upstream status, or whether the shown parent and child directories are independent working trees.

## Safe next steps

1. Run the audit script and share its complete output, particularly the backup path, both `git status --short --branch` results, origin URLs, branch listings, and fetch results. Redact personal tokens if any appear.
2. Normalize and compare all 364 shared files before deciding whether the nested copy can be removed.
3. Confirm the purpose and recoverability of the backup branch before changing it.
4. Consider enabling branch protection for `main` and `Developer` and verifying a workflow run against the latest commit.
5. Keep `main` and `Developer` aligned. Retain `feat/codepilot-free-app` while its unique work remains useful.

## Final assessment

Remote `main` and `Developer` currently match, but the full project is not verified as completely synchronized. The historical refs are behind, current-commit CI is unconfirmed, the branches are unprotected, the 364 differing file pairs are unresolved, and the Windows working copy has not been audited from its execution output. No local folder or historical branch has been deleted by this audit.
