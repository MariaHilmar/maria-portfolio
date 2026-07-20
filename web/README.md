# Site do portfólio (Astro)

Vitrine estática do hub `git-portfolio`. Conteúdo alinhado às Fases 0-3 (posicionamento, case study e competências).

## Pré-requisitos

- Node.js 18+
- npm

## Desenvolvimento local

```powershell
cd web
npm install
npm run dev
```

Abra a URL indicada no terminal (geralmente http://localhost:4321).

## Build

```powershell
npm run build
npm run preview
```

Saída estática em `dist/`.

## Conteúdo

- Página única: `src/pages/index.astro`
- Docs espelhados em `public/docs/` (case study e competências)
- Fontes: Syne (display) + Source Sans 3 (corpo)

## Deploy

**Produção:** https://mariahilmar-portfolio.vercel.app

```powershell
vercel deploy --prod --yes
```

Detalhes: [`../docs/deploy.md`](../docs/deploy.md).
