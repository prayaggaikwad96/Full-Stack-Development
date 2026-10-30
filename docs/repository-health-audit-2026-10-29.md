# Repository health and branch synchronization audit — 2026-10-30

## Current primary branch state — 2026-10-30 (refreshed)
- Default/published branch: `main`.
- `main` at time of latest check: `bf114fbfc80460e9ae80a143e6d4a5fda995131a` (this audit refresh commit).
- `Developer`: `33eb13cf83db41825e3184d4bb4314d0a4750630`.
- Shared merge base: `db1f8569d21a8bb41baec229fae4326f2c65aa43`.
- Live compare `main...Developer`: status `diverged`; Developer is 248 commits ahead and main is 27 commits ahead (latest compare after this document refresh).
- Main-side diff relative to Developer includes three paths: `.github/workflows/repository-consistency.yml`, `README.md`, and this audit document. Developer-side changes the workflow file.
- The branches are not synchronized. Do not force-push, reset, or merge until the complete history and tree changes are reviewed.

## Exact-head CI evidence — 2026-10-30
- Main at `66173f2547d600baa62d0650f238d70d554585b9`: repository invariants, nested-tree comparison, ignore validation, and CodeQL all passed.
- Developer `33eb13cf83db41825e3184d4bb4314d0a4750630`: CodeQL, repository invariants, and all eight CodePilot test-matrix combinations (Python 3.12–3.15 and Node.js 22/24) passed.
- The new main commit created by this refresh requires its own CI run; do not infer checks passed for a newer SHA.


## Scope and confidence

This is a remote-only GitHub audit performed on 2026-10-30. It checks public repository metadata, remote refs and comparisons, pull-request metadata, and recent GitHub Actions runs. It does not inspect the owner's Windows working tree, local-only commits, local backup copies, nested repository state, or all account security-alert settings.

Treat this document as a dated snapshot. Ahead/behind counts and check-run states change when branches are updated. Always rerun the compare and inspect the exact head SHA before a ref mutation.

## Latest verified remote state — 2026-10-30
- Default/published branch: `main`
- `main`: `66173f2547d600baa62d0650f238d70d554585b9`
- `Developer`: `33eb13cf83db41825e3184d4bb4314d0a4750630`
- Shared merge base: `db1f8569d21a8bb41baec229fae4326f2c65aa43`
- Live comparison `main...Developer`: status `diverged`; Developer is 248 commits ahead and main is 26 commits ahead.
- Comparison changed-tree summary: Developer relative to main changes `.github/workflows/repository-consistency.yml` (10 additions, 9 deletions); main relative to Developer has three paths differing (`.github/workflows/repository-consistency.yml`, `README.md`, and `docs/repository-health-audit-2026-10-29.md`). Recheck current refs before any merge because counts and diffs can change.

## CI evidence on exact branch heads
- Developer head `33eb13cf83db41825e3184d4bb4314d0a4750630`: repository consistency audit passed (run 41039119858), CodePilot test matrix passed (run 41039119948; all eight Python 3.12–3.15 / Node.js 22 and 24 combinations), and CodeQL passed (run 41039119885).
- Main head `66173f2547d600baa62d0650f238d70d554585b9`: repository consistency audit, nested project tree audit, root gitignore validation, and CodeQL all passed (run set 41038908042 / 41038908078 / 41038908151 / 41038908331).
- These CI results do not prove local Windows working-tree state or guarantee all historical branches are redundant.

## Current reconciliation gates
- Keep PR #13 draft. Do not merge it yet. The remote branches are substantially divergent (248 commits each way when comparing opposite base directions: main...Developer = 248 ahead, 26 behind). Review all divergent commits and the complete resulting tree, not only the PR changed-file summary.
- Keep PR #12 draft until its exact head checks and review are complete.
- Run `docs/windows-repository-audit.ps1` on the actual Windows checkout; verify dirty/untracked files, remotes, worktrees, local-only commits, nested repositories/submodules, and offline backups.
- Preserve primary branches and safety refs. No force-push, reset, or deletion is justified by the currently available evidence.
- Branch protection and owner-side security settings remain unverified; integration lacks required administration read/write scope.

## Remote recovery snapshots

The following two safety refs were checked against the current primary heads after the snapshot update:

- `safety/backup-main-latest-2026-10-30` matches `main` exactly at `34d203868e609401f1a454203bfefd3f46bb1ac3`.
- `safety/backup-developer-2026-10-30` matches `Developer` exactly at `204748099731c3aeb04963e6d8957dcd569daf62`.

These are remote Git refs, not a substitute for a local/offline clone backup. Keep both safety refs until reconciliation is complete and independently verified.

## Remote branches

The remote branch inventory currently contains eleven refs:

