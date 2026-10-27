# Read-only audit for both Windows repositories plus normalized tree comparison.
# Git repository state is inspected only. The only file written is a CSV report in $env:TEMP.
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
    Write-Host "This script does not change tracked files, branches, commits, or remotes."
} catch {
    Write-Error "Tree comparison could not complete: $($_.Exception.Message)"
}

Write-Host "`n===== END AUDIT =====" -ForegroundColor Cyan
