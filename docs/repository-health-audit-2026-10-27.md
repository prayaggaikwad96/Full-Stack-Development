# Repository health audit — 2026-10-28

## Scope and confidence
This document separates live remote GitHub checks from checks that must run on the Windows host. Do not treat a GitHub branch comparison or CI workflow as evidence that a local Windows working tree is clean or synchronized.

## Verified remote state
- Repository: `prayaggaikwad96/Full-Stack-Development`; default branch: `main`.
- At the last verified synchronization checkpoint, `main` and `Developer` were identical with 0 commits ahead and 0 behind. The current live SHA is intentionally verified from the branches API rather than embedded here, because each documentation commit changes that SHA.
- The only remaining remote branches were `main`, `Developer`, and `archive/codepilot-feature-history-before-sync-2026-10-27` (archive tip `6c68a09756d30a004f2519dab06c9da7494005c8`).
- `feat/codepilot-free-app` was deleted after verifying its tip was already contained in `main`; its application/tests had been integrated through [merged PR #8](https://github.com/prayaggaikwad96/Full-Stack-Development/pull/8).
- The older `backup/legacy-tree-before-cleanup-2026-10-27` ref was also removed after the guarded cleanup verified its tip was an ancestor of `main`. The independent CodePilot archive was preserved because it contains unique history.
- No open pull requests were present at the latest listing. Closed historical PRs remain available as audit records.

## Latest completed CI checkpoint
All four workflows on commit `ad8711cc73ffecf2a09984592987962c53997f29` completed successfully:
- [CodePilot tests — Python 3.10 and 3.12](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40568543373)
- [Nested learning-tree audit](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40568543354)
- [Root .gitignore validation](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40568543792)
- [Guarded redundant-branch cleanup](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40568543386)

## Nested learning-tree audit result
The latest uploaded [comparison report artifact](https://github.com/prayaggaikwad96/Full-Stack-Development/actions/runs/40568415162) compared `Prayag Gaikwad/` with `Full-Stack-Development/Prayag Gaikwad/`, normalizing only CRLF/CR line endings for UTF-8 text and comparing binary files byte-for-byte:
- 527 file paths compared.
- 160 byte-identical files.
- 364 files differed only in line endings.
- 0 substantive UTF-8 text content differences.
- 0 binary differences.
- 1 canonical-only empty placeholder: `Prayag Gaikwad CSS/Projects/.gitkeep.txt`.
- 2 nested-only empty placeholders: `Prayag Gaikwad CSS/Projects/Advanced Projects/.gitkeep.txt` and `Prayag Gaikwad CSS/Projects/Intermediate Projects/.gitkeep.txt`.

These differences are empty directory placeholders and line-ending variations, not substantive file-content mismatches. Keep this report as a point-in-time result; a later run supersedes it.

## Branch-cleanup guard
The workflow at [cleanup-redundant-branches.yml](../.github/workflows/cleanup-redundant-branches.yml) only deletes explicitly listed legacy refs when their tips are ancestors of `main`. It preserves the unique CodePilot history archive. Review the workflow before expanding its deletion list.

## Windows local repositories — not yet verified
GitHub-hosted Actions cannot inspect unsaved or untracked files in the user's Windows checkout. The read-only audit script [`docs/windows-repository-audit.ps1`](windows-repository-audit.ps1) is intended to run locally against both `C:\\Prayag Gaikwad` and `C:\\Prayag Gaikwad\\Full-Stack-Development`. Its output has not been supplied for this audit, so local status, remotes, tracking state, submodules, and working-tree differences remain unverified.

Run the following on the Windows PC from PowerShell (the script itself does not switch branches, commit, push, or change remotes; it writes its CSV comparison report under `%TEMP%`):

```powershell
& "C:\\Prayag Gaikwad\\Full-Stack-Development\\docs\\windows-repository-audit.ps1"
```

Review all output before attempting repairs. Do not run broad resets, force-pushes, branch deletions, or automated overwrites until any dirty or unique local files have been identified and backed up.

## Maintenance note
This report is a snapshot and will become stale after later commits. For current remote branch alignment, use the live [branches page](https://github.com/prayaggaikwad96/Full-Stack-Development/branches), compare `main` with `Developer`, and inspect the [Actions dashboard](https://github.com/prayaggaikwad96/Full-Stack-Development/actions). Never infer local synchronization from remote branch alignment alone.
