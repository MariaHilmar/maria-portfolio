# Sincronizar docs do hub para o site

Copia `docs/` da raiz para `web/public/docs/` (case study, competências, deploy).

```powershell
.\scripts\sync-docs.ps1
```

Depois do merge em `docs/portfolio-hub`, a Vercel publica automaticamente (integração Git).

Fallback manual: ver [`docs/deploy.md`](../docs/deploy.md).
