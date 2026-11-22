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


## Further remediation activity — 22 November 2026, afternoon

### Computer-Classes follow-ups
- PR #15 now changes both CodeQL triggers: pushes to `main` and `Developer`, and pull requests targeting either branch. Latest head `d960e665b6c25262d5c7085eb26602940c2332e6` has successful CodeQL analysis.
- PR #17 updates the GitHub Actions Dependabot ecosystem directory from `/` to `/.github/workflows`, the only real workflow directory in the repository. Latest head `09d9473f689c2946d3468f9f7666204b42794097` has successful CodeQL and configuration-validation checks. The next actual Dependabot update cycle is still required to prove that the updater now discovers and updates workflow actions.
- PR #16 remains a governance-document change only. It does not enable protection on `Developer`.

### TanStack Virtual / Marko anchor regression
- PR #25: [retry clamped prepend anchors after DOM commit](https://github.com/prayaggaikwad96/virtual/pull/25), current base `main`, latest head `6e0d079758efeee14f33c8188193fa2ad8f0a8bc`.
- The main branch's virtual-core retains a clamped anchor retry, but its Marko element and window wrappers did not schedule a retry after Marko commits the expanded sizer. The focused PR schedules one next-frame retry, cancels superseded frames and cancels on component destruction; it adds core tests for a clamped prepend, explicit-scroll cancellation and cancellation before update.
- The first preview build exposed a TypeScript visibility error because the wrapper called a private core method. This was corrected with a narrow internal type assertion; the core method remains private and no public API was added.
- On the corrected head, CodeQL, zizmor, provenance, package preview build and version preview succeeded. The main PR Test job was still in progress at this snapshot; do not merge until it finishes successfully.

### Security advisory accuracy — virtual dependencies
- Current `pnpm-lock.yaml` includes `glob@13.0.6`. GitHub-reviewed GHSA-3g3m-2fjr-6pw4 affects glob `>=9.0.0 <=14.0.1`; patched version is `14.0.2`. The advisory specifically documents continued filesystem traversal after an AbortSignal cancellation. <https://github.com/isaacs/node-glob/security/advisories/GHSA-3g3m-2fjr-6pw4>
- The transitive consumers in this lockfile include Marko tooling and npm-cli ecosystem packages. A forced major override to glob 14 can violate their `^13` ranges, so do not apply a lockfile-only major override without upgrading compatible parents and running the full test/build matrix. An existing candidate branch proposes glob 14 but has not regenerated the lockfile and is not a validated fix.
- Hono is currently locked at `4.13.19`, which is above the GHSA-5r4p-p66f-jhc7 fix `4.13.11`; that advisory is not a reason to roll back or further upgrade the current Hono entry. <https://github.com/honojs/hono/security/advisories/GHSA-5r4p-p66f-jhc7>
- Corrected a prior overbroad minimatch assessment: the current GitHub maintainer advisory GHSA-g3hv-75wg-m249 lists `10.2.6` as affected and `11.0.1` as patched; the main lockfile's `10.2.5` is not listed as affected by that specific advisory. GHSA-hqmv-qgp3-jx75 affects only `11.0.3` through `11.0.7`, patched at `11.0.8`; do not label 10.2.5 as affected by that distinct issue. <https://github.com/isaacs/minimatch/security/advisories/GHSA-g3hv-75wg-m249> <https://github.com/isaacs/minimatch/security/advisories/GHSA-hqmv-qgp3-jx75>

### Git fork CI
- PR #7: [atomic Ubuntu dirname replacement and container bootstrap](https://github.com/prayaggaikwad96/git/pull/7), latest patch head `68eaa64e81d103d91f1e4a679a2eebcdf5a3d4e4`. It is based on current `master`, modifies only `ci/install-dependencies.sh` and `.github/workflows/main.yml`, and has been exercised with a local filesystem-state/failure matrix.
- No GitHub Actions runs or check contexts were exposed for that head. A comment was added requesting repository Actions enablement/approval verification and exact-head CI. PR #3 remains as a recovery/history reference and is explicitly marked as superseded; do not merge either patch until PR #7 runs the full matrix successfully.

### Delayed Dependabot update jobs
- The REA root `minimatch` and advertised-schemas `pip` updater runs created on 18 November remain queued with no jobs listed. Several Altair daily npm update runs also show queued/no-job state. This indicates that the updater work is not verifiably completing; repository file inspection alone cannot establish a service-side cause. Track the Dependabot UI/logs and GitHub Actions status before asserting update automation is healthy.

### Current merge posture
- PR #63 audit document: the exact current head previously passed repository invariants, 8 Python/Node matrix combinations, and CodeQL; it remains open for independent review.
- PRs #15 and #17: exact-head CodeQL and configuration checks passed; keep open for review and confirm actual Developer branch protections / Dependabot update cycle.
- PR #25: security/build/preview checks passed on latest head; the main Test job was still running at this snapshot.
- PR #7: GitHub CI not running on latest head; do not merge.
- PR #35 remains draft; do not merge until content review, branch governance and two-PC backup/restore checks are complete.
- No settings, secrets, primary branch refs, tags, releases, or recovery refs were changed by this follow-up.


## Correction — Computer-Classes Dependabot diagnosis withdrawn (22 November 2026)

An earlier follow-up incorrectly claimed that `Computer-Classes/.github/dependabot.yml` was misconfigured because it used `directory: "/"`. That diagnosis is withdrawn.

