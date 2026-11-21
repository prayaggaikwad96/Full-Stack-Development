# GitHub account remediation audit — 2026-11-21

## Scope
Remote audit of the seven repositories accessible to the connected account `prayaggaikwad96`. This report records verified remote state and actions taken during this audit. It does not claim that local worktrees, untracked files, external backups, branch protection settings or every external security alert have been verified.

## Repositories
- `Full-Stack-Development` — default branch `main`
- `Computer-Classes` — default branch `main`
- `virtual` — default branch `main`
- `rea` — default branch `main`
- `altair` — default branch `master`
- `git` — default branch `master`
- `prayaggaikwad96` — default branch `main`

The live repository inventory returned seven repositories, all owned by the authenticated account, with administrator/push permissions reported by the connector.

## Changes completed
### Full-Stack-Development
- PR #50 merged by squash at commit `1c703e24b07584fd8a0e1935a3654bacfcff825c`.
  - Fixes false successful completion of interrupted Ollama streams.
  - Aligns export/import per-file size limits.
  - Rejects reserved archive manifest path collisions.
  - Rejects normalized duplicate ZIP paths.
  - Exact PR head checked: `770734df7b270827ef658415106158dc3040ee8b`.
  - Exact-head checks observed successful: 8 Python/Node matrix jobs, repository invariants, CodeQL.
- PR #49 merged by squash at commit `bb44f7c2bbd8bb86794359e40c58e3caaf33f236`.
  - Removes invalid CSS `spacing` declarations from three teaching examples and explains margin/padding/gap alternatives.
  - Exact PR head checked: `8e53cff60c5a36e9d64ceb159e90efc8512fc362`.
  - Exact-head matrix, nested-tree audit, invariants and CodeQL checks observed successful.

### Computer-Classes
- PR #10 merged by squash at commit `a0ecfea2c63098e03a537551c9ed2063b79c9abe`.
  - Adds weekly GitHub Actions Dependabot updates and maintenance/security/contribution guidance.
  - Exact PR head checked: `778f0db94617b655e692917758aa4d19c02b4d4c`.
  - CodeQL check observed successful; this PR did not show a broad application test suite, and the repo is a learning archive.

## Open PRs retained
- Full-Stack-Development #35: main-to-Developer synchronization; 72 commits ahead, zero behind at the observed comparison; 112 changed paths in the comparison snapshot (26 modified, 78 added, 3 renamed, 5 removed). Includes learning content, example edits, workflow changes and CodePilot changes. Not merged because file-level educational-content review and local recovery verification remain necessary. After #49/#50 merged, GitHub reports Developer is 72 commits behind main and no Developer-only commits.
- Computer-Classes #10 is now merged; no open PR on this repo from the scanned list.
- virtual #6: CI repair draft; 7 commits ahead and 1 behind, diverged. Exact-head checks observed successful for Test, CodeQL, Provenance, Version Preview, autofix and zizmor; Preview intentionally skipped for downstream fork. Retained as draft because it needs current-base refresh and PR author review.
- git #3: dirname compatibility shim fix; 2 commits ahead and 1 behind, diverged. No check runs observed for exact PR head. Not merged.
- Full-Stack-Development #35, #49 and #50 were the open PRs at the time of initial scan; #49/#50 are now merged. #35 remains open.

## CI / dependency / security inventory
- Full-Stack-Development: CodeQL, Python/Node matrix, repository invariants, gitignore validation, nested-tree comparison, cleanup workflow, Dependabot, SECURITY.md and CONTRIBUTING.md present.
- Computer-Classes: CodeQL, SECURITY.md and CONTRIBUTING.md present; Dependabot configuration added by merged PR #10.
- virtual: CI, release, autofix, CodeQL and zizmor workflows; Renovate configured; root pnpm manifest and lockfile. SECURITY.md not present in inspected root tree. Do not add generic Dependabot alongside Renovate without a dependency ownership decision.
- rea: large project with 35 workflows, CodeQL, Dependabot, SECURITY.md, package manifest and lockfile. Preserve existing release/CI conventions.
- altair: extensive existing workflows, Dependabot, Renovate-related? The tree scan observed Dependabot and 13 workflows; SECURITY.md and CONTRIBUTING.md not present at repository root. The project is a fork of upstream Altair GraphQL; avoid blanket changes.
- git: upstream Git repository fork with six existing CI workflows and SECURITY.md. Do not modify upstream workflow or code except a narrowly scoped tested fix.
- prayaggaikwad96: profile README exists; no workflows or root security/contribution docs inspected.

## Branch and governance cautions
- Full-Stack-Development `Developer` was an ancestor of `main` at the time of post-merge comparison, 72 commits behind and 0 ahead. PR #35 still includes substantial learning content; do not auto-merge merely because the ancestry is fast-forwardable. The connected GitHub integration did not have permission to read branch protection configuration (403). No protection settings were changed.
- Computer-Classes `Developer` diverged from `main`: 1 commit ahead and 7 behind, with a Developer-specific branch-protection document. Do not reset it; compare that document and confirm branch purpose first.
- All repositories have additional branches, including upstream feature work, backup snapshots, audit branches and maintenance branches. Search results were paginated in several repositories; do not treat first page as complete or delete branches by age alone.
- The remote audit cannot validate local Windows worktrees, untracked files, Git bundle backups or restore tests. Preserve all current refs.

## Not completed / external limitations
- Branch protection and ruleset settings: integration endpoint returned 403, so no changes or claims of enforcement.
- Open source project PR refreshes: not performed because existing branch divergence needs an explicit rebase/update workflow and renewed CI.
- External vulnerability alert and secret-scanning dashboards: not verified by supported endpoints.
- No branch deletions, force-pushes, history rewrites, secrets changes, or releases performed.

## Recommended next gates
1. Use GitHub administrator settings directly to verify/protect primary branches and configure required checks by exact job names after testing on all PR types.
2. Review Full-Stack-Development #35 changed learning content against original local work and independent backups; decide canonical directory rules before syncing.
3. Rebase/update virtual #6 and git #3 from current target branches, then rerun full exact-head CI.
4. Add repository-specific security documentation to `virtual` and `altair` only after aligning disclosure links and upstream contribution policy.
5. Review stale/recovery branch inventory across all pages before considering any deletion.
6. Verify local backups and worktrees on the Windows machines.

## Assurance
This is a point-in-time remote audit, not a claim of 100% correctness, complete security certification, or verified workstation synchronization.
