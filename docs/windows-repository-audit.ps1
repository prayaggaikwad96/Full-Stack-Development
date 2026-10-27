# Read-only audit for both Windows repositories plus normalized tree comparison.
# Run from PowerShell on the Windows machine that owns the repositories.
# Does not fetch/update refs, change config/remotes, switch branches, commit, or push.
# The only file written is the CSV comparison report in $env:TEMP.
$ErrorActionPreference = "Continue"
$script:auditFailures = New-Object System.Collections.Generic.List[string]
$parent = "C:\Prayag Gaikwad"
$child = Join-Path $parent "Full-Stack-Development"

function Invoke-GitReadOnly([string]$RepoPath, [string[]]$GitArgs, [string]$Label) {
    Write-Host ("-- {0} --" -f $Label) -ForegroundColor DarkCyan
    $output = & git -C $RepoPath @GitArgs 2>&1
    $exitCode = $LASTEXITCODE
    if ($output) { $output | ForEach-Object { Write-Host $_ } }
    if ($exitCode -ne 0) {
        $message = "Git command failed (exit $exitCode) in '$RepoPath': git $($GitArgs -join ' ')"
        Write-Host $message -ForegroundColor Red
        $script:auditFailures.Add($message)
    }
    return $output
}

foreach ($repoPath in @($parent, $child)) {
    Write-Host "`n===== REPOSITORY: $repoPath =====" -ForegroundColor Cyan
    if (-not (Test-Path -LiteralPath $repoPath -PathType Container)) {
        $message = "Repository path missing: $repoPath"
        Write-Host $message -ForegroundColor Red
        $script:auditFailures.Add($message)
        continue
    }

    Invoke-GitReadOnly $repoPath @("rev-parse", "--show-toplevel") "Git root"
    Invoke-GitReadOnly $repoPath @("rev-parse", "--is-inside-work-tree") "Worktree check"
    Invoke-GitReadOnly $repoPath @("status", "--short", "--branch") "Working-tree summary"
    Write-Host "-- Remotes configured locally --"
    Invoke-GitReadOnly $repoPath @("remote", "-v") "Remote URLs"
    Write-Host "-- Live branch refs on origin (read-only; does not update local refs) --"
    Invoke-GitReadOnly $repoPath @("ls-remote", "--heads", "origin") "Live origin heads"
    Write-Host "-- Existing local remote-tracking refs (may be stale) --"
    Invoke-GitReadOnly $repoPath @("for-each-ref", "--format=%(refname:short) %(objectname)", "refs/remotes/origin") "Local origin-tracking refs"
    Invoke-GitReadOnly $repoPath @("branch", "-vv") "Local branches and tracking state"
    Invoke-GitReadOnly $repoPath @("submodule", "status") "Submodule state"
    Invoke-GitReadOnly $repoPath @("log", "-1", "--oneline", "--decorate") "Latest local commit"
    Invoke-GitReadOnly $repoPath @("status", "--porcelain=v1", "--untracked-files=all") "All dirty/untracked paths"
}

function Get-FileMap([string]$Root) {
    $map = @{}
    if (-not (Test-Path -LiteralPath $Root -PathType Container)) {
        throw "Comparison directory does not exist: $Root"
    }
    $rootFull = [System.IO.Path]::GetFullPath($Root).TrimEnd([System.IO.Path]::DirectorySeparatorChar) + [System.IO.Path]::DirectorySeparatorChar
    Get-ChildItem -LiteralPath $Root -File -Recurse -Force | ForEach-Object {
        $rel = $_.FullName.Substring($rootFull.Length).Replace([System.IO.Path]::DirectorySeparatorChar, [char]'/')
        $map[$rel] = $_.FullName
    }
    return $map
}

function Get-BytesHash([byte[]]$Bytes) {
    $alg = [System.Security.Cryptography.SHA256]::Create()
    try {
        return ([System.BitConverter]::ToString($alg.ComputeHash($Bytes))).Replace('-', '').ToLowerInvariant()
    } finally {
        $alg.Dispose()
    }
}

function Normalize-LineEndings([byte[]]$Bytes) {
    $stream = New-Object System.IO.MemoryStream
    try {
        for ($i = 0; $i -lt $Bytes.Length; $i++) {
            if ($Bytes[$i] -eq 13) {
                $stream.WriteByte(10)
                if (($i + 1) -lt $Bytes.Length -and $Bytes[$i + 1] -eq 10) {
                    $i++
                }
            } else {
                $stream.WriteByte($Bytes[$i])
            }
        }
        return ,$stream.ToArray()
    } finally {
        $stream.Dispose()
    }
}

