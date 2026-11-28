# Full-Stack Development

A hands-on full-stack learning archive with web-development exercises and CodePilot Free, a local-first coding workspace built with Python, browser JavaScript, and Ollama.

## Repository status

- **Default branch:** `main`
- **Visibility:** Public
- **Last live-state review:** 22 November 2026
- **Account:** [@prayaggaikwad96](https://github.com/prayaggaikwad96)

This repository contains learning materials, practical examples, and software projects. Individual examples may be educational, incomplete, or dependent on their documented toolchains.

> [!IMPORTANT]
> This README reflects a remote repository review on 22 November 2026. The branch API reports `main` as unprotected and `Developer` as protected, but the connected integration cannot read branch-protection or ruleset details (HTTP 403). Required reviews, required status checks, bypass rules, and effective enforcement are therefore not verified. Local worktrees, independent backups, restore tests, and complete security-alert inventories also cannot be verified through this integration. Re-check repository Settings and local machines before treating governance or synchronization as complete.

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
- `Developer` is the development branch. The branch API reports a protected flag, but detailed rules could not be inspected; compare exact commit refs before relying on synchronization.
- Preserve recovery and archive branches until their unique commits and content have been reviewed and independently backed up.
- Never force-push, reset, delete, or overwrite a primary or recovery ref as a shortcut to synchronization.
- Review learning-content changes as content, not as routine maintenance. A mergeable pull request is not automatically approved for merge.

### Live branch and protection snapshot — 22 November 2026

The live branch listing reported the following protection flags. The detailed branch-protection and ruleset endpoints returned HTTP 403 through the connected integration, so the effective requirements and bypass rules could not be verified.

| Branch | Branch API `protected` flag | Detailed enforcement |
| --- | --- | --- |
| `main` | `false` | Not readable; verify in repository Settings |
| `Developer` | `true` | Not readable; verify in repository Settings |

A historical audit recorded ten required checks on `Developer`; that list is not confirmed as current and must not be copied into settings without checking the exact checks emitted by current workflows:

1. `Verify repository invariants`
2. `CodeQL analysis`
3. `Python 3.12 / Node.js 22`
4. `Python 3.12 / Node.js 24`
5. `Python 3.13 / Node.js 22`
6. `Python 3.13 / Node.js 24`
7. `Python 3.14 / Node.js 22`
8. `Python 3.14 / Node.js 24`
9. `Python 3.15 / Node.js 22`
10. `Python 3.15 / Node.js 24`

**Required owner action:** In repository Settings, protect `main`: require changes through pull requests, require stable checks that run on every relevant PR, resolve review conversations, and block force pushes and branch deletion. Require an independent approval when a reviewer is available; do not configure an impossible self-approval rule for a solo-maintained project. Keep any administrator bypass intentional and documented. Verify the saved rule and applicable rulesets after changing them.

### Pull requests and synchronization

Always use the [live pull-request list](https://github.com/prayaggaikwad96/Full-Stack-Development/pulls) rather than a hard-coded README list; PR states and checks change. The current `main` to `Developer` proposal is a substantial 112-path change, including learning-content moves and five removed paths. Keep it in draft until every affected educational file is reviewed, local worktrees and independent backups are verified, and the final proposed result passes CI. A green check or GitHub's mergeable flag is not approval to merge.

## CI, quality, and security

- [CodeQL workflow](.github/workflows/codeql.yml) scans configured GitHub Actions, JavaScript/TypeScript, and Python code.
- [CodePilot test workflow](.github/workflows/codepilot-tests.yml) validates the backend, browser JavaScript, integration behavior, and supported Python/Node combinations.
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

Use the [repository health audit](docs/repository-health-audit-2026-11-01.md) as historical context only; its dated observations must not be mistaken for today's live state. Refresh it after a new audit.

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
