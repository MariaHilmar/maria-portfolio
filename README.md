# Maria Hilmar - Hub do Portfólio

**Product Manager / Product Owner | Dados e IA | Base técnica em Python** - liderança de produto com proximidade técnica e projetos hands-on em APIs, pipelines e fundamentos de IA.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mariahilmar/)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/5561982062117)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MariaHilmar)
[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://mariahilmar-portfolio.vercel.app)
[![E-mail](https://img.shields.io/badge/E--mail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mariahilmar@gmail.com)

**Live:** [mariahilmar-portfolio.vercel.app](https://mariahilmar-portfolio.vercel.app)  
**Perfil GitHub:** [MariaHilmar/MariaHilmar](https://github.com/MariaHilmar/MariaHilmar)  
**Deploy:** [`docs/deploy.md`](docs/deploy.md)

---

## Sobre este repositório

Este é o **hub central do meu portfólio no Git**. Aqui concentro narrativa profissional, documentação com evidências e o site em [`web/`](web/).

Os projetos técnicos ([JurisSync API](https://github.com/MariaHilmar/juris-sync) e [JurisSync Web](https://github.com/MariaHilmar/juris-sync-web)) são **artefatos de estudo e demonstração** ligados ao produto próprio **Situação Jurídica** (jurimetria/dados jurídicos): pensados para avaliação local (clone + run), não para operação em produção. Sem autenticação de usuários finais; modo **mock** (padrão) ou **DataJud real** (chave do próprio testador).

Sou Product Manager / Product Owner com histórico em gestão de squads ágeis e governança de software. Concluí **MBA em Ciência de Dados (BI & Analytics)** e venho consolidando autonomia técnica com projetos hands-on em Python e FastAPI, na intersecção entre negócios, dados, IA e engenharia.

---

## Perfil

| | |
|---|---|
| **Posicionamento** | Product Manager / Product Owner - Dados, IA e base técnica em Python |
| **Bagagem consolidada** | Gestão de backlog (ROI), métricas ágeis/negócio (OKRs, Velocity, Lead Time), engenharia de requisitos (BDD, UML, BPMN), governança de testes/QA (CTAL-TM) |
| **Projeto próprio de estudo** | Situação Jurídica (produto) → evidências públicas JurisSync e MGI KPI |
| **Stack em prática** | Python, FastAPI, PostgreSQL, Supabase, Redis, Docker, fundamentos de ML (XGBoost) e busca vetorial (pgvector) |
| **Público-alvo deste hub** | Recrutadores e hiring managers de produto/tech; tech leads que avaliam entrega, qualidade e profundidade técnica |

---

## Competências

Detalhamento completo com evidências verificáveis: **[`docs/competencias.md`](docs/competencias.md)**

| Área | O que demonstro |
|------|-----------------|
| **Gestão de produto / projetos** | Roadmap em sprints, requisitos rastreáveis, BDD, entrega incremental |
| **Desenvolvimento backend** | APIs REST async, arquitetura em camadas, Docker, CI/CD |
| **Automação de testes** | 43 testes em 5 camadas, Testcontainers, Schemathesis |
| **Engenharia de dados** | Pipeline ETL idempotente, migrações versionadas, integração DataJud |
| **Análise e jurimetria** | Agregações SQL, endpoints analíticos e dashboard interativo |
| **Frontend de mercado** | Next.js + React + TypeScript consumindo a API |

![Tecnologias](https://skillicons.dev/icons?i=python,fastapi,docker,postgres,redis,git,github,githubactions,react,nextjs,ts&perline=11)

---

## Projetos de estudo e portfólio técnico

### Situação Jurídica (projeto próprio)

Produto próprio de jurimetria e dados jurídicos, em desenvolvimento como estudo aplicado de Product Ownership com base técnica. **Não é vínculo empregatício.** Os repositórios públicos abaixo são as evidências técnicas desse trabalho.

### JurisSync - API Backend (`juris-sync`)

Estudo prático focado em arquitetura de APIs assíncronas com FastAPI, persistência de dados e testes automatizados em múltiplas camadas.

API REST assíncrona para monitoramento, ingestão e jurimetria de processos judiciais, integrada à [API Pública do DataJud (CNJ)](https://datajud-wiki.cnj.jus.br/api-publica/).

- **Repositório:** [github.com/MariaHilmar/juris-sync](https://github.com/MariaHilmar/juris-sync)
- **Destaques:**
  - Pipeline de sincronização idempotente (DataJud → validação → persistência)
  - 43 testes em 5 camadas (unitário, API, mock HTTP, reconciliação, integração e contrato)
  - Documentação viva de requisitos com rastreabilidade requisito → código → teste
  - Modo **mock** sem chave CNJ; modo **real** opcional com `DATAJUD_API_KEY`

### JurisSync - Data & Analytics (`juris-sync-web`)

Interface focada em jornadas de dados: jurimetria interativa, consumo de API e conceitos iniciais de NLP, estratégias de LLM/RAG e bases analíticas.

Cliente web (Next.js + React + TypeScript + TanStack Query + Recharts) com jurimetria, lista, detalhe/timeline e sync por CNJ.

- **Repositório:** [github.com/MariaHilmar/juris-sync-web](https://github.com/MariaHilmar/juris-sync-web)
- **Como testar:** [Guia do testador](https://github.com/MariaHilmar/juris-sync-web/blob/main/docs/guia-do-testador.md)
- **Case study:** [`docs/case-study-juris-sync.md`](docs/case-study-juris-sync.md)

---

## Como este repositório está organizado

```
maria-portfolio/        # Este repositório (hub: narrativa, docs e site)
├── README.md
├── PORTFOLIO_EXECUTION_PLAN.md
├── docs/
├── web/                # Site estático (Astro)
└── scripts/
```

Workspace local típico:

```
git-portfolio/
├── maria-portfolio/    # Hub + vitrine Astro
├── juris-sync/         # API FastAPI (repo próprio)
└── juris-sync-web/     # Dashboard Next.js (repo próprio)
```

- **`maria-portfolio`** - vitrine, documentação narrativa e links para os repos técnicos.
- **`web/`** - site Astro. Desenvolvimento: `cd web && npm install && npm run dev` (http://localhost:4321).
- **`juris-sync`** e **`juris-sync-web`** - repositórios separados com a evidência técnica.

---

## Plano de execução

Fases documentadas em [`PORTFOLIO_EXECUTION_PLAN.md`](PORTFOLIO_EXECUTION_PLAN.md):

| Fase | Status |
|------|--------|
| 0 - Posicionamento | Concluída |
| 1 - Fundação do hub | Concluída |
| 2 - Case study JurisSync | Concluída |
| 3 - Competências com evidências | Concluída |
| 4 - Site estático | Concluída |
| 5 - Deploy (site) | Concluída |
| 6 - Polimento | Concluída |

---

## Licença

Cada subprojeto segue a licença do respectivo repositório. Consulte o README de `juris-sync` para detalhes.
