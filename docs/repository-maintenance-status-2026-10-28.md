# Repository cleanup decision — 2026-10-28

## Safe cleanup findings
- `main` and `Developer` are synchronized at the same commit.
- No PRs are open.
- `chore/github-recommendations-2026-10-28` has no file paths absent from the current `main` tree, and its associated PR #11 was merged. It is obsolete as a working branch, but deletion is blocked by the connected GitHub integration's lack of a branch-ref deletion operation.
- `docs/github-profile-readme` and `profile/readme-final` contain earlier profile README commits that are superseded by the merged profile draft. Their histories diverge from `main`, so verify local refs/backups before deleting.
- Preserve `archive/codepilot-feature-history-before-sync-2026-10-27`: it contains unique CodePilot history.
- The connected GitHub integration cannot write branch protections/rulesets. Current state remains unprotected with no rulesets.
- `.github/workflows/repository-consistency.yml` initially failed because unittest could not import `app`; the command is fixed with `PYTHONPATH=projects/codepilot-free`. GitHub Actions run 40649060475 for commit `d15758cc2c1bd1f0e0dad3fd7c20d9de22644b57` completed successfully, including the corrected CodePilot test step.
- Subsequent commit `10498c190185637dbfe9db3fe5f489edc9b6c4b2` updated this decision note, and `Developer` was fast-forwarded to it. At time of writing, its newer workflow runs were still in progress and need rechecking.

## Remaining manual actions
1. Configure branch protection on `main` via repository Settings → Branches/Rulesets. Require pull requests, choose only checks with verified stable names, disallow force pushes, and restrict deletion.
2. Delete `chore/github-recommendations-2026-10-28`, `docs/github-profile-readme`, and `profile/readme-final` only after confirming local backups/ref state. The GitHub connector cannot perform this deletion in this session.
3. Verify the Windows checkout with `git status --short --branch`, `git fetch origin`, and compare local/remote refs before any destructive reset.
