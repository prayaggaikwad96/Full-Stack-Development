# Account-wide GitHub audit — November 1, 2026

## Scope
Remote review of the six repositories accessible under `prayaggaikwad96`. Repository files, current refs, PR inventory, and selected GitHub Actions runs were inspected. This is not a verification of Windows working trees, private security settings, or organization/account billing and secrets.

## Owner repositories
- `Full-Stack-Development` — default branch `main`; public; not archived.
- `Computer-Classes` — default branch `main`; public; not archived.
- `virtual` — default branch `main`; public; not archived.
- `rea` — default branch `main`; public; not archived.
- `altair` — default branch `master`; public; not archived.
- `git` — default branch `master`; public; not archived.

## Full-Stack-Development
- Main: `5d54529803ec6772bf9923c22f1aa7e698848868`.
- Developer: `33eb13cf83db41825e3184d4bb4314d0a4750630`.
- Shared merge base: `db1f8569d21a8bb41baec229fae4326f2c65aa43`.
- Current compare: divergent; 248 Developer-only commits and 44 main-only commits. Both unique histories remain preserved.
- 19 branches; no open PRs in the latest inventory. Closed PRs are historical records.
- Branch metadata reports `protected: false`; rulesets endpoint returned an empty list.
- Corrected CodePilot workflow to run on every push to `main` and every pull request targeting `main`; retained Python 3.12–3.15 / Node.js 22 and 24 matrix.
- Corrected README wording to match the workflow.
- On latest audited main SHA `5d54529803ec6772bf9923c22f1aa7e698848868`: CodePilot tests, nested-tree audit, and .gitignore validation passed; CodeQL was still in progress at last observation. Recheck live before merging/releasing.
- No primary branch mutation, branch deletion, or PR alteration performed.

## Computer-Classes
- `main` and `Developer` compare identical at `e53a39c85f7b3395f793c8cea61dd0955974fbcf`.
- No open PRs and no workflow runs appeared in the latest limited sample.
- Default branch metadata reports unprotected. No ruleset was verified in this pass.
- Keep this lightweight learning archive; do not add unnecessary CI solely for appearance.

## virtual (TanStack/virtual fork)
- Default branch: `main`, observed head `51b06cd5e078a289fe1cbf25a8d2e647aa98bfff`.
- Branch comparison using an assumed upstream branch name did not resolve; no upstream synchronization conclusion is made.
- No open PRs in the latest owner-repository inventory; historical upstream contribution PRs are not equivalent to fork-local open PRs.
- No recent Actions runs were returned in the limited sample.
- Do not update fork refs or alter the upstream PR without inspecting the actual upstream and fork commit graph and required test suite.

## rea (morluto/rea fork)
- Default branch: `main`, observed head `42a912e196523f5ff401ebc6ee95cc90580c841b`.
- No open PRs in the latest owner-repository inventory.
- Recent CI timings runs on older commit `7590b50801553ca443922b1fb48e168334f8cc5d` passed; PR readiness/title runs on feature commit `287bf3357d9ae29afe214431d079ea283ee37237` passed.
- The limited run list does not prove that current main was tested. Recheck the full upstream/fork comparison and run the project’s prescribed checks before claiming synchronized or complete.
- Default branch metadata reports unprotected.

