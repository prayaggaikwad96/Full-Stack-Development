# Branch cleanup review — 2026-11-01

## Scope and safety
This review covers the current remote branch inventory and PR history. It does not inspect local clones, worktrees, local backup refs, or offline copies. Keep `main` and `Developer`. Do not delete remote refs if local branches/worktrees may depend on them until both Windows repository audits are reviewed.

## Primary branches
- `main`: current publishing branch.
- `Developer`: primary development branch. It remains divergent from `main`; latest checked comparison is 248 Developer-only commits and 40 main-only commits from shared merge base `db1f8569d21a8bb41baec229fae4326f2c65aa43`.
- No primary branch was modified by this cleanup review.

## Preserve
- `archive/codepilot-feature-history-before-sync-2026-10-27`: compare with main has no common ancestor. Preserve independent CodePilot history.
- `reconciliation/main-files-into-Developer-2026-10-29`: 246 commits ahead and 68 behind main; preserve until the migration candidate is reviewed against local content.
- `docs/remote-audit-2026-10-30`: contains audit documents and unique history; preserve.
- `docs/github-recommendations-2026-10-29`: PR #12 source contains the standalone repository engineering recommendations document. Although PR #14 copied a related document version, the main branch does not currently contain this file; preserve until an exact destination copy is verified and local references reviewed.
- `safety/backup-developer-2026-10-30`, `safety/backup-developer-latest-2026-10-30`, `safety/backup-main-2026-10-30`, `safety/backup-main-current-2026-10-30`, `safety/backup-main-latest-2026-10-30`, `safety/backup-main-pre-merge-candidate-2026-10-30`, `safety/backup-main-pre-pr13-2026-10-30`, `safety/backup-main-pre-reconcile-2026-10-30`, `safety/recovery-snapshot-developer-2026-10-31`, and `safety/recovery-snapshot-main-2026-10-31`: retain while branch reconciliation is incomplete. Some preserve distinct historical main/developer tips; not interchangeable.

## Cleanup candidates — not deleted
- `chore/github-recommendations-2026-10-28`: source branch of merged PR #11. GitHub compare reports no common ancestor with current main, so branch ancestry cannot be safely pruned based on containment. Retain until a full tree/commit archive and local dependency check are completed.
- `docs/github-profile-readme`: source of closed/superseded PR #9. Current main contains a later profile/readme result, but the branch has unrelated history/no common ancestor in the compare endpoint. Retain until local backup and tree review.
- `profile/readme-final`: source of merged PR #10. Main README is present, but the remote branch has unrelated history/no common ancestor in the compare endpoint. Retain until local backup and tree review.
- The above are possible eventual deletion candidates only after preserving their exact commit objects and verifying no local worktree/branch relies on them.

## Pull request records
Closed/merged/unmerged PRs #1–#14 are historical GitHub records and are not deletable through the available connector. PR #11, #10, #8, #7, #6, #3, #2, and #1 are merged. PR #14, #13, #12, #9, #5, and #4 are closed unmerged; they remain useful review/history records. PR #4 includes the original CodePilot feature lineage and should not be treated as meaningless.

## Actions performed
- Read-only branch/PR inventory and comparison.
- No branch was deleted.
- No PR record was deleted.
- No primary ref was reset, force-pushed, or merged.

## Next gates
1. Run `docs/windows-repository-audit.ps1` on both Windows PCs and inspect local branches, remotes, worktrees, untracked/dirty files, nested repo/submodule state, and offline backups.
2. Confirm the standalone engineering-recommendations document exists in an authoritative main-branch destination before considering deletion of its source branch.
3. Archive each cleanup candidate's exact commit SHA and inspect its unique tree/content.
4. Only then delete a branch that is both content-preserved and confirmed unused locally.
