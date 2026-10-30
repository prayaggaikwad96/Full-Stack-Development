# GitHub account and repository audit — 2026-10-30

## Scope and method

This report records a remote-only audit of the six public repositories returned by the connected GitHub account for `prayaggaikwad96`. Repository metadata, default branches, selected branch heads, recent pull requests, branch comparisons, and GitHub Actions runs were inspected through the GitHub connection. This is not a full account history export and does not inspect the user's local Windows filesystems.

## Account inventory

| Repository | Default branch | Remote synchronization finding |
| --- | --- | --- |
| Full-Stack-Development | `main` | `main` and `Developer` diverged at the latest compare |
| Computer-Classes | `main` | `main` and `Developer` identical |
| virtual | `main` | Fork default branch matches current TanStack upstream `main` |
| rea | `main` | Fork default branch includes current upstream `main` as merge parent |
| altair | `master` | Fork default branch matches current upstream `master` |
| git | `master` | Default branch inspected; no PRs found in the recent inventory |

All six repositories are public, unarchived, and report administrator permissions for the connected account.

## Freshly verified results — 2026-10-30

### Full-Stack-Development

- Latest `main` = `56f33b6128e0c4531782dbbcf5e5bd1bef078964`.
- Latest `Developer` = `33eb13cf83db41825e3184d4bb4314d0a4750630`.
- Shared merge base = `db1f8569d21a8bb41baec229fae4326f2c65aa43`.
- GitHub compare reports `diverged`: 30 commits ahead on `Developer` relative to `main`, and 248 commits behind (30 main-only, 248 Developer-only).
- Both primary refs report `protected: false`; observed branch-protection state is disabled. Rulesets and required branch controls have not been configured through this integration.
- PR #13 remains open/draft and is not safe to merge: it uses a stale base SHA and the full histories have not been reviewed or reconciled. Its one-file PR diff is not a representation of the full commit-graph divergence.
- PR #14 remains open/draft as the audit documentation review.
- Exact-head Actions runs on current `main` SHA `56f33b6...`: root gitignore validation, nested project-tree audit, repository-consistency audit, and CodeQL all completed successfully.
- Exact-head Actions runs on `Developer` SHA `33eb13c...`: CodePilot test matrix, repository-consistency audit, and CodeQL all completed successfully.
- The latest Actions evidence supports passing remote checks on those exact heads; it does not replace full diff/commit review or local Windows verification.
- Preserve primary refs, archive and recovery branches until local backups and unique commits are independently verified.

### Computer-Classes

- `main` and `Developer` both point to `e53a39c85f7b3395f793c8cea61dd0955974fbcf`.
- GitHub compare reports `identical`, zero ahead/behind, and no changed files.
- Both branch metadata records report unprotected refs. No open PRs were returned in the reviewed inventory.
- Local checkout cleanliness and security-alert settings remain unverified.

### REA fork

- Fork `main` = `dcb7bc72b2bc49898957c33a452bc0b98d0f2f1a`.
- Current upstream `morluto/rea` `main` = `cd878ad57d3e27e835d0db533c9603b24ae8607a`.
- Fork `main` is a merge commit whose parents are previous fork head `602468df998508a5a748036cce1e2becc6a51d15` and current upstream `cd878ad...`.
- Direct comparison shows fork `main` contains current upstream `main`, with five fork commits ahead; the five-commit list includes the four-document history and merge commit. The only net tree difference against the upstream parent in that comparison is the added `docs/fork-sync-audit-2026-10-28.md`.
- The open draft PR #13 is now stale: it targets old fork base `602468d...` and candidate `25859d0...`. Do not merge it over the already-synchronized default branch.
- Previously open staging PRs #1–#10 and #11–#12 were not reopened. Closed PR history and topic branches remain preserved pending branch-by-branch unique-work review.
- Upstream PR status and CI for other topic branches must be checked independently. No claim that all staged fixes were merged or accepted upstream is made.

### TanStack Virtual fork

