# Cross-device Git push setup

This guide standardizes local Git configuration and authentication for the repositories owned by @prayaggaikwad96. It does not change branch protection, credentials, secrets, commit history, or branch references.

## Scope and guarantees

A successful GitHub account permission check does not prove that a workstation is configured or authenticated. Each device must independently pass the checks below. A push can still be blocked by branch protection, repository rules, network policy, unavailable credentials, or lack of permission.

Use SSH as the preferred transport and Git Credential Manager with HTTPS as a fallback. Do not embed tokens in remote URLs, scripts, or checked-in configuration.

## 1. Install and verify tools

Install current Git for Windows, Git Credential Manager, and GitHub CLI from their official distribution channels. Restart PowerShell after installation.

```powershell
git --version
gh --version
git credential-manager --version
```

## 2. Set global Git identity and safe defaults

Use an email address verified on GitHub; do not guess it.

```powershell
git config --global user.name "Prayag Dilip Gaikwad"
git config --global user.email "YOUR_VERIFIED_GITHUB_EMAIL"
git config --global init.defaultBranch main
git config --global push.autoSetupRemote true
git config --global push.default simple
git config --global fetch.prune true
git config --global pull.ff only
git config --global credential.helper manager
```

Review effective values:

```powershell
git config --global --list --show-origin
```

Do not apply `core.autocrlf` or repository-specific line-ending settings blindly to all projects; follow each project's attributes and conventions.

## 3. Authenticate with HTTPS

```powershell
gh auth login
gh auth setup-git
gh auth status
```

Choose GitHub.com and HTTPS when prompted. Complete the browser/device verification. Never paste a token into chat or commit it to a repository.

## 4. Optional SSH authentication

Create a distinct key on each trusted device. Protect it with a passphrase.

```powershell
ssh-keygen -t ed25519 -C "YOUR_VERIFIED_GITHUB_EMAIL"
Get-Service ssh-agent | Set-Service -StartupType Automatic
Start-Service ssh-agent
ssh-add $env:USERPROFILE\.ssh\id_ed25519
```

Add only the public key from `$env:USERPROFILE\.ssh\id_ed25519.pub` under GitHub Settings → SSH and GPG keys. Keep `id_ed25519` private and backed up only through a secure password-manager workflow, or regenerate a device-specific key. Test:

```powershell
ssh -T git@github.com
```

## 5. Repository remotes and default branches

Use the canonical SSH remote for each repository:

| Repository | Default branch | SSH remote |
| --- | --- | --- |
| Full-Stack-Development | main | git@github.com:prayaggaikwad96/Full-Stack-Development.git |
| Computer-Classes | main | git@github.com:prayaggaikwad96/Computer-Classes.git |
| virtual | main | git@github.com:prayaggaikwad96/virtual.git |
| rea | main | git@github.com:prayaggaikwad96/rea.git |
| altair | master | git@github.com:prayaggaikwad96/altair.git |
| git | master | git@github.com:prayaggaikwad96/git.git |
| prayaggaikwad96 | main | git@github.com:prayaggaikwad96/prayaggaikwad96.git |

In an existing local clone, verify before changing:

```powershell
git remote -v
git remote set-url origin git@github.com:prayaggaikwad96/REPOSITORY.git
git fetch origin --prune
git branch -vv
git ls-remote origin
```

Replace REPOSITORY with the exact repository name. Never change remotes in an unknown or nested worktree without confirming the repository root with `git rev-parse --show-toplevel`.

Set upstream tracking only if the local branch and corresponding remote-tracking ref already exist:

```powershell
git branch --set-upstream-to=origin/DEFAULT_BRANCH DEFAULT_BRANCH
```

Replace both placeholders with the verified branch name (main or master).

## 6. Normal feature branch push workflow

```powershell
git status
git switch -c feature/short-description
git add -A
git diff --cached
git commit -m "feat: describe the change"
git push -u origin HEAD
```

After upstream is set, use `git push` and `git pull --ff-only`. Do not use `--force`, `reset --hard`, or force-with-lease as routine fixes. Do not commit secrets, .env files, private keys, build output, or generated data.

## 7. Machine readiness checks

Run in each clone:

```powershell
git rev-parse --show-toplevel
git status --short --branch
git remote -v
git branch -vv
git ls-remote origin
git fetch origin --prune
gh auth status
```

Then push a small, disposable test branch only if appropriate and delete that test branch only after verifying it is not needed. Do not test by pushing directly to main or master.

## 8. Network fallback and troubleshooting

- If SSH port 22 is blocked, use HTTPS with Git Credential Manager. GitHub also documents SSH over port 443 through `ssh.github.com`; configure it only according to GitHub's current official instructions.
- If HTTPS authentication fails, use `gh auth login` and `gh auth setup-git` rather than embedding a PAT.
- If push is rejected as non-fast-forward, fetch and inspect divergence; integrate intentionally. Do not force-push.
- If a protected branch rejects a direct push, open a pull request and satisfy its current required checks and reviews.
- If access is denied, confirm the authenticated account and repository push permission.

## 9. Repository protection and synchronization

Keep primary branch protection, CI checks, review requirements, and recovery branches. Do not remove branch protection to make pushing easier. Direct pushes to protected branches should remain blocked; use feature branches and pull requests instead. Never merge or synchronize main and Developer solely to make their histories identical. Independently back up important work and test restoration.

## 10. Current account inventory

The connected GitHub account reported push and admin permissions for the seven repositories listed above as of 24 November 2026. This is an account-side snapshot, not a successful push test from any local device.

The Full-Stack-Development branch listing reported main unprotected and Developer protected. Detailed branch protection could not be read through the current integration (HTTP 403). Verify effective branch rules and required check names directly in GitHub repository Settings before relying on enforcement.

## Verification record

For every workstation, record OS/device name, Git version, GitHub CLI version, authentication method (never a token), clone path, remote URL, default branch, upstream, and whether a test feature-branch push succeeded. Never record secrets or private-key material.
