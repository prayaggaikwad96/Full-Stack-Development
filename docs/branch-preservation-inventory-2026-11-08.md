# Branch preservation inventory — 2026-11-08

Repository: https://github.com/prayaggaikwad96/Full-Stack-Development

This report is a read-only GitHub compare snapshot against `main` at 42b32920dd18a2fadee8f9ec3f4660b775415c15. It classifies ancestry and preservation status, not local workstation recoverability.

| Branch | Compare status | Ahead | Behind | Merge base | Action |
|---|---:|---:|---:|---|---|
| `Developer` | diverged | 2 | 15 | `35ddeabd4303a9a7a2eaf092d0203540f656d450` | Primary branch; preserve |
| `archive/codepilot-feature-history-before-sync-2026-10-27` | diverged | 34 | 301 | `d55b6b35d2e3f1e0ebf320379b72425bef15caa1` | Preserve CodePilot implementation |
| `docs/github-profile-readme` | behind | 0 | 171 | `20cba506d773cc4047a92bd80b22a6663e9e745a` | Review lineage; no deletion |
| `docs/github-recommendations-2026-10-29` | diverged | 3 | 370 | `1864a9f5c02de48976ea2ac5a8e5337ec4215275` | Preserve document |
| `docs/remote-audit-2026-10-30` | diverged | 7 | 303 | `66173f2547d600baa62d0650f238d70d554585b9` | Preserve audit history |
| `docs/repository-audit-2026-11-08` | ahead | 1 | 0 | `42b32920dd18a2fadee8f9ec3f4660b775415c15` | Open documentation PR #34 |
| `fix/preserve-developer-learning-content-2026-11-07` | ahead | 10 | 0 | `42b32920dd18a2fadee8f9ec3f4660b775415c15` | Open draft PR #33; review before merge |
| `prayaggaikwad96-beginner-friendly-contribution` | diverged | 2 | 15 | `35ddeabd4303a9a7a2eaf092d0203540f656d450` | Review CodePilot app/test |
| `prayaggaikwad96-complete-github-account-audit` | diverged | 1 | 18 | `86e4b3069065d943d4bc1c83a99e94cb6f283d33` | Review CI workflow change |
| `prayaggaikwad96-patch-1` | diverged | 3 | 15 | `35ddeabd4303a9a7a2eaf092d0203540f656d450` | Contains learning-path removals; preserve |
| `prayaggaikwad96-repository-synchronization-6a0` | ahead | 1 | 0 | `42b32920dd18a2fadee8f9ec3f4660b775415c15` | Closed unmerged PR #32; review workflow diffs |
| `safety/backup-developer-2026-10-30` | behind | 0 | 82 | `204748099731c3aeb04963e6d8957dcd569daf62` | Retain historical snapshot |
| `safety/backup-developer-latest-2026-10-30` | behind | 0 | 81 | `33eb13cf83db41825e3184d4bb4314d0a4750630` | Retain historical snapshot |
| `safety/backup-main-2026-10-30` | behind | 0 | 311 | `922c98f781cc6c0060c861532dfcc73576f9f571` | Retain historical snapshot |
| `safety/backup-main-current-2026-10-30` | behind | 0 | 301 | `e34111048e9081df982fb71c474a6ea608b56091` | Retain historical snapshot |
| `safety/backup-main-latest-2026-10-30` | behind | 0 | 303 | `66173f2547d600baa62d0650f238d70d554585b9` | Same SHA as pre-pr13 backup; still retain |
| `safety/backup-main-pre-merge-candidate-2026-10-30` | behind | 0 | 304 | `fce73fdf1fb848721a756cb64c1e74e0681a816c` | Retain historical snapshot |
| `safety/backup-main-pre-pr13-2026-10-30` | behind | 0 | 303 | `66173f2547d600baa62d0650f238d70d554585b9` | Same SHA as latest backup; do not delete yet |
| `safety/backup-main-pre-reconcile-2026-10-30` | behind | 0 | 306 | `34d203868e609401f1a454203bfefd3f46bb1ac3` | Retain historical snapshot |
| `safety/recovery-snapshot-developer-2026-10-31` | behind | 0 | 81 | `33eb13cf83db41825e3184d4bb4314d0a4750630` | Same SHA as developer-latest backup |
| `safety/recovery-snapshot-main-2026-10-31` | behind | 0 | 290 | `cfa1a6643e3195672cffd2ece576865f302b7bc1` | Retain historical snapshot |
| `sync/main-to-developer-2026-11-07` | ahead | 4 | 0 | `42b32920dd18a2fadee8f9ec3f4660b775415c15` | 300 file differences; preserve pending review |
| `test/codepilot-public-github-import` | diverged | 1 | 7 | `d4d4e3af827e93ac7b3fc007aa82ecec9bf3dda5` | Closed unmerged PR #30; preserve/test cherry-pick review |

## Verified implications

- 24 live branches were inventoried.
- `main` and `Developer` are divergent: 2 commits exist on Developer beyond the merge base and 15 on main.
- The CodePilot archive has 34 commits beyond its merge base and must be retained while history is reviewed.
- PR #33 is a 10-commit preservation proposal and all current checks passed at head 11dea3eb7c53aee1019c518d86cf128a493f13b4. It remains draft because 370 overlapping same-relative-path content variants and four explicit conflicts require path/hash and human review.
- PR #35 proposes main into Developer but its current diff reports 549 changed files, 1,223 additions and 27,851 deletions. A maintainer safety note was added to PR #35; keep it draft and do not merge.
- Some snapshot branch names share the same SHA: backup-main-latest and backup-main-pre-pr13; backup-developer-latest and recovery-snapshot-developer. This is useful deduplication evidence, not permission to delete either ref before local backup verification.
- `prayaggaikwad96-patch-1` contains large deletions from the canonical learning root and remains preserved.

## Repository settings and checks

- GitHub branch API reports `protected: true` for `main` and `Developer`; all other 22 branches report false.
- Detailed protection policy could not be read due to integration HTTP 403. Empty repository rulesets were returned.
- Dependabot is configured weekly for GitHub Actions.
- CodeQL, CodePilot matrix, nested-tree audit and consistency checks are present and passed for the inspected PR #33 head.
- PR #34's checks passed, but its content is documentation-only and its open state remains distinct from a merge.
- Auto-delete of merged branches is disabled. Keep it disabled until branch preservation and local worktree checks finish.

## Not completed / not safe to certify

- Local state on both Windows PCs, including uncommitted and untracked files.
- Independently verified git bundle or mirror backups.
- Full commit-by-commit and blob-by-blob review of every branch.
- 370 path/hash comparisons and four conflict resolutions in PR #33.
- Merge/reconciliation of `main` and `Developer`.
- Detailed required status checks, review/bypass policy, secret scanning, push protection and alert inventories.
- Complete security audit of all active workflows and dependencies.

## Safety outcome

No branch was deleted, no ref was updated, no file was modified, no PR was merged, and no force update was performed by this inventory operation. All 24 refs must remain until the listed verification gates are satisfied.