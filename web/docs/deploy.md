# Deploy do portfólio

## Site (produção atual)

| Item | Valor |
|------|-------|
| **URL live** | https://mariahilmar.vercel.app |
| **Plataforma** | Vercel |
| **Projeto** | `mariahilmar` |
| **Escopo atual** | time `situacao-juridica-projects` (conta autenticada no CLI) |
| **Origem** | pasta `web/` (Astro estático) |
| **Branch de producao** | `docs/portfolio-hub` (default no GitHub) |

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

## CI no GitHub

| Workflow | Arquivo | O que faz |
|----------|---------|-----------|
| Build | [`.github/workflows/build-site.yml`](../.github/workflows/build-site.yml) | Valida `npm ci` + `npm run build` em PR e push |
| Deploy | [`.github/workflows/deploy-site.yml`](../.github/workflows/deploy-site.yml) | Publica em producao na Vercel apos merge em `docs/portfolio-hub` |

### Por que o merge nao atualizava producao

O projeto `mariahilmar` na Vercel foi criado com deploy manual via CLI (`vercel deploy --prod`). O repositorio **nao estava conectado** a integracao Git da Vercel, e o workflow de build **so compilava** sem publicar.

### Configurar deploy automatico (obrigatorio uma vez)

Adicione estes secrets em **GitHub → Settings → Secrets and variables → Actions**:

| Secret | Valor |
|--------|-------|
| `VERCEL_TOKEN` | Token em [vercel.com/account/tokens](https://vercel.com/account/tokens) |
| `VERCEL_ORG_ID` | `team_K0R2FcqfhJeaNCnZ4CkD2pbk` |
| `VERCEL_PROJECT_ID` | `prj_jyVxABEzwhtriemLFvaA6WaMym7F` |

Depois do merge em `docs/portfolio-hub`, o workflow **Deploy portfolio site** publica em https://mariahilmar.vercel.app.

Para republicar manualmente sem novo merge: **Actions → Deploy portfolio site → Run workflow**.

### Alternativa: integracao Git da Vercel

Em vez do workflow acima, conecte o repo em **Vercel → mariahilmar → Settings → Git**:

- Repositorio: `MariaHilmar/maria-portfolio`
- Production Branch: `docs/portfolio-hub`
- Root Directory: `web`

Use **apenas uma** das opcoes (GitHub Actions **ou** integracao Git da Vercel) para evitar deploy duplicado.

---

## GitHub Pages (opcional, desativado)

Se no futuro quiser hospedar em `https://mariahilmar.github.io/maria-portfolio/`:

1. Habilitar **Settings → Pages → GitHub Actions**
2. Recriar job de deploy no workflow (ou workflow separado)
3. Ajustar `base` em `web/astro.config.mjs` para `'/maria-portfolio/'`

URL canônica atual: Vercel (tabela acima).

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
- [x] Hub versionado no GitHub
- [ ] Domínio customizado (opcional)
