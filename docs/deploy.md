# Deploy do portfólio

## Padrão nos projetos

| Camada | Ferramenta | O que faz |
|--------|------------|-----------|
| **CI** | GitHub Actions | Lint, testes e build em PR/push |
| **Deploy web** | GitHub Actions + Vercel | Publica apos merge em `docs/portfolio-hub` |
| **APIs / backends** | Sem deploy público | Avaliação local (`docker compose`, `uvicorn`, `npm run dev`) |

Repos que seguem esse padrão hoje:

| Repo | CI (GitHub Actions) | Deploy |
|------|---------------------|--------|
| [juris-sync](https://github.com/MariaHilmar/juris-sync) | lint + testes | local |
| [juris-sync-web](https://github.com/MariaHilmar/juris-sync-web) | lint + test + build | local (ou Vercel se conectado) |
| [paycore](https://github.com/MariaHilmar/paycore) | lint + testes | local |
| **maria-portfolio** (este) | build do site Astro | GitHub Actions → Vercel |

**Regra:** CI valida no GitHub; o workflow `deploy-site.yml` dispara a publicacao na Vercel apos merge em `docs/portfolio-hub`.

---

## Site (produção)

| Item | Valor |
|------|-------|
| **URL live** | https://mariahilmar.vercel.app |
| **Plataforma** | Vercel |
| **Projeto** | `mariahilmar` |
| **Time** | `situacao-juridica-projects` |
| **Root Directory** | `web` |
| **Branch de produção** | `docs/portfolio-hub` |

### Deploy automatico (GitHub Actions)

Workflow [`.github/workflows/deploy-site.yml`](../.github/workflows/deploy-site.yml): roda em **push** para `docs/portfolio-hub` e publica em producao.

Configure **um** dos metodos nos secrets do repositorio (`Settings → Secrets and variables → Actions`):

| Metodo | Secrets | Como obter |
|--------|---------|------------|
| **Deploy Hook** (recomendado) | `VERCEL_DEPLOY_HOOK` | Vercel → mariahilmar → Settings → Git → Deploy Hooks → branch `docs/portfolio-hub` |
| **CLI** (fallback) | `VERCEL_TOKEN`, `VERCEL_ORG_ID`, `VERCEL_PROJECT_ID` | `vercel link` no diretorio `web/` e painel da Vercel |

Tambem e possivel disparar manualmente em **Actions → Deploy portfolio site → Run workflow**.

### Integracao Git da Vercel (complementar)

No painel **Vercel → mariahilmar → Settings → Git**:

1. **Connect Git Repository** → `MariaHilmar/maria-portfolio`
2. **Production Branch** → `docs/portfolio-hub`
3. **Root Directory** → `web`
4. Framework: Astro (detectado automaticamente)
5. Salvar

A integracao Git gera previews de PR. O deploy de producao apos merge e garantido pelo workflow acima.

### CI no GitHub

Workflow [`.github/workflows/build-site.yml`](../.github/workflows/build-site.yml): valida `npm ci` + `npm run build` em PR e push. **Nao publica** - so garante que o site compila antes do merge.

### Fallback manual (emergencia)

Se o workflow de deploy falhar:

```powershell
cd web
npm run build
vercel deploy --prod --yes
```

Requer [Vercel CLI](https://vercel.com/docs/cli) logado (`vercel login`).

### Variáveis

Nenhuma variável de ambiente é necessária para o site estático na v1.

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
- [ ] Secret `VERCEL_DEPLOY_HOOK` (ou trio `VERCEL_TOKEN` + IDs) configurado no GitHub
- [ ] Integracao Git Vercel conectada ao repositorio (opcional, para previews)
- [ ] Domínio customizado (opcional)
