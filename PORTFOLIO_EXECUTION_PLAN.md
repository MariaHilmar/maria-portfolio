# Plano de execução - Portfólio MariaHilmar

Documento para o **Composer** (ou outro agente) executar por etapas.
Não implementar tudo de uma vez. Concluir uma fase, validar o critério de pronto, só então avançar.

**Workspace:** `D:\git-portfolio`  
**Projeto âncora:** `juris-sync` (https://github.com/MariaHilmar/juris-sync)  
**Autor dos commits (quando pedido):** `MariaHilmar <mariahilmar@gmail.com>`  
**Idioma:** português (pt-BR). Nunca usar travessão (—); usar hífen (-).

---

## Regras obrigatórias para o agente

1. **Não commit/push/PR** sem pedido explícito do usuário.
2. **Nunca** commitar `.env`, tokens, credenciais, dumps ou arquivos temporários.
3. **Nunca** push direto em `main`/`master`. Usar branch `feat/` ou `docs/`.
4. **Não** adicionar Co-authored-by Cursor nem trailers de atribuição ao Cursor.
5. Preferir **menos arquivos** e **conteúdo linkado** a muitos docs órfãos.
6. Antes de criar doc novo: perguntar se o case study ou README já cobre o assunto.
7. Ao atender issues GitHub/GitLab: ler issue + comentários; ao concluir, comentar e fechar (salvo pedido em contrário).
8. Responder ao usuário em português, de forma direta.

---

## Contexto do repositório (estado atual)

```
D:\git-portfolio\
├── README.md            # Entrada do hub (Fase 1)
├── PORTFOLIO_EXECUTION_PLAN.md
├── docs/                # Case study, competências, assets (Fases 1-3)
├── web/                 # Site Astro (Fase 4)
├── .gitignore           # Raiz - cobre .env, caches, PDF local, node_modules
├── juris-sync\          # API FastAPI - projeto principal de portfólio
├── .env                 # NÃO versionar / NÃO commit
└── Product Owner - Maria Hilmar Gomes da Silva.pdf  # local, ignorado pelo .gitignore
```

- Site estático em `web/` (Astro). **Live:** https://mariahilmar-portfolio.vercel.app (Fase 5a).
- Não há pasta `exemplos/` com código de terceiros.
- JurisSync já demonstra: backend, ETL/idempotência, 5 camadas de teste, CI, jurimetria básica, roadmap de sprints.

---

## Posicionamento (Fase 0) - CONFIRMADO

**Status:** aceito pelo usuário em 2026-07-20 (default do plano, alinhado às conversas do chat).

| Campo | Valor |
|-------|-------|
| Papel primário | Product Owner / gestão de produto com base técnica |
| Secundários | Desenvolvimento backend, automação de testes, engenharia de dados (pipeline), análise |
| Frase de perfil | "Product Owner com base técnica em Python: traduz necessidade de negócio em entregas versionadas, testadas e observáveis." |
| Público | Recrutadores e hiring managers de produto/tech; tech leads que avaliam profundidade |
| Mensagem do hub | O repositório `git-portfolio` é a vitrine; `juris-sync` é a evidência técnica |

Se o PDF de Product Owner estiver no workspace, usá-lo só como referência de tom/experiência - **não** colar dados sensíveis no README público sem confirmação do usuário.

---

## Visão das fases

```
Fase 0  Posicionamento (confirmar com usuário se necessário)
  ↓
Fase 1  Fundação do hub (README raiz + limpeza)
  ↓
Fase 2  Case study JurisSync (+ screenshots)
  ↓
Fase 3  Competências (Markdown/tabela, sem YAML obrigatório)
  ↓
★★★ MVP FREEZE - parar e validar com o usuário ★★★
  ↓
Fase 4  Site estático (uma UI; jurimetria embutida ou via screenshot)
  ↓
Fase 5  Deploy (site obrigatório; API demo opcional)
  ↓
Fase 6  Polimento final
```

**Atalho:** Fases 0-3 = MVP (~6-8h). Fases 4-6 = vitrine (~10-15h).

---

## Fase 0 - Posicionamento

**Objetivo:** Uma frase clara de perfil antes de escrever conteúdo.

### Tarefas

1. Confirmar com o usuário (se ainda não confirmou) o papel primário e a frase de perfil.
2. Registrar a escolha no topo deste arquivo ou no README (após Fase 1), seção "Perfil".
3. Critério de sucesso do portfólio (usar como checklist final):
   - [ ] Perfil compreendido em ~30 segundos
   - [ ] Duas evidências técnicas citáveis sem abrir código
   - [ ] Pelo menos um visual forte (screenshot Swagger, CI ou gráfico)

### Critério de pronto

Usuário confirmou (ou aceitou o default) papel + frase.

### Estimativa

15-30 min

---

## Fase 1 - Fundação do hub

**Objetivo:** Quem abre `git-portfolio` entende o que é em menos de 30 segundos.

### Tarefas

1. Criar `README.md` na raiz com:
   - Nome + frase de perfil (Fase 0)
   - Links: GitHub (MariaHilmar), LinkedIn (pedir URL se faltar), e-mail só se o usuário autorizar
   - Seção **Competências** (resumo; detalhe vem na Fase 3)
   - Seção **Projetos** com card textual do JurisSync (link repo + 3 bullets de destaque)
   - Seção **Como este repositório está organizado**
   - Aviso de que `juris-sync` pode ser subpasta e/ou repo próprio
2. Criar pasta `docs/` (vazia ou com `.gitkeep`).
3. **Limpeza de exemplos de terceiros:**
   - Se existir `exemplos/rag-juridico-br-main` (ou similar de outro autor):
     - Preferência A: remover do tree versionado
     - Preferência B: mover para `references/` com `README.md` dizendo explicitamente que **não é código próprio**
   - Não deixar código alheio incompleto na raiz sem aviso
4. Garantir `.gitignore` na raiz cobrindo `.env`, `.venv`, `__pycache__`, caches, segredos.
5. **Não** incluir o PDF de PO no git a menos que o usuário peça.

### Arquivos esperados

- `README.md` (raiz)
- `docs/` 
- `.gitignore` (raiz, se ainda não existir)
- Ajuste em `exemplos/` ou `references/` conforme regra acima

### Critério de pronto

- README raiz renderiza bem no GitHub/preview Markdown
- Nenhum código de terceiro sem atribuição clara
- `.env` fora do versionamento

### Estimativa

1-2 h

### Branch sugerida (se commit for pedido)

`docs/portfolio-hub-foundation`

---

## Fase 2 - Case study JurisSync

**Objetivo:** Narrativa profissional (problema → solução → processo → resultado).

### Tarefas

1. Criar `docs/case-study-juris-sync.md` com seções fixas:
   1. Contexto e problema
   2. Papel / abordagem (PO + decisões técnicas)
   3. Solução (API, pipeline ETL, jurimetria)
   4. Arquitetura (mermaid reutilizando ideia do README do juris-sync)
   5. Decisões técnicas e trade-offs (async, idempotência, mock DataJud, RAG em memória, SQLite vs Postgres)
   6. Gestão da entrega (5 sprints do README - status e o que cada uma liberou)
   7. Qualidade (5 camadas de teste, cobertura ~89%, CI em 3 jobs)
   8. Resultados e aprendizados
   9. Links (repo, `/docs` Swagger local, workflow CI)
2. Coletar/gerar evidências visuais e salvar em `docs/assets/` (ou `docs/images/`):
   - Screenshot Swagger (`/docs`) **ou** instrução clara de como capturar se a API não estiver rodando
   - Screenshot/badge referência do CI verde
   - (Opcional) árvore ou tabela das camadas de teste
3. Linkar o case study no `README.md` raiz e, se fizer sentido, no `juris-sync/README.md` (seção curta "Case study").
4. **Não** criar `testing-strategy.md` / `data-pipeline.md` separados nesta fase - o case study absorve QA e dados. Só extrair docs dedicados depois se o case study passar de ~800 linhas ou o site precisar de páginas próprias.

### Critério de pronto

Um recrutador de produto ou tech lead entende problema, solução, processo e impacto sem ler código.

### Estimativa

2-3 h

### Branch sugerida

`docs/case-study-juris-sync`

---

## Fase 3 - Competências com evidências

**Objetivo:** Cada competência aponta para evidência real (arquivo, endpoint, teste, doc).

### Tarefas

1. Criar `docs/competencias.md` (Markdown simples - **sem** `skills.yaml` obrigatório) com tabela ou seções:

| Área | Nível | Evidência no JurisSync | Onde ver |
|------|-------|------------------------|----------|
| Gestão de produto / projetos | ... | Roadmap sprints, case study | `docs/case-study-...` |
| Desenvolvimento backend | ... | FastAPI, camadas, Docker | `juris-sync/app/` |
| Automação de testes | ... | Testcontainers, Schemathesis, pirâmide | `juris-sync/tests/`, CI |
| Engenharia de dados | ... | Pipeline sync idempotente, Alembic | `sync_service`, migrations |
| Análise | ... | Endpoints stats por tribunal/assunto | `app/api/process.py` |

2. Atualizar seção Competências do `README.md` raiz para apontar para `docs/competencias.md`.
3. Cada linha precisa de **pelo menos um path ou URL** verificável.

### Critério de pronto

Nenhuma competência é só buzzword; todas têm evidência linkada.

### Estimativa

1-2 h

### Branch sugerida

`docs/competencias`

---

## ★★★ MVP FREEZE ★★★

**Parar e pedir validação ao usuário antes da Fase 4.**

Checklist MVP:

- [x] README raiz claro
- [x] Case study completo
- [x] Competências com evidências
- [x] Exemplos de terceiros tratados (não havia pasta `exemplos/`)
- [x] Links internos ok
- [x] Nada sensível versionado (`.env` e PDF no `.gitignore`)

Perguntar ao usuário: *"MVP do hub pronto. Seguir para o site (Fase 4) ou ajustar conteúdo?"*

---

## Fase 4 - Site estático (uma UI)

**Objetivo:** Vitrine pública. Uma interface só - **não** criar Streamlit/dashboard separado na primeira entrega.

### Stack preferida

1. **Astro** (estático, rápido) em `web/`  
2. Fallback: HTML/CSS estático em `web/` se o usuário quiser zero build

### Seções obrigatórias

1. Hero - nome, frase de perfil, CTAs (GitHub, LinkedIn, case study)
2. Sobre - perfil multidisciplinar com primário em PO/produto
3. Competências - espelhar `docs/competencias.md` (copiar conteúdo ou importar Markdown; evitar YAML novo)
4. Projetos - card JurisSync (links repo + case study)
5. Jurimetria / análise - **screenshot + texto** OU gráficos leves consumindo API **se** API local/demo estiver disponível; senão, só screenshot/mock estático
6. Processo - sprints, CI, qualidade (resumo do case study)
7. Contato

### Design (regras do usuário para frontend)

- Uma composição no primeiro viewport (não dashboard)
- Marca/nome como sinal forte no hero
- Tipografia expressiva (evitar Inter/Roboto/Arial/system como escolha padrão)
- Fundo com atmosfera (gradiente/padrão sutil) - não cor chapada única
- Sem cards no hero; cards só onde houver interação real
- Evitar clichês: roxo-indigo default, cream+terracota+serif, dark mode forçado, glow, pills em excesso, emojis
- Responsivo mobile + desktop
- 2-3 motions intencionais

### Tarefas

1. Scaffold `web/` com a stack escolhida.
2. Conteúdo real (não lorem).
3. Reutilizar assets de `docs/assets/`.
4. README curto em `web/README.md` (dev local).
5. Link do site (local) no README raiz quando aplicável.

### Fora de escopo nesta fase

- App Streamlit separado
- Notebook Jupyter (salvo pedido explícito)
- Autenticação JWT na API
- Redesign do juris-sync backend

### Critério de pronto

Site responsivo, seções preenchidas, carrega rápido em dev; conteúdo alinhado às Fases 1-3.

### Estimativa

4-6 h

### Branch sugerida

`feat/portfolio-web`

---

## Fase 5 - Deploy

**Objetivo:** Links públicos. Site é o gate; API é bônus.

### 5a - Site (obrigatório para "live")

1. Deploy do `web/` em GitHub Pages ou Vercel.
2. Documentar URL no README raiz e no site.
3. Criar `docs/deploy.md` só com passos reproduzíveis (curto).

### 5b - API demo (opcional - não bloqueia conclusão)

Só se o usuário pedir:

1. Deploy JurisSync com **mock DataJud sempre ligado** (sem depender de chave real em público).
2. Rate limit / `ENV=demo` se fizer sentido.
3. Health check documentado.
4. Avisar custos e cold start no `docs/deploy.md`.

### Critério de pronto

- [x] Site acessível publicamente → https://mariahilmar-portfolio.vercel.app
- [x] README com link "Live"
- [x] `docs/deploy.md` criado
- [ ] API demo (5b) - não solicitada; fora desta entrega

### Estimativa

2-3 h (só site); +1-2 h se API

### Branch sugerida

`chore/portfolio-deploy-docs`

---

## Fase 6 - Polimento

### Checklist

- [x] Links internos e externos testados (site live, GitHub, docs espelhados)
- [x] Ortografia e tom consistentes (pt-BR)
- [x] Evidências visuais: site live + badges CI/cobertura + jurimetria ilustrativa no site
- [x] Meta tags / título / descrição / OG / favicon no site
- [x] Layout responsivo (mobile + desktop)
- [x] Nenhum segredo versionado (`.env`, PDF, `juris-sync/` no `.gitignore`)
- [x] README raiz e case study apontam para o site live
- [x] Script `scripts/sync-docs.ps1` para manter docs espelhados no site
- [ ] README em inglês - não solicitado

### Critério de pronto

Usuário se sentiria confortável enviando o link em processo seletivo.

### Estimativa

1-2 h

---

## Ordem de comandos sugerida por sessão

O agente deve abrir a sessão assim:

1. Ler este arquivo `PORTFOLIO_EXECUTION_PLAN.md`
2. Perguntar (ou inferir da conversa) **qual fase executar**
3. Listar tarefas da fase
4. Implementar só aquela fase
5. Mostrar diff / arquivos criados
6. Validar critério de pronto
7. Perguntar se commit e se avança

### Frases de gatilho do usuário

| Usuário diz | Agente faz |
|-------------|------------|
| `fase 0` / `posicionamento` | Fase 0 |
| `fase 1` / `fundação` | Fase 1 |
| `fase 2` / `case study` | Fase 2 |
| `fase 3` / `competências` | Fase 3 |
| `mvp` / `freeze` | Rodar checklist MVP FREEZE |
| `fase 4` / `site` | Fase 4 (só após MVP validado ou ordem explícita) |
| `fase 5` / `deploy` | Fase 5 |
| `fase 6` / `polimento` | Fase 6 |
| `executar MVP` | Fases 1→2→3 em sequência, pausando no FREEZE |

---

## Decisões já tomadas (não reabrir sem o usuário)

| Decisão | Valor |
|---------|--------|
| Projeto âncora | JurisSync |
| Hub | `git-portfolio` (README + docs + web) |
| Produto técnico | Repo/pasta `juris-sync` separado do hub quando possível |
| skills.yaml | Não obrigatório; preferir Markdown |
| Dashboard Streamlit separado | Não na v1; jurimetria no site ou screenshot |
| Docs QA/dados separados | Só se case study ficar enorme |
| Deploy API | Opcional; mock em público |
| Papel primário default | Product Owner com base técnica |

---

## Estimativa total

| Bloco | Fases | Horas |
|-------|-------|-------|
| MVP | 0-3 | 6-8 h |
| Vitrine | 4-6 | 10-15 h |
| **Total** | 0-6 | **~16-23 h** |

---

## Definição de pronto do portfólio completo

1. Hub com README + case study + competências  
2. Site live com perfil claro → https://mariahilmar-portfolio.vercel.app  
3. JurisSync linkado com evidências de backend, testes, dados e entrega  
4. Sem código de terceiro ambíguo e sem segredos no git  
5. Fases 0-6 concluídas (polimento e meta tags aplicados)

---

*Última atualização do plano: 2026-07-20 (Fase 6 concluída)*
