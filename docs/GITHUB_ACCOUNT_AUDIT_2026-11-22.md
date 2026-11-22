# GitHub account engineering audit — 22 November 2026

## Scope and method

Authenticated account: `prayaggaikwad96`.

The connected account exposed seven public repositories at audit time:
- `Full-Stack-Development` (default: `main`)
- `Computer-Classes` (default: `main`)
- `virtual` (default: `main`)
- `rea` (default: `main`)
- `altair` (default: `master`)
- `git` (default: `master`)
- `prayaggaikwad96` (default: `main`)

This is a remote GitHub audit, not a local build or complete security assessment. The connector can inspect repository content, branches, pull requests, and exposed workflow/check data. It cannot establish local worktree cleanliness, restore-tested offline backups, all Dependabot/security alerts, production behavior, or every branch-protection/ruleset setting.

## Verified observations

### Full-Stack-Development

- The current default-branch check-runs endpoint exposed 24 check runs; all 24 were completed successfully on the inspected main head (CodeQL, Python/Node matrix, repository invariants, nested-tree comparison, and ignore-rule validation among them).
- PR #35 (`main` → `Developer`) remains open and draft. The latest recorded comparison reports 78 commits ahead and zero behind, 112 changed paths, 8,462 additions, and 118 deletions. Five deleted paths were checked on Developer and were empty placeholder blobs. These facts do not establish that the complete learning/project-content diff is accepted.
- The live branch API reports `main` unprotected and `Developer` protected. Detailed protection/ruleset data is not available through this integration. Do not merge PR #35 until path-by-path content review, local worktree checks, independent restorable backups, and effective main protection are independently verified.
- Preserve all primary, archive, safety, recovery, and synchronization branches.

### Computer-Classes

- The default-branch check-runs endpoint exposed two successful CodeQL checks.
- PR #15 adds CodeQL push coverage for `Developer`; PR #16 proposes a governance document describing desired Developer protection. PR #16 explicitly does not apply settings.
- The branch-protection PR must not be mistaken for active branch protection. Verify settings in GitHub repository administration.

### virtual (TanStack Virtual fork)

- The default-branch check-runs endpoint exposed successful CodeQL and zizmor runs; conditional release/autofix jobs were skipped.
- Existing focused remediation branches include anchor-clamping/scroll-cancellation and dependency/security changes. Branch names alone do not prove the change is correct or merged. Inspect each diff and exact-head upstream CI before proposing integration.
- Review current dependency alerts, lockfile state, and upstream compatibility through normal security/dependency tooling.

### rea (REA fork)

- No check runs were returned by the default-branch check-runs endpoint during this audit. This is not evidence of a clean build.
- Current README describes a reverse-engineering toolkit and notes a gated production CodeQL workflow controlled by repository variable `REA_CODEQL_ADVANCED`. Validate which CodeQL mode is active and ensure the setting matches GitHub's repository configuration.
- Numerous narrow correctness and resource-safety branches exist. Review each against the current upstream base, tests, and issue reproduction; avoid combining unrelated changes.

### altair (Altair GraphQL Client fork)

- No check runs were returned by the default-branch check-runs endpoint during this audit. This is not evidence of a clean build.
- Recent history includes workflow hardening and CodeQL modernization. README includes a stale maintenance badge marked 2025; refresh only after confirming the actual upstream maintenance/release state.
- A workflow path lookup for `.github/workflows/codeql.yml` returned 404, so the location/configuration of CodeQL must be discovered from the current tree rather than assumed.

### git (Git fork)

- No check runs were returned by the default-branch check-runs endpoint during this audit. This is not evidence of a clean build.
- Open PR #3 (`fix/ci-dirname-ubuntu-2026-11-17`) is a draft and must not merge: recorded CI run 44145914206 still fails on Ubuntu 26.04 with `/usr/bin/dirname: Already exists`; the proposed remove-and-recreate strategy also creates a failure window if symlink creation fails. Separate linux-sha256 provisioning failures (`udevadm` missing and `/etc/resolv.conf` busy) require independent investigation.
- A follow-up fix must be atomic/idempotent, handle regular/correct/unexpected symlink states, preserve a working dirname on failure, and pass the exact upstream CI matrix.
- Recent commits added Dependabot scheduling, SHA-pinned Actions dependencies, and CodeQL. Confirm exact-head checks rather than relying on merged commit messages.

### Profile repository

- No check runs were returned by the default-branch check-runs endpoint.
- The README describes selected work and technologies; verify featured project links and claims remain current as projects evolve.

