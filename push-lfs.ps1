# Config
$LFS_THRESHOLD_MB = 50  # files larger than this go to LFS
$COMMIT_MSG = "Add large files via LFS"

if (-not (Get-Command git-lfs -ErrorAction SilentlyContinue)) {
    Write-Error "git-lfs not found. Install it first: winget install GitHub.GitLFS"
    exit 1
}

git lfs install | Out-Null

$threshold = $LFS_THRESHOLD_MB * 1MB
$largeFiles = Get-ChildItem -Recurse -File |
    Where-Object {
        $_.FullName -notmatch '\\\.git\\' -and
        $_.Length -gt $threshold
    }

if (-not $largeFiles) {
    Write-Host "No files over ${LFS_THRESHOLD_MB}MB found." -ForegroundColor Yellow
    exit 0
}

Write-Host "Found $($largeFiles.Count) large file(s):" -ForegroundColor Cyan
$largeFiles | ForEach-Object { Write-Host "  $($_.Name) ($([math]::Round($_.Length/1MB, 1)) MB)" }

$extensions = $largeFiles | ForEach-Object { $_.Extension } | Sort-Object -Unique
foreach ($ext in $extensions) {
    if ($ext) {
        Write-Host "Tracking *$ext with LFS..." -ForegroundColor Green
        git lfs track "*$ext"
    }
}

$noExt = $largeFiles | Where-Object { -not $_.Extension }
foreach ($f in $noExt) {
    $rel = Resolve-Path -Relative $f.FullName
    git lfs track $rel
}

git add .gitattributes

foreach ($f in $largeFiles) {
    $rel = Resolve-Path -Relative $f.FullName
    Write-Host "Staging: $rel" -ForegroundColor DarkCyan
    git add $rel
}

$status = git status --porcelain
if ($status) {
    git commit -m $COMMIT_MSG
    git push
    Write-Host "Done. Files pushed via LFS." -ForegroundColor Green
} else {
    Write-Host "Nothing to commit — files may already be tracked." -ForegroundColor Yellow
}