GitHub's official Dependabot documentation requires the GitHub Actions ecosystem directory to be `/ ` (slash, no space); Dependabot then searches `.github/workflows` and a root `action.yml`. The failed updater run `43805270981` was executed against commit `0d83861c6e187f962e7189647e2b1c6a9db6e922`. The exact historical tree at that SHA had no `.github/workflows/` directory, so `dependency_file_not_found` was expected on that historical commit and does not establish a bad directory setting. The CodeQL workflow first appears in the tree by commit `a0ecfea2c63098e03a537551c9ed2063b79c9abe` and exists on current `main`.

The speculative fix was reverted to `directory: "/"`, and [Computer-Classes PR #17](https://github.com/prayaggaikwad96/Computer-Classes/pull/17) was closed with an explanation. Do not describe PR #17 as a real fix or the original updater failure as a current configuration defect. Verify a later scheduled updater run before concluding current Dependabot operation is healthy.

Official documentation: https://docs.github.com/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file and https://docs.github.com/code-security/dependabot/dependabot-version-updates/optimizing-the-creation-of-pull-requests-for-dependabot-version-updates.


## Further exact-head verification — 22 November 2026, 13:05 IST

### TanStack Virtual PR #25 — Marko #1267
The corrected PR head `65d63632c5a38e9958f83b5d9254f46d093833e4` now has a green exact-head check suite:
- CodeQL: success.
- GitHub Actions security analysis / zizmor: success.
- PR Test: success.
- Provenance: success.
- Package Preview and Version Preview: success.
- The Test job reports 124/124 Nx tasks successful and 0 failed; the E2E segment reports 82 passed, 1 skipped. The skip in the combined log is from the separate core `scroll-trace.test.ts` suite; the Marko chat-pretext E2E suite is built and executed in the same run.
- The previously skipped Marko #1267 test is now deterministic: it holds the delayed history prepend, clicks Latest, then releases the prepend and asserts that the end remains pinned. The core fix marks a clamped prepend anchor and the Marko element/window wrappers re-run `_willUpdate()` after the next DOM commit.
- PR #25 remains open for independent review. Green CI validates the proposed head but does not substitute for maintainer review or prove performance/behavior beyond the test coverage.

### Full-Stack-Development audit PR #63
Latest audit-document head `f9c430d887a1ea160d98da1ba884e780bf936e78` passed Repository consistency, all eight CodePilot Python/Node matrix jobs, and CodeQL. It remains open for review and has not been merged.

### Dependabot false-positive correction
The earlier Computer-Classes PR #17 has been closed after confirming that `directory: "/"` is the documented setting for the GitHub Actions ecosystem and that the 16-November failed updater commit had no `.github/workflows/` directory. The attempted config change was reverted; no current-main config bug is established. See the correction section above and the closed PR for the historical evidence.

### Current merge posture
- PR #25: all available checks green; independent review still pending.
- PR #63: all available checks green on its latest audit-document head; independent review pending.
- Computer-Classes PR #15: CodeQL passed after adding both push and pull_request branch coverage for Developer; review remains pending.
- Computer-Classes PR #16: documentation only; actual Developer branch protection must be applied separately in Settings.
- Git PR #7: still no Actions run/check context on its latest commit; exact-head validation is a hard merge blocker. PR #3 remains the superseded historical reference.
- FSD PR #35 remains draft due the 112-path content synchronization and unverified two-PC recovery gate.
- No PR has been merged in this remediation session. No default/protected branch, repository settings, secrets, releases, tags, or recovery refs have been modified.


## Additional CI maintenance and PR disposition — 22 November 2026

### Git fork — stale PR closed, replacement remains gated
- Git PR #3 has been closed as superseded; its source branch remains preserved for history/recovery. No branch was deleted.
- Git PR #7 is based on current `master`; a fresh comparison is `ahead 3 / behind 0`, with only `ci/install-dependencies.sh` and `.github/workflows/main.yml` changed. GitHub currently reports it mergeable, but its exact-head Actions runs/check contexts remain absent. The PR is not validated and must not merge until the full CI matrix runs on its latest SHA.

### TanStack Virtual — GitHub Actions runtime update
- The `virtual` PR workflow currently pins `nrwl/nx-set-shas@v4.4.0`, whose `action.yml` targets Node 20. The exact-head PR #25 log emitted a Node-20 deprecation warning because GitHub runners force this action to Node 24.
- The upstream action released v5.1.0 with `runs.using: node24`; the `main-branch-name` input remains available. A separate one-line PR #26 updates the SHA pin to the v5.1.0 commit and is awaiting exact-head workflow validation. Do not merge without verifying the full PR test pipeline.

### Final state of other proposed changes
- Computer-Classes PR #17 was closed after its diagnosis was disproven; `directory: "/"` remains the documented correct Actions ecosystem setting. No current Dependabot path bug is claimed.
- Computer-Classes PR #15 still adds CodeQL push and pull_request triggers for both primary/development branches; exact-head CodeQL succeeded.
- FSD PR #35 remains draft; no merge. PR #63 remains open for independent review; latest audit document checks passed.
- Virtual PR #25 is fully green on exact head; review pending. PR #26 is a separate runtime-migration change and is not yet validated.

No default branch or protected branch, settings, repository secrets, tags, releases, or local refs/backups were changed.


### TanStack Virtual PR #26 — Node 24 runtime upgrade validated
- PR #26 updates `nrwl/nx-set-shas` from v4.4.0 (Node 20 action runtime) to v5.1.0 (Node 24 runtime) by immutable commit SHA.
- The action's v5.1.0 metadata retains `main-branch-name`, `NX_BASE` and `NX_HEAD` semantics needed by the current PR workflow.
- Latest exact head `df263d232f1f8be304e35cc7016c92f13af7b707` passed Test, Preview, Version Preview, Provenance, CodeQL, and GitHub Actions security analysis.
- PR #26 remains open for independent review; not merged.
