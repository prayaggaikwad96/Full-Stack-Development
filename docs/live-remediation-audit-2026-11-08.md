# Live repository remediation audit — 2026-11-08

## Scope

Live read-only inspection of GitHub repository state, plus documentation and PR-metadata corrections on a dedicated audit branch. This report does not claim that local Windows worktrees are synchronized.

## Repository identity

- Repository: `prayaggaikwad96/Full-Stack-Development`
- Default branch: `main`
- Visibility: public
- Connected account: `prayaggaikwad96`
- Connected repository permission snapshot: admin, maintain, push, pull, triage
- Audit branch: `docs/live-remediation-audit-2026-11-08`

## Primary branch state

| Ref | Current observed SHA |
|---|---|
| `main` | `42b32920dd18a2fadee8f9ec3f4660b775415c15` |
| `Developer` | `50702be32d21c0216a45a2647cd6ebca100a9dda` |
| Merge base | `35ddeabd4303a9a7a2eaf092d0203540f656d450` |

GitHub comparison reports divergence:
- `main`: 15 commits ahead of merge base.
- `Developer`: 2 commits ahead of merge base.
- These are not fast-forward synchronized.

Recursive Git trees at the observed tips:
- `main`: 592 file blobs.
- `Developer`: 1,118 file blobs.
- 539 paths exist only on `Developer`.
- 13 paths exist only on `main`.
- 4 shared paths have differing blob contents.

The four differing shared paths are:
1. `.github/workflows/nested-tree-audit.yml`
2. `Full-Stack-Development/Prayag Gaikwad/Prayag Gaikwad CSS/Practice/3 Login Page.html`
3. `projects/codepilot-free/app.py`
4. `projects/codepilot-free/tests/test_app.py`

The Developer-only material includes files in both the canonical `Prayag Gaikwad/` root and a separate top-level CSS learning folder. The README says new work belongs in `Prayag Gaikwad/` and the legacy nested copy must not be overwritten automatically.

## Open pull requests

### PR #33 — preserve learning material

- Open, draft.
- Head: `fix/preserve-developer-learning-content-2026-11-07`
- Head SHA: `11dea3eb7c53aee1019c518d86cf128a493f13b4`
- The PR metadata lists 531 changed files, 28,176 additions and zero deletions.
- PR body now explicitly identifies the 539/13/4 baseline comparison, eight omitted source-only paths requiring exact-SHA verification, 370 same-path canonical/nested pairs with differing hashes, and four conflicts.
- The PR remains draft. Successful CI does not replace file-level provenance review or human approval.

### PR #34 — previous audit report

- Open, ready for review.
- Previous body claimed 24 branches. That count is stale relative to the recent live branch listing and pagination state.
- A current audit update has been posted to its conversation. Complete branch pagination before publishing a final branch count.

### PR #35 — synchronization proposal

- Open, draft.
- Proposes merging `main` into `Developer`.
- Current metadata reports 549 changed files, 1,223 additions and 27,851 deletions.
- Keep draft and do not merge. This proposal would remove substantial content from `Developer`.

## Branch inventory caution

A live branch-search page returned 20 branches and a pagination cursor. The previous 24-branch assertion is not certified by the current partial page. Do not delete or classify branches using an incomplete inventory.

The resolvable historical snapshots are older than their corresponding primary branches; they remain recovery points and are preserved pending path-level recoverability review. Two earlier candidate names ending in `backup-*-latest-2026-10-30` returned 404 and are not current resolvable refs.

## CI evidence

Latest inspected successful workflow runs:
- `main` at `42b32920...`: repository consistency audit, CodeQL, CodePilot tests, root gitignore validation.
- `Developer` at `50702be3...`: repository consistency, nested-tree audit, gitignore validation, CodeQL and CodePilot tests via workflow_dispatch.

These are point-in-time observations. Re-run all applicable checks on exact proposed heads following code or workflow changes.

## Security and repository governance

Observed configuration on `main` includes:
- Dependabot weekly GitHub Actions updates.
- CodeQL workflow for Actions, JavaScript/TypeScript and Python.
- CODEOWNERS.
- SECURITY.md.
- Pull-request template.
- Read-only redundant-branch audit workflow.

The repository rulesets endpoint returned an empty list during the preceding audit. Branch-protection read endpoints returned HTTP 403 to the installed GitHub integration. This means protection could not be inspected through that connection; it does not prove protection is absent. Secret-scanning, push-protection, Dependabot alert inventory and CodeQL alert inventory remain unverified.

Automatic deletion of merged branches was reported disabled by the prior audit; enable only after verifying that recovery refs and meaningful history are retained.

## Local-machine verification required

Two Windows worktrees have been used. GitHub cannot establish that either working tree is clean, that untracked files are backed up, or that local-only commits have been pushed.

Before reconciliation, on both PCs:
1. Confirm the actual repository root, remotes and branch tracking configuration.
2. Record current branch, pushRemote, staged/unstaged/untracked status, ahead/behind counts and recent graph.
3. Fetch all remotes without merging or rebasing.
4. Create Git bundle backups of all refs, plus a separate copy of untracked work.
5. Verify bundle integrity and test restore into a fresh directory.
6. Compare local commit sets and file trees before any merge.

## Remediation decisions

- Preserve `main` and `Developer`.
- Keep PR #33 and PR #35 open and in draft.
- Keep PR #34 open for audit review; refresh its branch-count statement before merging.
- Preserve all recovery refs until each snapshot is independently proven redundant and recoverable.
- Do not use force-push, hard reset, destructive clean, unrelated-history merge or bulk directory overwrite.
- Only reconcile primary branches through a new, reviewed diff after local backups and content provenance are verified.

## Work completed in this audit

- Created this dedicated audit branch from the observed `main` tip.
- Corrected PR #33 body to remove stale certainty around omitted paths and to state explicit merge gates.
- Posted current live-state correction to PR #34's conversation.
- Posted explicit keep-draft/no-merge safety guidance to PR #35's conversation.
- No primary branch refs were moved.
- No branch or recovery ref was deleted.
- No pull request was merged or closed.