- Fork `prayaggaikwad96/virtual` `main` and current upstream `TanStack/virtual` `main` both point to `51b06cd5e078a289fe1cbf25a8d2e647aa98bfff`.
- The default branches therefore match exactly at this snapshot.
- Upstream PR #1321 remains open/draft and reports non-mergeable. Its head is 1 commit ahead and 4 behind current upstream per its recorded comparison; focused typecheck, anchor-end tests, scroll-trace snapshots, and Marko Playwright E2E were still outstanding in the PR description.
- Fork topic branches remain preserved; do not call the feature contribution complete until refreshed and validated.

### Altair fork

- Fork `master` = `2deae0675ebf170e0bc8eac743de609a1c7dd07d`, matching current upstream `altair-graphql/altair` `master` at the same SHA.
- Upstream PR #3341 remains open and is the source of truth for the theme-aware Import from cURL textarea change; it reports one commit ahead of its base and its author-described checks passed, but it awaits upstream maintainer disposition.
- Fork PRs #1 and #2 are closed duplicate proposals. Preserve the corresponding branch/history; no reason to merge the fork duplicates.
- Earlier inspected workflow failures remain separate outstanding investigation items: Scorecard container-image access, Docker Hub publishing authentication, and Linux Electron packaging. A green CodeQL run does not close those failures.

### git repository

- Default branch `master` head inspected at `b9e5cff1803ab24582201ef059516eb16014b9d9`.
- No open PRs were returned in the reviewed inventory.
- The current scan did not establish comprehensive CI, dependency, or security-alert health.

## Work performed

- Confirmed authenticated account and six owned public repositories.
- Inspected live repository metadata, default branches, selected remote refs, recent PR inventory, and exact branch comparisons for the principal repositories.
- Verified latest Full-Stack-Development CI results on the current exact `main` and `Developer` heads.
- Verified exact default-branch synchronization for Computer-Classes, Virtual fork, and Altair fork.
- Verified REA fork `main` is a merge of current upstream `main`; identified old draft PR #13 as stale rather than attempting to merge it.
- Prior audit comments on Full-Stack-Development #13 and REA #13 record the safety gates.
- Did not merge an unverified PR, delete branches, force-update refs, rewrite primary history, or modify application code.

## Outstanding — do not describe as completed

1. Run `docs/windows-repository-audit.ps1` on the actual Windows checkout and inspect both local worktrees, dirty/untracked files, remotes, worktrees, local-only commits, nested repositories/submodules, and offline backups.
2. Resolve Full-Stack-Development `main` / `Developer` divergence only after full commit/tree review and local backup verification. Do not merge PR #13 as currently configured.
3. Close or replace stale REA fork PR #13 only after deciding whether to retain a history-only audit record; it is not a current synchronization candidate.
4. Refresh and test Virtual PR #1321 against current upstream before requesting review.
5. Monitor upstream Altair PR #3341 and separately diagnose the previously observed Scorecard, Docker publishing, and Linux Electron workflow failures.
6. Review all branches in REA, Altair, Virtual, and Full-Stack-Development for unique work before any deletion. Closed PRs do not prove their source branches are disposable.
7. Configure appropriate default-branch protection/rulesets, required checks, security features, secret scanning/push protection, and Dependabot settings in GitHub repository Settings. Current unprotected-ref evidence shows this is not complete.
8. Inspect workflow, dependency, vulnerability, release, and security-alert state for Computer-Classes and git before making an account-wide quality claim.
9. Validate local clones and any nested repository/submodule state; GitHub remote refs cannot prove local disk synchronization.

## Status

Remote inventory and selected exact-head comparisons/checks are updated. Three fork/default branches are verified to match upstream or include upstream history; Computer-Classes primary refs are identical. Full-Stack-Development remains divergent; Virtual's feature contribution remains unvalidated; Altair awaits upstream PR review and has other recorded workflow failures. Branch protection/security hardening, complete dependency remediation, full PR and topic-branch review, and local Windows synchronization are **not complete**. No claim of perfect or zero-error state is made.