- `main`
- `Developer`
- `archive/codepilot-feature-history-before-sync-2026-10-27`
- `chore/github-recommendations-2026-10-28`
- `docs/github-profile-readme`
- `docs/github-recommendations-2026-10-29`
- `profile/readme-final`
- `reconciliation/main-files-into-Developer-2026-10-29`
- `safety/backup-developer-2026-10-30`
- `safety/backup-main-2026-10-30`
- `safety/backup-main-latest-2026-10-30`

No historical or safety branch was deleted in this audit.

### Branch preservation decisions

- Preserve `archive/codepilot-feature-history-before-sync-2026-10-27`. Comparison against current `Developer` shows it is diverged and has 36 commits not reachable from `Developer`; its compared file delta includes the CodePilot app, license, README, launcher, frontend assets, tests, and workflow.
- Preserve `reconciliation/main-files-into-Developer-2026-10-29`. It points to a separate merge/reconciliation commit and is not identical to `Developer`.
- Preserve `chore/github-recommendations-2026-10-28`, `docs/github-profile-readme`, and `profile/readme-final` until their unique contents are reviewed or independently backed up. The profile branches have no common ancestor with current `main` in the direct compare, so a simple ancestry test cannot prove redundancy.
- Preserve `docs/github-recommendations-2026-10-29` while PR #12 remains open.
- The three `safety/backup-*` refs are deliberate recovery snapshots, not cleanup candidates.

## Pull request inventory

- PR #12: open draft documentation/engineering checklist; keep draft pending full PR-head checks and review.
- PR #11: merged security, CI, contribution, and audit changes.
- PR #10: merged curated profile README.
- PR #9: closed unmerged and superseded by #10; retain history until its source branch is independently preserved.
- PR #8: merged CodePilot integration into `main`.
- PR #7: merged archive/snapshot contribution; do not confuse this PR merge with permission to delete the separate archive branch.
- PR #6: merged root `.gitignore` and validation workflow.
- PR #5: closed unmerged duplicate superseded by #6.
- PR #4: closed unmerged original CodePilot feature PR. Its source branch has separate historical ancestry and should be preserved until its commits are accounted for.
- PRs #1–#3: merged historical changes.

Only PR #12 is open in the reviewed list. Closed PRs #5 and #9 are historical duplicates already superseded by merged PRs #6 and #10 respectively. Do not delete branch refs solely because their PR is closed.

## GitHub Actions evidence

At audited `main` head `34d203868e609401f1a454203bfefd3f46bb1ac3`:

- Root `.gitignore` validation run #41038619889 completed successfully on this exact SHA.
- Other workflows, including CodeQL and the nested-tree audit, must be checked by matching their run's `head_sha` to this exact main SHA before being reported as passed. Older successful runs are not evidence for this newer SHA.
- The CodePilot test matrix is configured for Python 3.12–3.15 and Node.js 22/24; this configuration statement is not a claim that every matrix combination ran successfully on this audited main head.
- No Actions run sample was returned for branch `Developer`; do not infer that Developer has passing CI from main's runs.

## Repository protection and security settings

- Branch metadata reports `protected: false` for both `main` and `Developer`.
- The repository rulesets endpoint returns an empty list.
- The connected GitHub integration does not provide the administration permission needed to read or configure branch-protection settings directly. Confirm them in GitHub Settings.
- Secret scanning, push protection, Dependabot alerts/security updates, vulnerability reporting configuration, and the full alert inventory were not verified.
- Commit signature checks observed on sampled commits report unsigned; this is a hygiene observation, not evidence of compromise.

## Safe reconciliation plan

1. Run `docs/windows-repository-audit.ps1` on the actual Windows checkout.
2. Confirm clean/dirty/untracked state, remotes, worktrees, local-only commits, `.gitmodules`, nested repositories/submodules, and offline backups.
3. Preserve both exact primary heads and all recovery refs.
4. Review the complete 247 Developer-only and 23 main-only commit sets from the shared merge base, including full diffs, file/tree changes, tests, dependencies, generated files, and CodePilot history.
5. Create a candidate branch from the selected integration base; do not rewrite `main` or `Developer` as a shortcut.
6. Run all applicable CI on the exact candidate SHA and inspect the complete diff.
7. Merge only through a reviewed PR after all unique work is accounted for.
8. Compare the resulting refs again; call them synchronized only when the intended relationship is proven by Git.

## Conclusion

The remote repository has verified recovery refs for both primary heads and a shared merge base between `main` and `Developer`. The branches remain diverged (247 commits on Developer-only side; 23 on main-only side). The repository is not yet fully synchronized or fully hardened. Local Windows state, full candidate validation, branch protection, and owner-side security settings remain outstanding. No primary ref was reset or force-pushed, no historical branch was deleted, and PR #12 was not merged.
