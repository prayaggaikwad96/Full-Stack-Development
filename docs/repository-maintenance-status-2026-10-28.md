# Repository maintenance status — 2026-10-28

## Verified remote state
- `main` and `Developer` both point to `72ec6c01ebd2e72227163cbf7ea79f5c6265b376` after the repository consistency workflow was committed to `main` and `Developer` was fast-forwarded without force.
- All 11 known pull requests are closed; latest live listing showed no open pull requests.
- `.github/workflows/repository-consistency.yml` was added. It checks exact `main` / `Developer` SHA equality, required repository hygiene files, CodePilot syntax and unit tests, and explicitly notes the archive's independent history.
- The intentional CodePilot archive remains divergent with 36 commits not reachable from `main`; preserve it as a recovery point.
- `docs/github-profile-readme` is 2 commits ahead / 32 behind `main`; `profile/readme-final` is 1 ahead / 27 behind. Their histories diverge. They were not deleted because the connected GitHub tool lacks a delete-ref operation.
- `chore/github-recommendations-2026-10-28` is 9 commits ahead / 7 behind. It was not deleted because the connected GitHub tool lacks a delete-ref operation and its unique commits should be reviewed before deletion.
- Neither `main` nor `Developer` currently has branch protection enabled, and the repository rulesets endpoint returns an empty list. The connected GitHub tool has no branch protection / ruleset write operation.
- The new workflow is committed but no run/status was returned immediately after the commit; its CI execution is pending/not yet confirmed. Do not report it as passed until Actions reports success.
- A local Windows working tree cannot be verified through this remote connection.

## Remaining manual GitHub actions
1. In Settings → Rules → Rulesets (or Settings → Branches), configure protections for `main`: require pull requests, require the checks that exist, block force pushes, and block deletion. Consider whether `Developer` needs the same protections.
2. Delete the two README branches only after local refs and backups have been checked; do not delete the CodePilot archive.
3. Review `chore/github-recommendations-2026-10-28` and remove it only after its merged content/history and any use of it as a reference is confirmed.
4. On the Windows checkout, inspect `git status --short --branch`, fetch, confirm backups, and compare local `main` / `Developer` before any reset or checkout action.
