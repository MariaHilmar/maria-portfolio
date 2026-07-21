$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
$source = Join-Path $root "docs"
$target = Join-Path $root "web\docs"

Write-Host "Docs fonte: $source"
Write-Host "Docs destino (build Vercel): $target"

New-Item -ItemType Directory -Force -Path $target | Out-Null
Get-ChildItem $source -Filter *.md | ForEach-Object {
  Copy-Item $_.FullName (Join-Path $target $_.Name) -Force
  Write-Host "  -> $($_.Name)"
}

# Remove copias antigas que serviam Markdown cru sem layout
$legacy = Join-Path $root "web\public\docs"
if (Test-Path $legacy) {
  Remove-Item $legacy -Recurse -Force
  Write-Host "Removido: web/public/docs (evita URLs .md sem design)"
}

Write-Host "OK - edite maria-portfolio/docs/*.md e rode npm run build em web/"
