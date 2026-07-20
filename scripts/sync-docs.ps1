$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $PSScriptRoot
$source = Join-Path $root "docs"

Write-Host "Docs fonte: $source"
Write-Host "O site Astro le os arquivos em docs/ no build (src/pages/docs/[slug].astro)."
Write-Host "Nao e mais necessario copiar para web/public/docs."

# Remove copias antigas que serviam Markdown cru sem layout
$legacy = Join-Path $root "web\public\docs"
if (Test-Path $legacy) {
  Remove-Item $legacy -Recurse -Force
  Write-Host "Removido: web/public/docs (evita URLs .md sem design)"
}

Write-Host "OK - edite maria-portfolio/docs/*.md e rode npm run build em web/"
