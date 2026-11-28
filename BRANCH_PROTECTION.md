# Branch Protection Baseline

**Live status checked: 28 November 2026**

## Observed repository state

The latest accessible repository/branch audit reports:

| Branch | Role | GitHub protected flag |
| --- | --- | --- |
| `main` | Default/integration branch | `false` |
| `Developer` | Development branch | `true` |

The connected GitHub integration was unable to read detailed classic branch-protection configuration (the protection endpoint returned 403) and did not return any repository rulesets. Therefore, the branch-level flags above must not be mistaken for a verified inventory of effective rule settings.

## Recommended protection for `main`

Configure a ruleset or branch-protection rule for `main` using the least-privilege settings appropriate to this repository:

1. Require pull requests for changes; disallow routine direct pushes.
2. Require at least one approval by someone other than the pull-request author, where an independent reviewer is available.
3. Dismiss stale approvals when the reviewed code changes and require all review conversations to be resolved.
4. Require only stable, exact status-check contexts that have been observed on the target branch and pull requests. Confirm their names and successful execution before making them mandatory.
5. Require branches to be up to date before merging only after the required check set is reliable.
6. Block force pushes and deletion of the protected branch.
7. Apply the rules to administrators and use narrowly scoped, documented bypass exceptions.
8. Do not treat a green nested-tree audit as proof of tree equivalence: the workflow currently generates difference reports and is not a policy-based equality gate.

Keep the existing `Developer` protection in place while its effective settings are independently reviewed.

## Synchronization status — 28 November 2026

The live GitHub compare from `Developer` (base) to `main` (head) reports:

- `main`: `f0f9a103c95cf89737901a3ecc3a7a926051d847`
- `Developer`: `50702be32d21c0216a45a2647cd6ebca100a9dda`
- `main` is **88 commits ahead** and **0 commits behind**.
- The merge base is the current `Developer` tip, so the remote commit graph is fast-forward-compatible.

This graph relationship is not approval to synchronize. PR #35 contains a large content and workflow change set (the current PR file listing is extensive) and its local worktree/recovery requirements cannot be verified by this remote integration. Keep PR #35 in draft. Do not merge it, force-push, reset, or directly move either branch until the full diff has been reviewed, local worktrees are confirmed clean, independent backups have been restore-tested, effective branch protection is verified, and independent review is obtained.

## Validation and limitations

- PR #68 is documentation only; this file does not enable branch protection.
- The integration does not expose the required administrative branch-protection write capability, and detailed effective settings remain unverified.
- A missing status response from the combined-status endpoint is not proof that checks passed. Verify exact-head GitHub Actions/check-run results in GitHub before requiring or claiming them.
- Re-run and verify required CI against the final merge candidate after any changes.
- Review the final PR diff and obtain an independent approval before merging.

Apply settings in **Repository Settings → Rules → Rulesets** or **Settings → Branches**, then verify the effective configuration and a test pull request from an independent GitHub session.
