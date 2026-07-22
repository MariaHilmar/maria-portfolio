$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$hooksSource = Join-Path $repoRoot ".githooks"
$hooksTarget = Join-Path $repoRoot ".git\hooks"

if (-not (Test-Path $hooksSource)) {
  throw "Pasta .githooks nao encontrada em $repoRoot"
}

Get-ChildItem -Path $hooksSource -File | ForEach-Object {
  $destination = Join-Path $hooksTarget $_.Name
  Copy-Item -Path $_.FullName -Destination $destination -Force
}

Write-Host "Git hooks instalados em $hooksTarget"
