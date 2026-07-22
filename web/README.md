# Site do portfólio (Astro)

Vitrine estática do repositório `maria-portfolio`. Conteúdo alinhado às Fases 0-3 (posicionamento, case study e competências).

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

**Produção:** https://mariahilmar.vercel.app

Deploy automático via **integração Git da Vercel** após merge em `docs/portfolio-hub` (mesmo padrão dos demais projetos web).

Configuração e fallback manual: [`../docs/deploy.md`](../docs/deploy.md).
