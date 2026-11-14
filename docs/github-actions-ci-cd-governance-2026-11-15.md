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

## Live baseline — 15 November 2026

### Primary branches
- `main`: `038db41aff086a67e4ed39aa3bc8a53a27d7b6f7`.
- `Developer`: `50702be32d21c0216a45a2647cd6ebca100a9dda`.
- GitHub compare (`Developer` base, `main` head): `ahead`, 51 commits ahead, 0 behind. Developer's current remote history is an ancestor of main; this is a fast-forward ancestry relationship. It does not prove local worktrees contain no uncommitted/untracked work.
- Main branch metadata reports `protected: false`, with enforcement off and no required checks. Developer reports `protected: true` with ten required status contexts.
- The integration can read branch metadata but receives HTTP 403 from the detailed branch-protection endpoint. It cannot mutate branch-protection settings or create repository rulesets. The repository rulesets endpoint currently returns an empty array.
- Repository setting `delete_branch_on_merge` is enabled. Keep recovery/safety branches until independent backups and restore tests have been verified.

### CI/CD changes actually merged
PR #43 was merged to main as commit `038db41aff086a67e4ed39aa3bc8a53a27d7b6f7` after all five workflow suites passed on its exact PR head `219d9ed43dce4a84fec951973c2724d098955bdd`.

- All third-party action uses in the six existing workflows are pinned to full upstream commit SHAs.
- CodeQL now runs on pull requests targeting both `main` and `Developer`, matching the required CodeQL context configured on Developer.
- CodeQL has a 30-minute timeout, per-ref concurrency cancellation for superseded analyses, job-scoped least-privilege permissions, and checkout credentials are not persisted.
- Existing test and audit workflows retain read-only token permissions, timeouts, and artifact retention.
- Dependabot continues weekly GitHub Actions dependency updates so pinned references can be updated through reviewed PRs.

Pinned action references:
- `actions/checkout` v7 — `3d3c42e5aac5ba805825da76410c181273ba90b1`
- `actions/setup-python` v7 — `6d4fd22b20465ccc0f7354476588e8df7c9ca0e0`
- `actions/setup-node` v7 — `949feb2413d6458794dcd2491c4babbbce0c15c1`
- `actions/upload-artifact` v7 — `cf430e030ddbb5b0abf93d22962f4752f3646cd9`
- `github/codeql-action` v4 — `33d7b85da1a04171e211befe2c739303b9a4c066`

### Exact current Actions evidence
- PR #43 exact-head runs: CodeQL, Repository consistency, CodePilot tests (8 matrix jobs), nested-tree audit, and gitignore validation all succeeded.
- Following the merge, push runs for main: CodePilot matrix, repository consistency, nested-tree audit, redundant-branch audit, and gitignore validation succeeded. CodeQL push analysis was in progress at the last check.
- PR #35 updated exact head `038db41aff086a67e4ed39aa3bc8a53a27d7b6f7`: CodePilot matrix and repository invariants succeeded; CodeQL was running. It is now eligible for the CodeQL context because PR #43 added the Developer target.
- PR #35 remains draft. Its current diff is 37 files (+2,128/-61). It includes a user-content change to a nested login-page exercise (Tours & Travels to Vietnam Da Nang, including external image URLs) and added learning exercises. The three removed legacy paths and three removed `.gitkeep.txt` markers on Developer were independently checked and each is zero bytes; nonetheless, review the whole diff before merging.
- The ten required Developer contexts are: `Verify repository invariants`, `CodeQL analysis`, and all eight Python 3.12–3.15 / Node.js 22–24 matrix jobs. Gitignore and nested-tree audits are path-scoped supplemental checks and should not be configured as universal required checks.

### Security and repository settings still unverified
The GitHub connection cannot read/write Actions repository policy, security settings, secret-scanning alerts, Dependabot alerts, or CodeQL alert inventories. Therefore these are **not certified as enabled or clear**:
- Main protection, required PRs/checks, review policy, conversation resolution, stale approval dismissal, force-push/delete restrictions.
- Repository Actions policy, including enforcement of full-SHA pins and allowed-actions restrictions.
- Secret scanning, push protection, dependency graph, Dependabot security alerts, and the current code-scanning alert inventory.
- Environment protection, deployment credentials, release/deployment workflows, and any hosting target. No deployment pipeline was invented because no target or deployment process is established in this repository.
- Local state on each Windows workstation, including uncommitted/untracked files and independently restorable Git bundle backups.

### Current completion gate
CI workflow hardening is merged and its exact-head checks passed. Overall CI/CD governance and primary-branch synchronization are **not complete** until:
1. An administrator enables and verifies main protection with PR review rules, the ten applicable required checks, conversation resolution, and force-push/deletion restrictions.
2. The Actions settings enforce full-length SHA pinning and restrict allowed actions to approved publishers/repositories.
3. Secret scanning, push protection, dependency graph, Dependabot alerts, and CodeQL alerts are checked in GitHub Security settings.
4. PR #35's 37-file diff and its user-content changes are reviewed; its latest exact-head ten required Developer contexts succeed.
5. Both local worktrees are independently inspected and Git bundle backups are created and restore-tested before completing synchronization.

Never report complete based on green Actions alone. Do not force-push, hard-reset, delete recovery refs, overwrite learning content, or merge PR #35 solely to make branch names appear synchronized.

## Completion criteria

CI/CD is complete only when required checks are enforced on both primary branches, all security settings and alerts are verified, dependency updates work for actual manifests, workflow changes pass on exact commit SHAs, any synchronization diff is reviewed, and both local worktrees/backups are independently validated.
