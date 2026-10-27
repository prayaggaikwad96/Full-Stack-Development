# READ-ONLY audit for both Windows working copies. No files or refs are changed.
$ErrorActionPreference = "Continue"
$parent = "C:\Prayag Gaikwad"
$child = Join-Path $parent "Full-Stack-Development"

foreach ($repoPath in @($parent, $child)) {
    Write-Host "`n===== REPOSITORY: $repoPath =====" -ForegroundColor Cyan
    if (-not (Test-Path $repoPath)) {
        Write-Host "PATH MISSING"
        continue
    }

    git -C $repoPath rev-parse --show-toplevel 2>&1
    git -C $repoPath rev-parse --is-inside-work-tree 2>&1
    git -C $repoPath status --short --branch 2>&1
    git -C $repoPath remote -v 2>&1
    git -C $repoPath branch -vv 2>&1
    git -C $repoPath submodule status 2>&1
    git -C $repoPath log -1 --oneline --decorate 2>&1
    Write-Host "`n-- Worktree status porcelain --"
    git -C $repoPath status --porcelain=v1 --untracked-files=all 2>&1
}

Write-Host "`n===== END READ-ONLY AUDIT =====" -ForegroundColor Cyan
