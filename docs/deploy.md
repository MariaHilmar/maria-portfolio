# Deploy do portfólio

## Site (produção atual)

| Item | Valor |
|------|-------|
| **URL live** | https://mariahilmar-portfolio.vercel.app |
| **Plataforma** | Vercel |
| **Projeto** | `mariahilmar-portfolio` |
| **Escopo atual** | time `situacao-juridica-projects` (conta autenticada no CLI) |
| **Origem** | pasta `web/` (Astro estático) |

### Redeploy (local)

```powershell
cd web
npm run build
vercel deploy --prod --yes
```

Requer [Vercel CLI](https://vercel.com/docs/cli) logado (`vercel login`).

### Variáveis

Nenhuma variável de ambiente é necessária para o site estático na v1.

---

## GitHub Pages (alternativa)

Workflow pronto em [`.github/workflows/deploy-pages.yml`](../.github/workflows/deploy-pages.yml).

Pré-requisitos:

1. Inicializar o hub como repositório Git e publicar (ex.: `MariaHilmar/git-portfolio`)
2. Em **Settings → Pages**, escolher fonte **GitHub Actions**
3. Se o site for em `https://mariahilmar.github.io/git-portfolio/`, ajustar `base` em `web/astro.config.mjs` para `'/git-portfolio/'` e os links absolutos (`/docs/...`) para respeitar o base

Enquanto o hub não estiver no GitHub, a URL canônica permanece a da Vercel.

---

## API JurisSync (opcional - Fase 5b)

**Não implantada nesta fase.** Deploy público da API só se pedido explicitamente.

Se for feito no futuro:

- Usar modo mock (`DATAJUD_API_KEY` vazio)
- Documentar cold start e custos (Railway/Render)
- Expor apenas `GET /health` e endpoints de leitura com rate limit

Repo da API: https://github.com/MariaHilmar/juris-sync

---

## Checklist pós-deploy

- [x] Site acessível publicamente
- [x] URL no README raiz
- [x] URL no site (`web/`)
- [ ] Hub versionado no GitHub (opcional, para Pages / histórico)
- [ ] Domínio customizado (opcional)
