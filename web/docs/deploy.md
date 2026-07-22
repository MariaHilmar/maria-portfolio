# Deploy do portfólio

## Padrão nos projetos

| Camada | Ferramenta | O que faz |
|--------|------------|-----------|
| **CI** | GitHub Actions | Lint, testes e build em PR/push |
| **Deploy web** | Integração Git da Vercel | Build e publicação automáticos após merge |
| **APIs / backends** | Sem deploy público | Avaliação local (`docker compose`, `uvicorn`, `npm run dev`) |

Repos que seguem esse padrão hoje:

| Repo | CI (GitHub Actions) | Deploy |
|------|---------------------|--------|
| [juris-sync](https://github.com/MariaHilmar/juris-sync) | lint + testes | local |
| [juris-sync-web](https://github.com/MariaHilmar/juris-sync-web) | lint + test + build | local (ou Vercel se conectado) |
| [paycore](https://github.com/MariaHilmar/paycore) | lint + testes | local |
| **maria-portfolio** (este) | build do site Astro | Vercel (integração Git) |

**Regra:** CI valida no GitHub; a Vercel publica. Não usar workflow de deploy com `VERCEL_TOKEN` no GitHub Actions.

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

### Configurar integração Git (uma vez)

No painel **Vercel → mariahilmar → Settings → Git**:

1. **Connect Git Repository** → `MariaHilmar/maria-portfolio`
2. **Production Branch** → `docs/portfolio-hub`
3. **Root Directory** → `web`
4. Framework: Astro (detectado automaticamente)
5. Salvar

Depois disso, cada merge em `docs/portfolio-hub` dispara deploy em produção. PRs ganham **preview URL** automática.

### CI no GitHub

Workflow [`.github/workflows/build-site.yml`](../.github/workflows/build-site.yml): valida `npm ci` + `npm run build` em PR e push. **Não publica** - só garante que o site compila antes do merge.

### Fallback manual (emergência)

Se a integração Git falhar:

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
- [ ] Integração Git Vercel conectada ao repositório
- [ ] Domínio customizado (opcional)
