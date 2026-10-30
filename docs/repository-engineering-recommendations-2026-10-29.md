# Repository engineering and synchronization recommendations

Last reviewed: 2026-10-31

This document is a practical maintenance checklist, not a claim that every GitHub setting is enabled. Verify remote state and required checks before each high-risk operation. Local working trees, secrets settings, and administration-only controls may not be observable through the connected integration.

## Live revalidation — 2026-10-31

- Full-Stack-Development PR #14 head `a85b219bba8f65a637e036ae696669d0b3c83f0a` has completed successfully for Repository consistency audit, CodePilot tests, and CodeQL.
- CodeQL run `41066359274` completed with conclusion `success`; its `CodeQL analysis` job also completed successfully.
- Full-Stack-Development `main` and `Developer` remain intentionally unreconciled because the remote comparison is substantially divergent and the required Windows working-tree/backup audit has not been performed through this connection.
- REA fork `main` remains source-history synchronized with upstream `morluto/rea:main` at the previously verified merge relationship; fork CI remains unverified.
- TanStack Virtual PR #1321 has upstream workflow runs in `action_required` state, so upstream tests cannot honestly be marked complete from this connection.
- Altair PR #3341 has upstream workflow runs in `action_required` state; maintainer authorization is required and cannot be supplied by this fork connection.
- Branch protection/rulesets remain unverified or disabled where inspected. No administration write operation for branch protection/rulesets is exposed by the connected GitHub tool.
- Dependabot update configuration is present. Dependabot alert state, secret scanning and push protection remain Settings-level items that cannot be certified from the available integration.
- Windows local synchronization, uncommitted/untracked files, worktrees and offline-backup restoration remain owner-side checks.

## Shared rules for all repositories

- Make changes on a short-lived, purpose-specific branch based on the current default branch.
- Inspect the relevant files, active PRs, upstream behavior, and current CI before editing.
- Keep diffs small and scoped. Do not perform cosmetic refactors, dependency upgrades, or generated-file changes unrelated to the task.
- Add or update regression tests for behavior changes; update the nearest applicable documentation.
- Run the repository's documented checks and report exact commands/results. Clearly identify checks not run or unavailable.
- Treat AI/model output as a proposal, not verification. Require tests, CI, and human review.
- Never commit tokens, private records, real environment files, or credentials. Use least-privilege workflow permissions and pin third-party Actions to reviewed immutable SHAs where practical.
- Do not force-push shared refs, delete recovery branches, close PRs, or merge without comparing exact heads, reviewing unique commits/files, and preserving any unique work.
- For forks, use one canonical upstream PR per contribution. Do not create a second fork PR for the same upstream change.
- Do not claim "fully hardened" until branch rules, security settings, and local state have been independently verified.

## Repository-specific plan

### Full-Stack-Development

- Keep `main` as the publishing source of truth.
- `main` and `Developer` share history but remain diverged. Ahead/behind counts, merge-base SHAs, and branch-tip SHAs are volatile; do not hard-code them in this evergreen checklist. Before any reconciliation, fetch the live refs, record the exact compare output and recovery-ref SHAs in a dated audit, and complete the local Windows audit and unique-commit review. Do not treat `Developer` as a mirror or reset, force-push, or merge it merely to remove divergence.
- Preserve recovery references until local backups and unique commits have been checked.
- Continue CodePilot's existing Python syntax, browser-JavaScript syntax, API integration tests, and Python 3.12–3.15 / Node.js 22 and 24 matrix.
- Confirm exact required status-check names from a real pull-request run before enforcing them in a ruleset.
- Owner-side follow-up: review branch rules/rulesets and secret scanning, push protection, Dependabot alerts and security updates in repository Settings.

### Computer-Classes

- Keep the repository a lightweight learning archive; do not add complex CI just for appearance.
- Keep the README honest about observed contents.
- For new substantive examples, document prerequisites, how to run them, expected output, source/reference and any known limitation.
- Keep private data and secrets out of notes and exercises.

### virtual (fork of TanStack/virtual)

- Keep the relevant TanStack upstream PR as the sole review source of truth; the fork PR that duplicates it remains historical.
- Finish focused virtual-core tests, typecheck, scroll-trace snapshots, Marko E2E, and required upstream CI before requesting merge.
- Preserve the current contribution branch until upstream has accepted or declined the change.
- Do not label the contribution complete while upstream workflows remain `action_required`.

### rea (fork of morluto/rea)

- Treat upstream synchronization as a code-review event, not an administrative fast-forward. Compare merge base, ahead/behind counts, changed files, generated metadata, contracts, dependencies, and test changes.
- Keep historical/superseded contribution branches until each has been compared to current upstream and its unique value assessed.
- Use the existing validation pipeline and report which parts actually ran.
- Fork CI remains unverified until an actual current fork-head workflow run or status is available.

### altair (fork of altair-graphql/altair)

- Keep upstream PR #3341 as the single review source of truth; retain duplicate fork PR history without recreating it.
- Do not replace or weaken upstream security workflows merely to bypass `action_required`.
- Maintainer authorization is required for the blocked upstream workflow runs.
- Use the repository’s existing pnpm, test, Playwright and build scripts for app changes.

### git

- Preserve upstream Git source and documentation; avoid arbitrary code rewrites.
- Prefer research notes, focused upstream issues/PRs, and reproducible documentation fixes.
- Verify provenance and license obligations before adding, removing or relocating copied material.

## Multi-model coding-agent operating contract

1. Planner/researcher: establish the issue, reproduce conditions, inspect current code and upstream, and write acceptance criteria and risk notes. No writes.
2. Implementer: make the smallest patch on a dedicated branch. One agent owns writes for a given change.
3. Test challenger: independently propose edge cases, regression tests and failure paths.
4. Security reviewer: inspect input validation, permissions, secrets/data flow, dependency changes and side effects.
5. CI/human review: run documented checks, capture exact run links and statuses, review the diff, and keep uncertainty visible. Human owner controls approval and merge.

## Synchronization and release checklist

- [ ] Verify repository default branch and exact head SHA.
- [ ] For Full-Stack-Development, use the live GitHub comparison of `main` and `Developer` before every synchronization operation.
- [ ] Verify candidate branch SHA and compare base/head; inspect merge base and unique commits.
- [ ] Check open PRs, duplicate upstream PRs, review threads and workflow/check runs.
- [ ] Review changed files and generated/dependency artifacts.
- [ ] Run tests appropriate to the changed boundary.
- [ ] Confirm CI ran against the exact proposed head.
- [ ] Confirm no unrelated or unpreserved unique work is lost.
- [ ] Review the proposed operation's impact before branch updates, PR closure, or merge.
- [ ] Human maintainer approves the final change.
- [ ] Recheck default-branch/working-tree state after completion.

## Important limitations

The connected GitHub view is not a substitute for a local Windows audit, repository Settings review, upstream maintainer authorization, or a real maintainer decision. Access restrictions prevent the available connection from changing branch-protection/ruleset settings. A successful fetch or mergeable flag does not prove the full test suite passed.
