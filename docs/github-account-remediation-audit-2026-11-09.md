# GitHub account and repository remediation audit — 2026-11-09

## Account scope
Authenticated account: `prayaggaikwad96`.
Owned repositories returned by the connected GitHub account: seven.
Default branches:
- `Full-Stack-Development`: `main`
- `Computer-Classes`: `main`
- `virtual`: `main`
- `rea`: `main`
- `altair`: `master`
- `git`: `master`
- `prayaggaikwad96`: `main`

## Verification summary
- All seven repository metadata records were retrieved and account owner/admin permissions were reported.
- Default branch commit SHAs were confirmed.
- Live branch search was performed for each repository. Some results were paginated; no branches were deleted.
- Open PRs were identified in Full-Stack-Development (#33–#36, including #36 audit and #35 sync proposal), Computer-Classes (#6), and altair (#3).
- No PR was merged or closed during this audit.

## Critical finding: Full-Stack-Development
Default branch `main`: `42b32920dd18a2fadee8f9ec3f4660b775415c15`.
`Developer`: `50702be32d21c0216a45a2647cd6ebca100a9dda`.
GitHub compare reports `main` is 15 commits ahead and `Developer` is 2 commits ahead of their common merge base `35ddeabd4303a9a7a2eaf092d0203540f656d450`. They are diverged, not synchronized.
Existing PR #35 is a draft sync proposal from main to Developer. Its diff contains 549 changed files, 1,223 additions and 27,851 deletions. It must not be merged in current form.
PR #33 is a draft preservation proposal; its changed-file and provenance inventory has outstanding same-path conflicts and content verification. It must not be merged until the path/hash audit and local backup gate pass.
PR #34 and #36 are documentation/audit work; #34 branch inventory needs pagination refresh.
The live branch list currently includes 21 visible branches on the first list page; results indicate pagination. Recovery/archive refs are intentionally preserved.

GitHub Actions check-runs on current `main` included successful recent results for repository invariants and CodeQL, and prior successful matrix checks. This is point-in-time evidence, not proof that every draft PR head is currently green.

## Critical finding: virtual — Dependabot
The current default-branch check-runs include five failed Dependabot security-update jobs on SHA `ce84d96475d7552ec6af70cab14656a7f31fa72d`.
Inspected run logs show a `minimatch` security update cannot be resolved by the current dependency constraints: latest resolvable version `3.0.8`, earliest fixed version `11.0.1`. The root manifest specifies pnpm 11.9.0; the lockfile contains a transitive `minimatch@3.0.8` dependency (e.g. via `@microsoft/api-extractor@7.47.7`). This requires dependency-tree compatibility analysis, updating the introducing package/toolchain if feasible, then regenerating the lockfile and testing. No blind lockfile edit was made.

## Other repositories
- `Computer-Classes`: open draft PR #6 proposes weekly GitHub Actions Dependabot updates. Its diff is a seven-line Actions-only Dependabot config. Default branch current SHA `d87aa3ef21fd883f8f747e8e7983725c29edeafb`; check-runs API returned none.
- `altair`: open draft PR #3 changes four CI workflow files (46 additions, 21 deletions). It is not validated: its PR description explicitly lists missing PR-head CI for non-publishing and publishing paths. Do not merge until fresh CI and maintainer review. Current `master` SHA `c96f9dd2dfe680dc553262ef65cc6b513d701c3c`; available CodeQL checks succeeded.
- `virtual`: current main SHA `ce84d96475d7552ec6af70cab14656a7f31fa72d`.
- `rea`: current main SHA `938312834afe8aa32eb8d144e240f1675d68b621`.
- `git`: current master SHA `667f881bd14e8594009867c7ea415b9a046bb606`.
- `prayaggaikwad96`: current main SHA `7737fe2bb570ae200fa331342238a50dc3ac0fd5`.
For Computer-Classes, virtual, rea, git and profile repo, the queried commit-check runs endpoint returned no check runs for the current default-branch commit; this is not equivalent to a comprehensive workflow/security audit.

## Access limitations and unverified controls
The connected integration returned HTTP 403 for branch-protection detail reads on Full-Stack-Development. However, a subsequent live GET of the default-branch objects reports `protected: true` for all seven repositories. Thus all seven default branches are marked protected; the exact protection policy (required checks/reviews, admin enforcement, force-push/deletion rules, and ruleset/classic details) remains unverified. Secret-scanning, push-protection, vulnerability alerts, Actions secrets, and automatic branch-deletion settings were not fully verified across all repositories. The connector does not expose administrative write actions for branch protection/rulesets or repository security settings.
Local Windows worktrees on two PCs cannot be inspected through this GitHub connection. No claim is made that local files, untracked work, or local-only commits are synchronized or backed up.

## Actions taken in this audit
- Created a dedicated audit branch from the observed `main` tip.
- No repository source files changed.
- No branch refs moved.
- No branches deleted.
- No PR merged or closed.
- No secrets, releases, deploy keys, or environment settings modified.

## Safe next steps
1. On both Windows workstations, capture status/remotes/tracking/ahead-behind and create/verify Git bundle backups plus separate untracked-file backups.
2. Reconcile Full-Stack-Development paths and history using a fresh, reviewed proposal; keep #33 and #35 draft until each content/provenance gate is satisfied.
3. Repair the `virtual` transitive minimatch dependency through the owning dependency, then regenerate pnpm lockfile and run the full applicable test suite.
4. Validate Computer-Classes #6 and altair #3 with fresh PR checks before merge.
5. Use an administrator-authorized GitHub session to configure and verify branch rulesets, required CI, secret scanning, push protection, Dependabot alerts, and default branch auto-delete policy.
6. Complete full paginated branch, PR, workflow, security-alert, and releases/tags inventory before making cleanup decisions.


## Verification correction — default-branch protection flags
A fresh live GET of each repository's exact default-branch endpoint reports `protected: true` for all seven default branches:
- Full-Stack-Development `main`
- Computer-Classes `main`
- virtual `main`
- rea `main`
- altair `master`
- git `master`
- prayaggaikwad96 `main`

This confirms that GitHub currently marks every default branch as protected. The branch-protection detail endpoint still returns HTTP 403 to this integration, so exact rule contents remain unverified: required check names, required review count, stale-review dismissal, admin enforcement, force-push/deletion restrictions, and ruleset-vs-classic configuration. Do not describe protection as absent; describe detailed policy as inaccessible to this connection.

## Audit PR validation
This report is submitted as draft PR #38: https://github.com/prayaggaikwad96/Full-Stack-Development/pull/38. Its initial run passed seven checks on audit commit `7d60970679628b14da47aab11a222faaf8b1667e` (repository invariants and six Python/Node matrix jobs). The audit is documentation-only and must not be treated as approval to merge any other PR.


## Additional fork synchronization finding — REA
The fork `prayaggaikwad96/rea` is diverged from parent `morluto/rea`:
- Fork `main`: `938312834afe8aa32eb8d144e240f1675d68b621`
- Upstream `main`: `e9b6c87c1cacac24a0376a93e70aa07d0d530b9a`
- Comparison: upstream has 214 commits not in the fork; the fork has 7 commits not in upstream.
- The fork's unique direct file delta against upstream includes the fork synchronization audit document; preserve it.

A draft-only upstream-to-fork review PR was opened: [prayaggaikwad96/rea#16](https://github.com/prayaggaikwad96/rea/pull/16). GitHub reports 214 commits, 2,173 changed files, 174,721 additions and 17,459 deletions, and initially returned `mergeable: false` at creation; a later live PR fetch reports `mergeable: true`. This is only GitHub's current mergeability calculation, not a safety approval. Keep the PR draft. The size still requires full content review, current head CI, and verification that all seven fork-only commits and the audit document remain preserved. This PR did not move either branch ref.

The other checked fork relationships do not show missing upstream commits at the inspected tip: `virtual` local main is one commit ahead of upstream; `altair` local master is seven commits ahead; `git` local master is one commit ahead. These are point-in-time comparisons and should not be force-synchronized.
