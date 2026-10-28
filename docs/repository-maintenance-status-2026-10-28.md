# Repository maintenance status — 2026-10-28 (updated)

## Confirmed remote state
- `main` and `Developer` are exactly synchronized at the latest recorded commit. The repository consistency audit checks this on pushes, pull requests, manual dispatch, and a weekly schedule.
- The initial run of the repository consistency audit failed because Python's test discovery did not include `projects/codepilot-free` on `PYTHONPATH`. The workflow was corrected to set `PYTHONPATH=projects/codepilot-free` for the test command. The corrected run is currently in progress; do not mark it successful until GitHub Actions reports a successful conclusion.
- All 11 recorded pull requests are closed, and the latest PR listing reports zero open pull requests.
- The CodePilot archive branch is intentionally retained. It remains divergent with 36 commits not reachable from `main`; do not delete it.
- `docs/github-profile-readme` and `profile/readme-final` remain divergent (respectively 2 and 1 commits ahead of `main`). Their README file may be superseded, but their unique commit history should be checked before deletion. No deletion was performed.
- `chore/github-recommendations-2026-10-28` remains divergent (9 commits ahead of `main`) even though its PR was merged. It has not been deleted.
- Current branch listing reports `main` and `Developer` as unprotected; rulesets list is empty. The available connected GitHub actions support reading rulesets but do not expose writing branch protection/rulesets or deleting refs.
- Local Windows checkout cleanliness and backup status cannot be proven by remote API actions.

## Remaining work
1. Confirm the corrected repository consistency workflow passes in Actions.
2. Use GitHub Settings → Branches / Rulesets to protect `main` with pull-request requirements, existing appropriate checks, block force-pushes, and block deletions. Decide separately whether to protect `Developer`.
3. Delete the README branches only after checking local branches and backups. Review the maintenance branch before any deletion. Preserve the CodePilot archive.
4. Locally, run `git status --short --branch`, fetch, confirm backups, and only then synchronize the Windows checkout.