function Is-Utf8Text([byte[]]$Bytes) {
    if ($Bytes -contains 0) { return $false }
    try {
        $decoder = New-Object System.Text.UTF8Encoding($false, $true)
        $null = $decoder.GetString($Bytes)
        return $true
    } catch {
        return $false
    }
}

$canonicalRoot = Join-Path $parent "Prayag Gaikwad"
$nestedRoot = Join-Path $child "Prayag Gaikwad"
Write-Host "`n===== NORMALIZED TREE COMPARISON =====" -ForegroundColor Cyan
Write-Host "Canonical: $canonicalRoot"
Write-Host "Nested:    $nestedRoot"

try {
    $canonical = Get-FileMap $canonicalRoot
    $nested = Get-FileMap $nestedRoot
    $allPaths = @($canonical.Keys + $nested.Keys | Sort-Object -Unique)
    $rows = New-Object System.Collections.Generic.List[object]

    foreach ($rel in $allPaths) {
        $cPath = $canonical[$rel]
        $nPath = $nested[$rel]
        $status = ""
        $cHash = ""
        $nHash = ""
        $cSize = $null
        $nSize = $null

        if (-not $cPath) {
            $status = "nested-only"
            $nBytes = [System.IO.File]::ReadAllBytes($nPath)
            $nHash = Get-BytesHash $nBytes
            $nSize = $nBytes.Length
        } elseif (-not $nPath) {
            $status = "canonical-only"
            $cBytes = [System.IO.File]::ReadAllBytes($cPath)
            $cHash = Get-BytesHash $cBytes
            $cSize = $cBytes.Length
        } else {
            $cBytes = [System.IO.File]::ReadAllBytes($cPath)
            $nBytes = [System.IO.File]::ReadAllBytes($nPath)
            $cHash = Get-BytesHash $cBytes
            $nHash = Get-BytesHash $nBytes
            $cSize = $cBytes.Length
            $nSize = $nBytes.Length

            if ($cHash -eq $nHash) {
                $status = "identical"
            } elseif ((Is-Utf8Text $cBytes) -and (Is-Utf8Text $nBytes)) {
                $cNorm = Normalize-LineEndings $cBytes
                $nNorm = Normalize-LineEndings $nBytes
                if ((Get-BytesHash $cNorm) -eq (Get-BytesHash $nNorm)) {
                    $status = "line-ending-only"
                } else {
                    $status = "content-different"
                }
            } else {
                $status = "binary-different"
            }
        }

        $rows.Add([pscustomobject]@{
            RelativePath = $rel
            Status = $status
            CanonicalBytes = $cSize
            NestedBytes = $nSize
            CanonicalSHA256 = $cHash
            NestedSHA256 = $nHash
        })
    }

    $reportPath = Join-Path $env:TEMP "nested-tree-normalized-comparison.csv"
    $rows | Export-Csv -LiteralPath $reportPath -NoTypeInformation -Encoding UTF8
    Write-Host "`n===== COMPARISON SUMMARY =====" -ForegroundColor Cyan
    $rows | Group-Object Status | Sort-Object Name | ForEach-Object {
        Write-Host ("{0,-24} {1,6}" -f $_.Name, $_.Count)
    }
    Write-Host "Full per-file report: $reportPath"
    Write-Host "No tracked files, refs, config, branches, commits, or remotes have been changed by this script."
} catch {
    $message = "Tree comparison could not complete: $($_.Exception.Message)"
    Write-Host $message -ForegroundColor Red
    $script:auditFailures.Add($message)
}

Write-Host "`n===== AUDIT RESULT =====" -ForegroundColor Cyan
if ($script:auditFailures.Count -gt 0) {
    Write-Host ("INCOMPLETE: {0} audit error(s) were detected." -f $script:auditFailures.Count) -ForegroundColor Red
    $script:auditFailures | ForEach-Object { Write-Host (" - {0}" -f $_) -ForegroundColor Red }
    Write-Host "Resolve reported path, Git, authentication, or remote errors before trusting the comparison."
    exit 1
}
Write-Host "Audit completed without Git-command or comparison errors." -ForegroundColor Green
Write-Host "Interpret dirty paths, live origin SHAs versus local remote-tracking SHAs, ahead/behind, and file-level differences before any repair."
Write-Host "`n===== END AUDIT =====" -ForegroundColor Cyan
