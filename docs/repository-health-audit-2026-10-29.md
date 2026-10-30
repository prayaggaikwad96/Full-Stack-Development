# Repository health and branch synchronization audit — 2026-10-30

## Scope
Remote-only audit of the public repository using GitHub metadata, commit comparisons, Actions workflow runs, pull request metadata, and repository files. This does not verify the owner's local Windows worktree, local-only commits/backups, nested repository configuration, or account/repository security-alert settings.

## Verified repository state

**Rechecked 2026-10-30:** at main head `0bbf192f301959f09f7f0978091d08cdd832532f`, the comparison `main...Developer` is 247 commits ahead on Developer and 22 commits ahead on main. Shared merge base is `db1f8569d21a8bb41baec229fae4326f2c65aa43`. The behind count changes with new main commits; rerun the comparison before any ref mutation.
- Default branch: `main`.
- Main head at audit time: `0bbf192f301959f09f7f0978091d08cdd832532f`.
- Developer head at audit time: `204748099731c3aeb04963e6d8957dcd569daf62`.
- GitHub compare reports a shared merge base: `db1f8569d21a8bb41baec229fae4326f2c65aa43`.
- Compare `main...Developer`: Developer is 247 commits ahead and main is 22 commits ahead; status is `diverged`. The reverse comparison confirms main is 22 commits ahead and Developer 247 commits ahead.
- Therefore, the branches are not synchronized. The previous "no common ancestor" assertion is incorrect for this live snapshot.
- Both refs report `protected: false` in the branch metadata response. The repository rulesets endpoint returned an empty list.
- The `archive/codepilot-feature-history-before-sync-2026-10-27` recovery branch remains at `6c68a09756d30a004f2519dab06c9da7494005c8`. GitHub compare currently returns no common ancestor between this branch and `main`; preserve it.
- Open PR #12 is a draft documentation checklist; it is not a synchronization candidate and should not be merged merely to reduce the open-PR count.
- Previous audit documents and PR comments contain stale branch heads/counts. Revalidate before using them for any ref mutation.

## Latest CI evidence on exact main head
Commit: `0bbf192f301959f09f7f0978091d08cdd832532f`.
- CodeQL run on this SHA is still in progress at final recheck.
- Nested-tree audit run #41038576318 for this SHA is in progress at final recheck.
- Root `.gitignore` validation run #41038576273 for this SHA is in progress at final recheck.
- The three previous checks plus CodeQL all completed successfully on parent SHA `08cbdc0…`; the new runs on this exact SHA remain in progress.
- The CodePilot test workflow remains configured for Python 3.12–3.15 and Node.js 22/24. Its successful run on the open PR head is separate from the main-head result; check exact run SHA before treating its matrix as validation of main.

## Security and quality controls
- CodeQL workflow exists; the run against the latest main head was still in progress when this report was refreshed.
- Dependabot weekly GitHub Actions update configuration exists.
- SECURITY.md and CONTRIBUTING.md exist.
- Branch metadata reports `protected: false` for both `main` and `Developer`; required checks are not enforced by these branch refs.
- Rulesets list is empty.
- Secret scanning, push protection, Dependabot security alerts/security updates, private vulnerability reporting availability, and alert inventory were not verified.
- Main commit signature verification reports unsigned. This is not proof of compromise, but commit signing can be considered as a hygiene improvement.
- Configure branch protections/rulesets in GitHub Settings. Require PRs, appropriate checks, resolved conversations, and block force-push/deletion. Only select required checks using exact names observed on completed PR runs.

## Safe reconciliation plan
1. Run `docs/windows-repository-audit.ps1` on the real Windows checkout.
2. Confirm clean/dirty/untracked state, all remotes, local-only commits, worktrees, .gitmodules, nested repositories/submodules, and verified backups.
3. Preserve both current branch heads and archive references.
4. Inventory unique commits on both sides relative to the shared merge base; review commit subjects, patches, trees, generated files, dependencies, tests, and CodePilot project content.
5. Build a new reconciliation candidate branch; do not reset, force-push, or overwrite either shared branch as a shortcut.
6. Run the documented checks on the exact candidate SHA and inspect the complete diff.
7. Merge through a reviewed pull request only after unique work is accounted for and all applicable checks pass.
8. Recompare refs and confirm the intended relationship afterward.

## Other account repositories sampled
- Computer-Classes: main and Developer unprotected; no PRs or recent Actions runs returned in the sample.
- virtual (TanStack/virtual fork): branches remain unprotected; fork PR #1 is closed/draft and upstream PR #1321 needs focused tests and required CI. Upstream PR #1335 is recorded as merged in prior audit context.
- rea (morluto/rea fork): multiple topic branches; open draft PRs #11 and #12 are not a complete upstream synchronization. Upstream #6027 and #6025 still record missing focused local tests and required CI; #6026 records validation gaps; #6265 is described as superseded upstream.
- altair: CodeQL passed on the sampled master head; Scorecard run #40511367244 failed while pulling the Scorecard action container image, before analysis. A separate main workflow run #40107547203 also failed and requires diagnosis from its exact failed job.
- git: master branch unprotected; no PRs or recent Actions runs returned in the sample.
- This is a prioritised sample, not a complete audit of every file, workflow, dependency, release, or security alert in all repositories.

## What remains unverified
- Local Windows checkout and backups.
- Full CI across all projects and current PR heads.
- Repository security alert inventory and owner-side Settings toggles.
- Complete review of all 247/10 divergent commits.
- Complete upstream contribution readiness and human maintainer decisions.

## CI workflow correction
The previous `Repository consistency audit` workflow failed on PR #12 because it treated any unequal `main` and `Developer` heads as a failure and printed an obsolete no-common-ancestor branch. The live refs share a merge base. The workflow was updated on main at `922c98f781cc6c0060c861532dfcc73576f9f571` to report ordinary divergence as a warning, preserve the archive, validate required hygiene files, and run CodePilot source/tests without automatically changing refs. Its first run on this commit was still in progress at report time.

## Conclusion
Useful CI and documentation controls are in place, but the repository is not fully synchronized or fully hardened. Do not call synchronization complete until the 247/22 divergence has been reconciled after local backup and unique-history review, checks complete on the exact current main head, and owner-side security/rules settings are verified. No branch ref, recovery branch, or PR was merged or deleted during this audit.