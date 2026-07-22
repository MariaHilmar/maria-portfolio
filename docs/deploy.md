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

## CI no GitHub (build)

Workflow em [`.github/workflows/build-site.yml`](../.github/workflows/build-site.yml): valida `npm ci` + `npm run build` em push/PR que alteram `web/`. **Não publica** o site - produção fica na Vercel.

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
