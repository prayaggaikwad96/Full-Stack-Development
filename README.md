# Full-Stack Development

A hands-on full-stack learning archive with web-development exercises and CodePilot Free, a local-first coding workspace built with Python, browser JavaScript, and Ollama.

## Repository status

- **Default branch:** `main`
- **Visibility:** Public
- **Last remote review:** 22 November 2026
- **Account:** [@prayaggaikwad96](https://github.com/prayaggaikwad96)

This repository contains learning materials, practical examples, and software projects. Individual examples may be educational, incomplete, or dependent on their documented toolchains.

> [!IMPORTANT]
> This README reflects a remote repository review on 22 November 2026. `main` is currently unprotected, and inspected protected branches have no required status-check enforcement. Local worktrees, external backups, restore tests, and complete security-alert inventories cannot be verified through this integration. Re-check GitHub settings and local machines before treating governance or synchronization as complete.

## Learning path

1. HTML and CSS fundamentals
2. JavaScript and browser APIs
3. Git and GitHub
4. React and other frontend frameworks
5. Backend development and APIs
6. SQL and NoSQL databases
7. Testing, debugging, security, and deployment

## Featured project: CodePilot Free

[CodePilot Free](projects/codepilot-free/README.md) is a local-first coding workspace built with Python's standard library, browser JavaScript, and Ollama. It provides a browser-based workspace, live HTML preview, project import/export, and local-model chat.

- [Read the CodePilot README](projects/codepilot-free/README.md)
- [Run the CodePilot test workflow](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/workflows/codepilot-tests.yml)

## Repository layout

- `Prayag Gaikwad/` — canonical learning materials and exercises. Use this path for new work.
- `Full-Stack-Development/` — legacy nested copy from an earlier repository/submodule conversion. Do not use it for new work or copy it over the canonical folder automatically.
- `.github/workflows/` — repository automation.
- `.github/ISSUE_TEMPLATE/` — issue forms and templates.
- `.github/dependabot.yml` — dependency-update configuration.
- `.gitignore` — excludes common generated files, local environments, and secrets.
- `docs/` — maintenance, audit, and operational documentation.

The archived nested-tree audit report records a point-in-time comparison. Its counts are not a guarantee that the two trees remain identical today. Keep the legacy nested copy until local repository/submodule state, unique files, and independent backups have been checked.

## Branch workflow and synchronization

- `main` is the default branch and the published source of truth.
- `Developer` is the development branch. Compare exact commit references before relying on synchronization; do not assume it is current.
- Preserve recovery and archive branches until their unique commits and content have been reviewed and independently backed up.
- Never force-push, reset, delete, or overwrite a primary or recovery ref as a shortcut to synchronization.
- Review learning-content changes as content, not as routine maintenance. A mergeable pull request is not automatically approved for merge.

### Live branch and synchronization snapshot — 22 November 2026

The remote branch API reported:

| Branch | Protection | Required status checks |
| --- | --- | --- |
| `main` | Disabled | None |
| `Developer` | Enabled | No current enforcement verified |

The current comparison `Developer...main` reports `main` 72 commits ahead and `Developer` zero commits ahead. This is a fast-forward-shaped history, not approval to synchronize. [PR #35](https://github.com/prayaggaikwad96/Full-Stack-Development/pull/35) contains a substantial 112-path educational-content and configuration change; review every path and verify local recovery state before merging.

**Required owner action:** Configure suitable protection for `main` in GitHub repository Settings. Require pull requests, block force pushes and branch deletion, and require only stable CI checks verified on relevant pull-request events. The connected integration does not expose protection-write operations, so this repository has not changed those settings.

### Open pull requests observed during this review

- [PR #35 — synchronize `main` into `Developer`](https://github.com/prayaggaikwad96/Full-Stack-Development/pull/35): substantial 112-path synchronization; content review and local recovery verification required.
- [PR #51 — refresh audit documentation](https://github.com/prayaggaikwad96/Full-Stack-Development/pull/51): documentation-only proposal; review its complete diff and current facts before merging.

Pull-request states and checks can change. Inspect live PRs and exact head SHAs before acting.

## CI, quality, and security

- [CodeQL workflow](.github/workflows/codeql.yml) scans configured GitHub Actions, JavaScript/TypeScript, and Python code.
- [CodePilot test workflow](.github/workflows/codepilot-tests.yml) validates the backend, browser JavaScript, integration behavior, and supported Python/Node combinations.
- On the observed `main` commit `1c703e24b07584fd8a0e1935a3654bacfcff825c`, CodeQL, all reported Python/Node matrix jobs, repository invariants, and ignore-rule checks completed successfully. These workflows do not validate every learning example or unrelated path.
- [Dependabot configuration](.github/dependabot.yml) requests configured dependency updates. Review generated pull requests and test them before merging.
- Use the [pull-request template](.github/pull_request_template.md) to document scope, tests, security hygiene, and compatibility.
- Use the [issue forms](.github/ISSUE_TEMPLATE) for bug reports and feature requests. Do not include secrets or private data.
- Report vulnerabilities privately according to [SECURITY.md](SECURITY.md).

A configured workflow is not proof that a particular commit passed. Check the latest workflow runs for the exact commit SHA being reviewed. Likewise, the existence of CodeQL or Dependabot configuration does not, by itself, prove that every alert, secret-scanning option, or account-level security control is enabled.

### Remaining operational verification

The following cannot be proven by a remote README update:

- Local Windows worktree status, uncommitted/untracked files, local-only commits, and nested repository/submodule state.
- Independently restorable backups and successful restore tests.
- Whether every branch and recovery reference has a current external backup.
- Exact-head CI success after each new commit.
- All repository and account security settings, including alert inventories and push-protection configuration.

Use dated audit documents as historical context only; do not treat them as proof of today's state.

## Adding examples

- Keep each example focused on one topic.
- Use descriptive filenames and consistent folder organization.
- Include setup, run, and expected-result instructions when dependencies are required.
- Update documentation when project structure or behavior changes.
- Add tests for behavior changes and regressions where practical.
- Do not commit API keys, tokens, passwords, real environment files, private records, or other sensitive data.
- Use `.env.example` for non-secret configuration templates.
- Respect upstream licenses, copyright notices, and attribution requirements.

## Validation

Before submitting a change:

1. Read the affected project's instructions and existing conventions.
2. Run the documented formatter, linter, and tests relevant to the change.
3. Review `git diff --check` and the complete diff.
4. Confirm no secrets, credentials, generated artifacts, or unrelated files were introduced.
5. Push a focused branch and open a pull request.
6. Wait for the exact-head required checks and review feedback; resolve findings before merging.
7. After merge, verify the target branch SHA and relevant workflow results.

The CodePilot test workflow and repository-specific workflows may cover different paths. Do not infer that a passing workflow validates unrelated projects or all files in this learning archive.

## Contributing and community standards

- [Contributing guide](CONTRIBUTING.md) — branch workflow, local validation, and review expectations.
- [Code of Conduct](CODE_OF_CONDUCT.md) — community standards and reporting options.
- [Security policy](SECURITY.md) — private vulnerability disclosure.
- [Pull-request template](.github/pull_request_template.md) — review checklist.

## License and third-party material

Check the repository's current license and the license of each dependency or copied learning resource before redistribution. Do not infer that all files share one license merely from the presence of a license file in a subdirectory. Preserve required notices and attribution.
