$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
$source = Join-Path $root "docs"
$target = Join-Path $root "web\public\docs"

New-Item -ItemType Directory -Force -Path $target | Out-Null

$files = @(
  "case-study-juris-sync.md",
  "competencias.md",
  "deploy.md"
)

foreach ($file in $files) {
  $from = Join-Path $source $file
  if (-not (Test-Path $from)) {
    Write-Warning "Arquivo ausente: $from"
    continue
  }
  Copy-Item $from (Join-Path $target $file) -Force
  Write-Host "Copiado: $file"
}

Write-Host "Docs sincronizados em web/public/docs/"
