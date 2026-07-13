param(
    [string]$CompilerId = "IntelLLVM",
    [string]$CompilerVersion = "local"
)

$ErrorActionPreference = "Stop"

$generatedDir = $PSScriptRoot
$projectDir = Resolve-Path (Join-Path $generatedDir "..")
$repoRoot = Resolve-Path (Join-Path $projectDir "..\..")
$template = Join-Path $repoRoot "SWATPLUS\swatplus\src\main.f90.in"
$output = Join-Path $generatedDir "main.f90"

if (-not (Test-Path -LiteralPath $template)) {
    throw "Cannot find main template: $template"
}

$sourceRevision = "local"
$gitlink = git -C $repoRoot ls-files -s SWATPLUS/swatplus 2>$null
if ($LASTEXITCODE -eq 0 -and $gitlink -match "160000\s+([0-9a-f]{7,40})") {
    $sourceRevision = $Matches[1]
}

$today = Get-Date -Format "yyyy-MM-dd"
$year = Get-Date -Format "yyyy"
$iso = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$hostSystem = [System.Environment]::OSVersion.Platform.ToString()

$text = Get-Content -LiteralPath $template -Raw
$text = $text.Replace("@TODAY@", $today)
$text = $text.Replace("@YEAR@", $year)
$text = $text.Replace("@SWAT_VERSION@", $sourceRevision)
$text = $text.Replace("@CMAKE_Fortran_COMPILER_ID@", $CompilerId)
$text = $text.Replace("@CMAKE_Fortran_COMPILER_VERSION@", $CompilerVersion)
$text = $text.Replace("@ISO@", $iso)
$text = $text.Replace("@CMAKE_HOST_SYSTEM_NAME@", $hostSystem)

$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($output, $text, $utf8NoBom)

Write-Host "Generated $output"
