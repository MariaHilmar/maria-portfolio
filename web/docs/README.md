# Sincronizar docs do hub para o site

Copia `docs/` da raiz para `web/public/docs/` (case study, competências, deploy).

```powershell
.\scripts\sync-docs.ps1
```

Depois, se o site estiver em produção:

```powershell
cd web
vercel deploy --prod --yes
```