## altair (altair-graphql/altair fork)
- Default branch: `master`, observed head `2deae0675ebf170e0bc8eac743de609a1c7dd07d`.
- No open PRs in the latest owner-repository inventory; two closed unmerged historical PRs remain.
- CodeQL passed on the observed default head (run [40340346718](https://github.com/prayaggaikwad96/altair/actions/runs/40340346718)).
- Scorecard run [40511367244](https://github.com/prayaggaikwad96/altair/actions/runs/40511367244) failed before analysis while pulling `gcr.io/openssf/scorecard-action:v2.4.0`. Do not weaken or disable Scorecard to hide the external image/registry problem.
- The Oct 24 general workflow [40107547203](https://github.com/prayaggaikwad96/altair/actions/runs/40107547203) had a separate Electron Linux packaging failure and Docker Hub login failure; most test, E2E, Tauri, Windows packaging and npm publish jobs passed. Logs are inconclusive about whether the login failure is missing/invalid repository secrets or an external service issue; inspect repository secrets and rerun after verifying credentials.
- This review did not edit upstream fork workflows or secrets.
- Default branch metadata reports unprotected.

## git (upstream Git mirror)
- Default branch: `master`, observed head `b9e5cff1803ab24582201ef059516eb16014b9d9`.
- No open PRs and no recent Actions runs appeared in the limited sample.
- Preserve upstream content and licensing; avoid arbitrary code changes.

## Cross-cutting governance gaps
- All six default branch metadata checks in the sampled set reported unprotected.
- The connected GitHub integration does not provide branch protection/ruleset write functionality. Owner action in GitHub Settings is required.
- Recommended: protect each maintained default branch with PR review, required stable checks appropriate to that repo, block force pushes and deletion, and avoid requiring checks that do not run on a given repository.
- Confirm secret scanning and push protection in Security settings; confirm Dependabot alerts and security updates. These settings were not visible in this audit and are not claimed enabled.
- Use least-privilege workflow permissions, maintain pinned reviewed Actions, and investigate actual failed job steps rather than suppressing failures.
- No branch deletions or PR record deletions were performed.

## Local-device blockers
On both Windows PCs, run the checked-in audit script from each actual clone and inspect working tree, untracked files, worktrees, remotes, local-only commits, nested Git/submodule state, and offline backups. Remote GitHub cannot validate local-only data. Do not reconcile or delete recovery refs until this evidence is reviewed.

## Conclusion
Two remote documentation/CI corrections were made in Full-Stack-Development. Its CodePilot matrix now runs for every main push and the latest selected CI checks passed except CodeQL remained in progress at the last observation. Computer-Classes primary branches are identical. Altair has an external Scorecard image-pull failure plus separate release-job failures requiring registry/credential investigation. REA, virtual, and git still require deeper upstream/CI review for any complete synchronization claim. No owner-side security controls or Windows local state are verified, so account-wide "fully complete" status cannot yet be claimed.


## Final CI refresh — 2026-11-01
On current Full-Stack-Development main `5d54529803ec6772bf9923c22f1aa7e698848868`:
- CodePilot test matrix [41327147269](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/41327147269): success.
- Nested project tree audit [41327147277](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/41327147277): success.
- Root .gitignore validation [41327147273](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/41327147273): success.
- CodeQL [41327147262](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/41327147262): success.
- This confirms these remote checks on the stated main SHA only; it does not verify local Windows state or the Developer branch.


## Subsequent safe fast-forward sync — November 1, 2026
After checking exact upstream refs and verifying that both forks contained zero fork-only commits:
- `prayaggaikwad96/virtual:main` was fast-forwarded from `51b06cd5e078a289fe1cbf25a8d2e647aa98bfff` to upstream `TanStack/virtual:main` at `0a368c76950610227af7a5d3695e53877f9ad914`. Post-update ref verification confirms equality with upstream.
- `prayaggaikwad96/git:master` was fast-forwarded from `b9e5cff1803ab24582201ef059516eb16014b9d9` to upstream `git/git:master` at `50fe5cc63f9cd6e89b87a2c9ccf96a444f4cfdb7`. Post-update ref verification confirms equality with upstream.
- Both updates used non-force fast-forward ref updates with expected prior SHA leases. No commits unique to either fork were displaced.
- No new Actions runs appeared on these repos after the ref updates; run the projects' recommended tests on a local checkout before treating builds as validated.
- `altair` remains exactly equal to upstream at `2deae0675ebf170e0bc8eac743de609a1c7dd07d`.
- `rea` remains divergent from upstream: fork is 6 commits ahead and 43 commits behind, so no ref update was attempted.
- `Full-Stack-Development` remains divergent: Developer is 248 commits ahead and main is 46 commits behind; neither primary ref was changed.


## Live remote verification — 2026-11-01 22:11 IST

This section supersedes stale counts and status statements above where the live observations differ.

### Current refs and repository hygiene
- `virtual:main`: `0a368c76950610227af7a5d3695e53877f9ad914`, equal to observed upstream `TanStack/virtual:main`.
- `git:master`: `50fe5cc63f9cd6e89b87a2c9ccf96a444f4cfdb7`, equal to observed upstream `git/git:master`.
- `altair:master`: `2deae0675ebf170e0bc8eac743de609a1c7dd07d`, the same observed tip as its upstream baseline in the previous audit; verify equality again before future sync.
- `Computer-Classes:main` and `Developer` both point to `e53a39c85f7b3395f793c8cea61dd0955974fbcf`.
- `REA:main`: `42a912e196523f5ff401ebc6ee95cc90580c841b`; live upstream `morluto/rea:main`: `1d343a88e53af51101a408d437641c60b7bb34e4` (Nov 1 commit). The fork is behind newer upstream work and must be reconciled from the new exact tip; do not treat the Oct 31 merge as current synchronization.
- `Full-Stack-Development:main`: `8e7f74b62115da1850d1be6952463c764b9dd293`; `Developer`: `33eb13cf83db41825e3184d4bb4314d0a4750630`. GitHub compare reports Developer 248 ahead and main 47 ahead, merge base `db1f8569d21a8bb41baec229fae4326f2c65aa43`. Both refs must be preserved pending a reviewed reconciliation.

### Live PR and branch-protection audit
- The live owner-repository inventory returned zero open PRs in all six repositories.
- All six default branch records report `protected: false`; all six repository rulesets endpoints return an empty list.
- Numerous closed topic, staging, and safety refs are preserved. No branches were deleted.
- Both Windows local clones/worktrees remain unverified; do not delete their branches or recovery refs until the local PowerShell audit is reviewed.

### CI / check qualification
- Live combined-status and PR-triggered workflow queries returned no status contexts and no workflow runs on the six current default-branch commit SHAs inspected. This means current-head CI is **unverified** through these queries, not passed.
- Historical CI results recorded earlier in this document apply only to their explicitly named historical SHAs and do not qualify later commits.

### Workflow scope finding
- The existing `.github/workflows/repository-consistency.yml` on Full-Stack-Development runs on main push only when selected paths change, on PRs targeting main, manual dispatch, and weekly schedule. It is intentionally read-only for branch comparison and does not reconcile refs.
- Keep this workflow read-only; it correctly warns on divergence rather than rewriting refs automatically.

### Current conclusion
- Remote fast-forward synchronization verified for `virtual` and `git` at the exact SHAs above.
- `Computer-Classes` primary branches are identical.
- `altair` has no fork-local open PRs; upstream equality should be verified directly before future updates.
- `REA` needs a new upstream reconciliation based on upstream SHA `1d343a88e53af51101a408d437641c60b7bb34e4`, with CI.
- `Full-Stack-Development` needs a reviewed history reconciliation; current divergence is 248/47, not 248/46.
- Security rulesets/branch protections, current CI qualification, secrets/security alert settings, and Windows local checkout verification remain outstanding.
- No destructive operation or unreviewed branch deletion was performed.

## Live account refresh — November 2, 2026

This section supersedes earlier live-state claims in this historical report where they differ. It covers the six owner repositories visible to the authenticated account.

### Branches and synchronization
- `Full-Stack-Development`: PR #16 merged after all ten required checks and CodeQL passed. `Developer` was fast-forwarded to the resulting `main`; the branches compare identical.
- `Computer-Classes`: community PRs #1 and #2 merged. `Developer` was fast-forwarded to the resulting `main`; the branches compare identical.
- `virtual`: `main` is identical to `TanStack/virtual:main` at `0a368c76950610227af7a5d3695e53877f9ad914`.
- `git`: `master` was fast-forwarded without force from `50fe5cc63f9cd6e89b87a2c9ccf96a444f4cfdb7` to upstream `git/git:master` at `ebdc087dc99d68bb340c282b2ba5f722def28d19`; post-update comparison is identical. The recovery backup branch was left intact.
- `altair`: `master` is 7 commits ahead of `altair-graphql/altair:master`, 0 behind. Preserve the fork-only history.
- `rea`: `main` is 6 commits ahead and 76 behind `morluto/rea:main`. Preserve both histories and do not merge until the full divergence is reviewed.

### Branch protection and security
- PRs are required on `Full-Stack-Development:main` and `Computer-Classes:main`; force-push and deletion are blocked, and administrators can bypass. Full-Stack requires 10 checks that run on every PR (CodeQL analysis, repository invariants, and the eight Python/Node matrix jobs), with the branch required to be up to date. Path-scoped nested-tree and `.gitignore` checks are not global requirements. Computer-Classes has no required checks until reliable checks are available. These settings were verified after applying them.
- No repository rulesets were present on the six repositories.
- Dependabot vulnerability alerts are enabled on all six repositories.
- Automated Dependabot security updates are enabled on the two first-party repositories, `Full-Stack-Development` and `Computer-Classes`; the four forks were left unchanged.
- Secret scanning and push protection are enabled on all six repositories. Non-provider-pattern secret scanning is disabled.

### CI, community health, and PR inventory
- Full-Stack-Development CodeQL and repository consistency passed on SHA `50778e6e9aaf7a4bdca27ffc8a69653a027e6144`; CodePilot tests, `.gitignore` validation, and nested-tree audit passed on that SHA on November 1.
- Computer-Classes' Dependabot dynamic run failed on SHA `59c573635430b9973b5e03de5212edbb2bd539c9`: it requested the `github_actions` ecosystem and `/.github/workflows/<anything>.yml`, but the repository has no workflows directory and its current Dependabot file has `updates: []`. Its dependency graph has no external package entries. No dummy manifest or ecosystem was added; the dynamic job's source still needs GitHub-side investigation.
- Altair CodeQL passed on its current `master` SHA `c96f9dd2dfe680dc553262ef65cc6b513d701c3c`. Its Dependabot, Scorecard, and main workflow runs failed; their logs were unavailable through the CLI, so causes are not asserted.
- Current `main`/`master` CI evidence for Virtual, REA, and Git was absent in the inspected check-runs. Do not treat lack of a run as a pass.
- At the start of this November 2 refresh, no open PRs were returned for the six owner repositories. TanStack Virtual #1335 is merged; Virtual #1321, Altair #3341, REA #6025–#6027, REA fork #13, and Full-Stack #13–#14 are closed unmerged. Do not reopen or resubmit without reviewing their diffs and maintainer context.
- Both first-party repositories now report 85% community health. Full-Stack [PR #16](https://github.com/prayaggaikwad96/Full-Stack-Development/pull/16) merged at `b77343abd392eeae9ffcb332c3f09e7bd4354846`; all ten required checks and CodeQL passed. Computer-Classes [PR #1](https://github.com/prayaggaikwad96/Computer-Classes/pull/1) and [PR #2](https://github.com/prayaggaikwad96/Computer-Classes/pull/2) merged; its profile recognizes the Contributor Covenant. Both profiles now recognize issue and pull-request templates; neither reports a root license. Repository descriptions match the scope stated in each README. Root licenses remain deferred pending provenance review.
- No `prayaggaikwad96/prayaggaikwad96` profile README repository was found. No profile repository or metadata was created or changed.

### Remaining verification
- The Windows repository audit was not run: it inspects local clones outside this worktree and writes a CSV under `%TEMP%`. Verify each actual clone and backup on the user's Windows machines before claiming local synchronization.
- Computer-Classes' Dependabot dynamic-run failure, Altair failures, stale/missing CI evidence on Virtual/REA/Git, upstream PR decisions, Windows local synchronization, and root-license provenance remain open work as of this report update. No recovery branch was deleted or rewritten.