## Cross-repository remediation priorities

1. Protect every primary branch with a GitHub ruleset/branch protection that requires pull requests, blocks force pushes and deletion, requires conversation resolution, and enforces only stable checks that actually run on each relevant PR.
2. Review open PRs individually. Never merge based only on the GitHub mergeable flag, branch name, or a check that ran on a different SHA.
3. Confirm branch-specific CI coverage for both primary and supported development branches.
4. Inspect dependency manifests and lockfiles; enable appropriate Dependabot ecosystems only where manifests exist. Review major-version upgrades manually.
5. Keep CodeQL languages aligned to actual source languages, with least-privilege workflow permissions and immutable action pins.
6. Add/maintain secret scanning and push protection where available; review alerts privately and rotate any exposed credentials rather than merely deleting files.
7. Add reproducible tests for behavioral fixes, regression cases, supported runtime matrices, and security boundaries.
8. Verify license, notices, provenance, upstream remote, and fork sync policy before redistributing upstream content.
9. On each local machine, inspect dirty/untracked files and create independent Git bundle backups; test restoration before any synchronization or history-changing operation.
10. Record exact commit SHAs, CI run URLs, and reviewer decisions for each accepted change.

## Limitations and non-claims

- This audit did not change branch-protection settings, repository secrets, releases, tags, or any protected/default branch.
- No PR was merged and no branch was force-pushed, reset, or deleted.
- No local build/test suite was executed in a local checkout.
- No assertion is made that every vulnerability, bug, dependency issue, or breakthrough has been discovered.
- Research or technical breakthroughs should be reported only when supported by upstream release notes, merged source changes, benchmark/test evidence, or peer-reviewed/public technical documentation. A normal refactor or workflow improvement is not automatically a breakthrough.

## Next review

Re-run the audit against fresh refs and exact workflow run SHAs. Update this report only when new evidence changes a finding or closes a remediation item.


## Follow-up verification — 22 November 2026, 12:40 IST

### PR #63 validation
The exact PR head `d6cd01ecfeee72f4f1eb99e4790c46933a30da7a` passed Repository consistency, all eight CodePilot Python/Node matrix jobs, and CodeQL. No independent review is recorded; PR #63 remains open for review.

### Primary-branch API snapshot
The branch endpoint reports the following coarse `protected` flags:
- `Full-Stack-Development/main`: false.
- `Computer-Classes/main`, `virtual/main`, `rea/main`, `altair/master`, `git/master`, and `prayaggaikwad96/main`: true.

The detailed protection endpoint returns HTTP 403 through this GitHub integration for the six protected branches. The rulesets endpoint returned an empty list for all seven repositories. Thus the effective review requirements, required checks, conversation resolution, bypass policy, and force-push/deletion restrictions remain unverified. Do not interpret a coarse protected flag as full governance compliance.

### New confirmed Dependabot configuration defect — Computer-Classes
The 16 November Dependabot run failed with `dependency_file_not_found`: `/action.yml or /.github/workflows/<anything>.yml not found`. The repository root inventory contains only `.github`, docs, and Markdown guidance; the only workflow is `.github/workflows/codeql.yml`. The GitHub Actions ecosystem was incorrectly scoped to `/`.

A focused config-only fix was opened as [Computer-Classes PR #17](https://github.com/prayaggaikwad96/Computer-Classes/pull/17): change the Dependabot directory to `/.github/workflows`. The PR changes one file (5 additions, 1 deletion), no source code, and its current CodeQL PR check is running. The actual Dependabot updater cycle must still confirm the fix after merge/scheduled execution; do not claim it is repaired until then.

### Workflow run evidence refresh
- Full-Stack-Development/main: latest visible PR checks and push runs for the current main head succeeded.
- Computer-Classes/main: CodeQL succeeded; prior Dependabot updater runs failed due to the wrong directory scope described above.
- virtual/main: CodeQL and zizmor succeeded on current main; Release and autofix jobs were skipped by conditions. An earlier CodeQL run on the immediately preceding SHA was cancelled, while the latest current-head CodeQL succeeded.
- REA and Altair: recent Dependabot jobs appear queued for long periods in the workflow-run API, so dependency update automation completion is not established.
- Git and profile repository: the recent default-branch workflow-run query returned no entries. This is not passing CI evidence.

### Safety and current disposition
No settings, secrets, default branches, tags, releases, or recovery refs were changed. PR #35 and Git PR #3 remain draft and must not be merged based on existing evidence. Local worktree/backup/restore checks remain an owner-side task.
