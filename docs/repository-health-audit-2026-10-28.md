# Repository health audit — 2026-10-28

## Scope and confidence

This is a remote snapshot of the repository after maintenance PR #11 merged on 28 October 2026. Live GitHub ref comparisons and Actions results are authoritative for remote state only. GitHub cannot prove that a Windows working tree is clean or synchronized.

## Verified remote state

- Repository: [`prayaggaikwad96/Full-Stack-Development`](https://github.com/prayaggaikwad96/Full-Stack-Development), public and not archived.
- Default branch: `main`; current snapshot SHA at time of this audit entry: `7cc55178a81116d1a9f32c43ba5fc6fef9b46486`.
- [PR #11](https://github.com/prayaggaikwad96/Full-Stack-Development/pull/11) merged via squash at 2026-10-28 06:55:01 UTC. It adds CodeQL, weekly GitHub Actions dependency updates, security/contribution documentation, a pull-request checklist, broader PR test coverage, and this audit refresh.
- `Developer` was fast-forwarded with `force=false` using an expected old SHA. A fresh compare after audit refresh reports `main` and `Developer` identical at `7cc55178a81116d1a9f32c43ba5fc6fef9b46486` (0 commits ahead and 0 behind).
- The intentional recovery branch `archive/codepilot-feature-history-before-sync-2026-10-27` remains divergent: 36 commits ahead and 156 behind `main`. Preserve its unique history.
- `docs/github-profile-readme` remains 2 commits ahead / 26 behind `main`; `profile/readme-final` remains 1 ahead / 21 behind. Their tracked `docs/github-profile/README.md` file is byte-identical to `main` (blob SHA `7ee1b595e76a4b8dc455a0ad950ad6201b60bbbe`). The branches have divergent histories; preserve them until their unique commits, local refs, and backups are reviewed. File equality alone does not make a branch safe to delete.
- PR #11's [CodePilot test matrix](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40646535324) passed all eight Python 3.12–3.15 / Node.js 22 and 24 combinations. Its [CodeQL analysis](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40646535563) completed successfully.
- Post-merge checks on `ac622b91c5e294f1d255e6712e3fb7deb2c3ee97` passed: [nested-tree audit](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40646889241), [root .gitignore validation](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40646889196), and [CodeQL analysis](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40646889193). Following this audit-only refresh, checks on `7cc55178a81116d1a9f32c43ba5fc6fef9b46486` also passed: [nested-tree audit](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40647423177), [root .gitignore validation](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40647423230), and [CodeQL analysis](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40647423251). The CodePilot tests, branch audit, and Dependabot version-update workflow had passed on the preceding `9c85c8512effe17c531e1425c1f3393ad3b4e9a1` commit; that later commit changed only this audit document.

## Repository quality and supply-chain safeguards

- Root README now links the [contribution guide](../CONTRIBUTING.md), [security policy](../SECURITY.md), [pull-request template](../.github/pull_request_template.md), [CodeQL workflow](../.github/workflows/codeql.yml), and [Dependabot config](../.github/dependabot.yml).
- CodeQL is configured for GitHub Actions, JavaScript/TypeScript, and Python on `main` pushes, pull requests, a weekly schedule, and manual dispatch. This is not a claim that every language or file type in the learning archive is covered.
- Dependabot version updates are configured weekly for GitHub Actions. This is separate from Dependabot security alerts and security updates, which need their own settings.
- The CodePilot test matrix now runs on every pull request to `main`; its push workflow remains path-filtered.
- The branch audit remains read-only. It reports branch reachability and does not delete branches.

## Branch protection and security settings still requiring manual review

- GitHub reports `main` as unprotected, with required status checks disabled; the repository rulesets endpoint returns an empty list. The connected GitHub actions expose settings reads but no mutation action for branch protection or rulesets; therefore these controls cannot be enabled from this connection.
- In repository **Settings → Rules → Rulesets** (or **Branches**), add a ruleset targeting `main`: require pull requests, block force pushes and deletion, and require checks only after confirming their exact successful names. Candidate checks from PR #11 are `CodeQL analysis` and the eight `Python <version> / Node.js <version>` matrix jobs. Consider requiring conversation resolution and linear history as appropriate for your workflow.
- In **Settings → Advanced Security** (or the available **Security** settings), check secret scanning, push protection, Dependabot alerts, and Dependabot security updates. Their state was not exposed by the read-only public API response, so this audit does not assert they are on or off.
- The `SECURITY.md` disclosure guide is now present. Availability of GitHub's private vulnerability reporting depends on the repository's security settings.

## Windows checkout — not remotely verified

No local audit output was supplied. The local Windows checkout remains out of scope for this remote GitHub check. Local uncommitted/untracked files, local-only commits, tracking refs, and submodule state remain unverified. On the Windows PC, run the read-only script [`docs/windows-repository-audit.ps1`](windows-repository-audit.ps1) from PowerShell and inspect the results for both `C:\\Prayag Gaikwad` and `C:\\Prayag Gaikwad\\Full-Stack-Development`. Do not reset, overwrite files, force-push, or delete local branches until differences and backups have been reviewed.

## Licensing

No root license was added because this is a mixed learning archive with legacy material of uncertain provenance and intended license. Keep project-specific license notices, including CodePilot Free's own MIT license, and review ownership before licensing the whole repository.
