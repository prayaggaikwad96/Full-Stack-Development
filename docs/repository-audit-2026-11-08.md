# Repository audit — 2026-11-08

## Scope and method

This is a read-only remote audit of `prayaggaikwad96/Full-Stack-Development`, performed against GitHub's live repository and refs on 2026-11-08. It does not establish the state of either local PC or any untracked local files. Values below are a dated snapshot and must be refreshed before future branch operations.

## Repository identity

- Repository: https://github.com/prayaggaikwad96/Full-Stack-Development
- Owner: `prayaggaikwad96`
- Visibility: public
- Default branch: `main`
- Repository is not archived.
- Connected GitHub identity: `prayaggaikwad96`
- Connected integration reported repository admin, maintain, push, pull, and triage permissions.

## Live primary branch refs

| Ref | Commit |
|---|---|
| `main` | `42b32920dd18a2fadee8f9ec3f4660b775415c15` |
| `Developer` | `50702be32d21c0216a45a2647cd6ebca100a9dda` |
| Merge base | `35ddeabd4303a9a7a2eaf092d0203540f656d450` |

GitHub compare result for `main...Developer` was `diverged`: `Developer` is 2 commits ahead of the merge base and `main` is 15 commits ahead. This is not a fast-forward-only synchronization. Do not reset, force-push, or move either primary ref based on this report. Review the unique commits, affected paths, both local worktrees, and verified backups before proposing a merge.

## PR #33 — preserve Developer-only learning content

- URL: https://github.com/prayaggaikwad96/Full-Stack-Development/pull/33
- Title: `fix(repository): preserve Developer-only learning content on main`
- State at audit: open draft.
- Head branch: `fix/preserve-developer-learning-content-2026-11-07`
- Observed head commit: `11dea3eb7c53aee1019c518d86cf128a493f13b4`
- The PR description reports 531 restored source-only paths, 13 target-only paths retained, and no intended overwrites or deletions in its comparison against its recorded base.
- The PR description identifies 370 same-relative-path variants and four cross-branch conflicts requiring manual review.
- No submitted reviews or inline review threads were returned by the connected GitHub integration during this audit.
- Four associated CI workflows were returned as completed successfully for the inspected head: nested-tree audit, repository consistency, CodePilot tests, and CodeQL.

**Decision:** Keep PR #33 as a draft. Successful CI is necessary but does not resolve content provenance, same-path evolution, or canonical-root decisions. Review the exact current PR head and all unresolved path differences before changing its draft status or merging.

## Repository layout and safeguards

The root tree includes `README.md`, `.gitignore`, `.github/`, `docs/`, `projects/`, and a legacy nested `Full-Stack-Development/` directory. The README identifies `Prayag Gaikwad/` as the canonical learning path and says not to automatically copy the nested legacy tree over it. Preserve both paths until the Windows repository/submodule state and local backups are verified.

The root README, contributing guide, security policy, code of conduct, CODEOWNERS, Dependabot configuration, CodeQL workflow, CodePilot tests, gitignore validation, nested-tree audit, repository-consistency workflow, and read-only branch audit workflow were present at the time of inspection.

The branch audit workflow states explicitly that it reports candidates and never deletes branches. Keep that safety property.

## CI and security observations

- The latest listed CodeQL run for `main` at `42b32920dd18a2fadee8f9ec3f4660b775415c15` completed successfully.
- CodePilot tests cover Python 3.12–3.15 and Node.js 22/24.
- Dependabot is configured for weekly GitHub Actions dependency updates.
- The repository rulesets endpoint returned an empty list.
- The branch-protection read for `main` returned HTTP 403 `Resource not accessible by integration`. This is an integration permission limitation, not evidence that branch protection is absent.
- Secret-scanning status, push-protection status, and alert inventories were not independently verified by this audit.
- The repository metadata reports automatic branch deletion as disabled.

## Safe next actions

1. Keep both `main` and `Developer` unchanged until a commit-by-commit and path-by-path review is complete.
2. Verify local repository roots, remotes, checked-out branches, clean/dirty status, untracked files, upstreams, and ahead/behind counts on both PCs.
3. Create and verify independent Git bundle or mirror backups from both PCs before any reconciliation.
4. Review PR #33's same-path variants and four content conflicts; preserve the draft until the review is documented.
5. Use an administrator-authorized GitHub connection or repository settings UI to inspect and configure branch protections/rulesets. Require successful applicable CI, block force pushes and branch deletion, and avoid imposing an impossible approval requirement on a sole maintainer.
6. Inspect secret scanning, push protection, Dependabot alerts, and CodeQL alerts using an appropriately authorized connection.
7. Re-run the relevant CI on the final proposed branch head and record the exact SHA and check conclusions.
8. Consider enabling automatic deletion of merged topic branches only after verifying that recovery branches and active work are excluded.

## Explicit safety boundaries

Until the above evidence is collected, do not run or perform equivalent operations to:

- `git reset --hard`
- `git clean -fd`
- `git push --force` or force-update a primary ref
- `git pull --allow-unrelated-histories`
- Delete `Developer`, recovery branches, or duplicate project directories
- Merge PR #33 solely because CI is green

This report records observations and recommendations; it does not claim that repository synchronization, local workstation synchronization, or all security controls are complete.
