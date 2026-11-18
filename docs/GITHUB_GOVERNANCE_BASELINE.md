# GitHub repository governance baseline

This repository uses a protected default branch and a reviewed integration branch.

## Branch policy
- Protect `main` and `Developer`; require pull requests for changes.
- Require current CI checks before merge, including CodeQL and repository-specific validation.
- Require at least one approval where independent reviewers are available. For a solo-maintained repository, document the exception and rely on required CI and protected administrator rules.
- Dismiss stale approvals when new commits are pushed.
- Require conversation resolution and prevent force pushes and branch deletion.
- Keep linear history if compatible with the project's established workflow.
- Do not automatically synchronize `main` and `Developer` when their histories or content have not been reviewed.

## Pull request policy
- Keep pull requests small and scoped.
- Separate source/content changes from workflow or security maintenance.
- Review generated and third-party code changes before merging.
- Merge only after exact-head checks pass and all review threads are resolved.
- Preserve recovery references until the corresponding primary branch is verified.

## Actions and supply-chain policy
- Set workflow-level permissions to read-only and grant write access only to jobs that need it.
- Pin third-party actions to verified full commit SHAs and retain release comments.
- Disable checkout credential persistence unless a job explicitly requires authenticated Git operations.
- Set job timeouts and concurrency groups; avoid cancelling critical default-branch baselines.
- Keep CodeQL enabled for every language actually present.
- Keep Dependabot enabled only for package ecosystems and manifest locations that exist.

## Secrets and releases
- Never commit tokens, private keys, passwords, or production credentials.
- Use repository/environment secrets and least-privilege tokens.
- Protect release and deployment environments with required reviewers where practical.

## Backup and recovery
- Maintain independent backups of important work outside GitHub.
- Verify restore procedures periodically.
- Do not treat a remote backup branch as the only backup.
- Never force-push or delete recovery branches as part of routine cleanup.

## Verification
After changing repository settings, verify effective branch protection/rulesets, exact required status-check names, and workflow results from the GitHub UI or an administrator-capable API connection.
