# Branch Protection Baseline

**Live status checked: 26 November 2026**

The repository branch listing reports:

| Branch | GitHub protected flag |
| --- | --- |
| `main` (default branch) | `false` |
| `Developer` | `true` |

This is a branch-level protection indicator, not a complete view of the active rule configuration. The connected GitHub integration cannot read the detailed classic branch-protection rules (GitHub returned 403 for the protection endpoint). The repository-level rulesets endpoint returned an empty list.

## Required remediation

Protect `main` before treating it as a safe integration target. Keep the existing `Developer` protection in place while reviewing whether its rules match the active workflow.

Recommended controls for `main`:

1. Require changes to enter through pull requests; do not permit routine direct pushes.
2. Require at least one approval from an independent reviewer when one is available. A pull-request author cannot approve their own work.
3. Dismiss stale approvals after new commits and require all review conversations to be resolved.
4. Require status checks only after confirming the exact check names run reliably on the default branch and pull requests. Start with CodeQL, CodePilot tests, repository consistency, and root gitignore validation where applicable.
5. Require the branch to be up to date before merging once the required check set is stable.
6. Block force pushes and branch deletion.
7. Include administrators in the rules and limit bypass to documented emergencies.
8. Do not require the nested-tree audit as proof of canonical/nested tree equivalence: it currently reports differences but is not a policy-based equality gate.

## Synchronization safety

The current `main` branch is 84 commits ahead of `Developer`, with `Developer` 0 commits ahead. This is a fast-forward relationship, not automatic merge authorization. Keep PR #35 in draft until the learning-tree content, local worktrees, independently restorable backups, and review requirements are verified. Do not force-push, reset, or delete recovery refs to make the branches appear synchronized.

## Apply and verify

Apply the settings in **Repository Settings → Rules → Rulesets** or **Settings → Branches**. This file is documentation only; it does not enable GitHub protection.

After applying the rule, verify the effective settings and a test pull request from an independent GitHub session. Record the exact required check names and confirm they complete successfully on the final commit.
