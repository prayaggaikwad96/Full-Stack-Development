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
