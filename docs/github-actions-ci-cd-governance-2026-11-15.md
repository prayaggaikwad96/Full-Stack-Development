# GitHub Actions governance and CI/CD operations

This document defines the repository's safe CI/CD operating policy. It intentionally does not change branch protection, branch refs, deployment configuration, secrets, or primary-branch history.

## Required CI checks

For pull requests targeting `main` or `Developer`, retain the repository's existing checks and use exact current workflow/job names when configuring branch protection:
- `Verify repository invariants` (Repository consistency audit)
- `CodeQL analysis`
- `Python 3.12 / Node.js 22`
- `Python 3.12 / Node.js 24`
- `Python 3.13 / Node.js 22`
- `Python 3.13 / Node.js 24`
- `Python 3.14 / Node.js 22`
- `Python 3.14 / Node.js 24`
- `Python 3.15 / Node.js 22`
- `Python 3.15 / Node.js 24`

Do not configure a required context until a successful run has confirmed its exact name on the target branch. Do not make optional, path-filtered audits required checks unless they emit a check for every relevant pull request.

## Workflow security baseline

- Set the narrowest practical `permissions:` at workflow and job scope.
- Use read-only repository permissions for test and audit workflows.
- Disable persisted checkout credentials when a workflow does not need to push or create releases.
- Pin third-party actions to verified immutable commit SHAs; document the upstream release corresponding to each pin.
- Set explicit job timeouts and avoid unbounded matrix expansion.
- Use concurrency cancellation only where an in-flight run is safely superseded by a newer run for the same ref. Never cancel deployment, release, migration, or other non-idempotent operations without an explicit safety design.
- Do not expose secrets to fork-originated pull request code. Prefer `pull_request`; avoid `pull_request_target` for untrusted code execution.
- Use protected GitHub Environments and short-lived OIDC credentials for deployments. No deployment workflow is authorized by this document.
- Upload diagnostic artifacts with bounded retention and avoid including credentials, personal data, or unredacted logs.

## Branch protection and merge governance

Configure protection through an administrator-authorized GitHub settings session:
- Require pull requests before merging.
- Require the ten named CI contexts above only after confirming they are generated for every applicable PR.
- Require all review conversations to be resolved.
- Require branches to be up to date before merging, after testing the expected queue/merge behavior.
- Block force pushes and branch deletion on primary branches.
- Preserve administrator recovery access while documenting it.
- Consider requiring one approving review only when an independent reviewer is available; do not create an unworkable policy for a single-maintainer repository.
- Verify the effective settings after saving. An empty rulesets list is not evidence that classic branch protection is disabled or enabled.

## Dependency and security maintenance

- Keep Dependabot enabled for ecosystems with committed dependency manifests.
- Add package ecosystems only when a matching manifest/lockfile exists.
- Review grouped dependency PRs and release notes before merging.
- Keep CodeQL on supported languages and inspect alerts separately; a successful scan is not the same as zero alerts.
- Verify secret scanning, push protection, dependency graph, Dependabot alerts, and code-scanning alert state in an administrator-authorized security view.
- Never put tokens, keys, passwords, or production credentials in workflow YAML or logs.

## Synchronization and recovery

- Treat `main` and `Developer` as separate histories until a reviewed reconciliation proves otherwise.
- Never force-push, hard-reset, delete recovery branches, or bulk-overwrite learning content to make branch names appear synchronized.
- Before any reconciliation, verify both local worktrees, preserve uncommitted files, and create independent Git bundle backups that can be restored.
- Re-run checks on the final candidate SHA after all changes and review the actual PR diff before merge.

## Current baseline recorded 2026-11-15

- Main head: `05eaab095d716927ab5c3bf7fe0ffabda1ea8ea5`.
- Developer head: `50702be32d21c0216a45a2647cd6ebca100a9dda`.
- Main is 50 commits ahead of Developer and 0 commits behind.
- The open PR #35 is a synchronization proposal with learning-material removals. Do not merge until every removed or changed learning path is reviewed and local backups are verified.
- Latest inspected main runs (2026-11-14): CodeQL, eight CodePilot matrix jobs, repository invariants, and gitignore validation succeeded.
- Main is reported unprotected by the branch metadata endpoint; Developer is reported protected with ten required status contexts. The connected GitHub integration cannot read the branch-protection endpoint. Configure and verify main protection through authorized settings.
- The repository rulesets endpoint returned an empty list.
- CI workflow files on main and Developer differ. Retest each branch after any intentional workflow reconciliation.
- Secret scanning, push protection, complete alert inventories, local workstation state, and deployment policy remain unverified.

## Completion criteria

CI/CD is complete only when required checks are enforced on both primary branches, all security settings and alerts are verified, dependency updates are functioning for real manifests, workflow changes pass on exact commit SHAs, any synchronization diff is reviewed, and both local worktrees/backups are independently validated. Never report completion based only on green Actions runs.
