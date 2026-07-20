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

1. Publicar este repositório em `MariaHilmar/maria-portfolio`
2. Em **Settings → Pages**, escolher fonte **GitHub Actions**
3. Se o site for em `https://mariahilmar.github.io/maria-portfolio/`, ajustar `base` em `web/astro.config.mjs` para `'/maria-portfolio/'` e os links absolutos (`/docs/...`) para respeitar o base

Enquanto o hub não estiver no GitHub, a URL canônica permanece a da Vercel.

---

## API e dashboard JurisSync

**Artefatos de portfólio - avaliação local.** Não há deploy público obrigatório da API nem do dashboard Next.js.

| Peça | Repo | Como avaliar |
|------|------|--------------|
| API | [juris-sync](https://github.com/MariaHilmar/juris-sync) | Clone + uvicorn local; mock sem chave |
| Dashboard | [juris-sync-web](https://github.com/MariaHilmar/juris-sync-web) | Clone + `npm run dev`; aponta para `localhost:8000` |
| Guia | [guia-do-testador.md](https://github.com/MariaHilmar/juris-sync-web/blob/main/docs/guia-do-testador.md) | Mock vs DataJud real |

O site Astro neste repo (`web/`) é a **vitrine**; o dashboard Next é a **evidência de frontend**, rodando na máquina de quem testa.

Deploy público da API só se pedido explicitamente (e com restrições de CORS/rate limit).

---

## Checklist pós-deploy

- [x] Site acessível publicamente
- [x] URL no README raiz
- [x] URL no site (`web/`)
- [ ] Hub versionado no GitHub (opcional, para Pages / histórico)
- [ ] Domínio customizado (opcional)
