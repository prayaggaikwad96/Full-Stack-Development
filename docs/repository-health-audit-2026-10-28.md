# Repository health audit — 2026-10-28

## Scope and confidence

This audit distinguishes live remote GitHub state from work that requires the Windows PC. The remote findings below were collected on 28 October 2026. The maintenance changes described at the end are proposed on branch `chore/github-recommendations-2026-10-28`; their CI and security-analysis outcomes must be rechecked after the pull request is merged.

## Verified remote state

- Repository: [`prayaggaikwad96/Full-Stack-Development`](https://github.com/prayaggaikwad96/Full-Stack-Development), public and not archived.
- Default branch: `main`.
- Snapshot commit: `acb0115cba664e88d062b9da1a05337824bd64b4`.
- `Developer` was safely fast-forwarded from `3038accb3cdc1d5ceba22dcf3f0c91760a7e6b34` to the snapshot commit using a non-force update with the expected old SHA. A fresh comparison then reported `main` and `Developer` identical (0 ahead, 0 behind).
- The historical branch `archive/codepilot-feature-history-before-sync-2026-10-27` is intentionally divergent: 36 commits ahead and 155 behind `main`. Preserve this recovery history.
- The remote branch list at audit time was `main`, `Developer`, `archive/codepilot-feature-history-before-sync-2026-10-27`, `docs/github-profile-readme`, and `profile/readme-final`.
- The README-related branches are not ancestors of `main`, but the tracked `docs/github-profile/README.md` blob is byte-identical across `main` and both branches (blob SHA `7ee1b595e76a4b8dc455a0ad950ad6201b60bbbe`). Keep the branches until local references and any unique commit history are reviewed and backed up; do not delete them just because their file content is already present.
- No open pull requests were present before this maintenance update. PR [#10](https://github.com/prayaggaikwad96/Full-Stack-Development/pull/10) is merged; PR [#9](https://github.com/prayaggaikwad96/Full-Stack-Development/pull/9) remains closed as superseded.
- The `.gitignore` validation and nested-tree audit both passed on the snapshot commit: [gitignore run](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40645361292), [tree audit run](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40645361206).
- The most recent successful CodePilot test matrix observed during this audit was run [#40571925649](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40571925649), on `38d59da645a92201f83363c785fb37affb4a644a`. The later `main` changes at the snapshot were documentation-only and did not change CodePilot source or tests.

## Branch protection and repository security settings

- GitHub reported `main` as unprotected, with required status checks disabled. The repository rulesets endpoint returned an empty list.
- This connected GitHub toolset can inspect these settings but does not expose a write operation for branch protection or rulesets. Configure the rules in GitHub's repository Settings after the relevant PR checks have run: require pull requests for `main`, prevent force pushes and deletion, and require the agreed status checks. Do not choose required check names until their current runs appear in GitHub.
- The public-API view used for this audit did not expose secret-scanning, push-protection, or Dependabot security-alert settings. Do not interpret this as proof that they are enabled or disabled.

## Windows checkout — not remotely verifiable

GitHub's remote refs and Actions cannot tell whether the local Windows working tree has unsaved changes, untracked files, local-only commits, or mismatched submodules. No local audit output was provided. Before deleting branches or replacing files, run the read-only script `docs/windows-repository-audit.ps1` from PowerShell on the Windows PC and review its output for both `C:\\Prayag Gaikwad` and `C:\\Prayag Gaikwad\\Full-Stack-Development`. Do not run broad resets or force-pushes to resolve any differences automatically.

## Maintenance changes proposed for review

The maintenance branch adds a responsible-disclosure policy, contribution instructions, a pull-request checklist, weekly GitHub Actions dependency updates, and a CodeQL workflow for GitHub Actions, JavaScript/TypeScript, and Python. It also removes the path filter from pull-request-triggered CodePilot tests so the test matrix runs on every PR, while keeping push runs path-filtered, and updates the read-only branch-audit workflow to include the current README-related legacy branches.

After merge, recheck the CodeQL workflow result, CodePilot test matrix, main/Developer comparison, and settings above. A configuration file is not proof that a workflow completed successfully or that a GitHub-hosted security toggle is enabled.

## Licensing note

No repository-wide license was added. The root contains a mixed learning archive and legacy files; licensing the entire tree without checking the provenance and intended license of existing material would be unsafe. Keep project-specific license notices and clarify ownership before adding a root license.
