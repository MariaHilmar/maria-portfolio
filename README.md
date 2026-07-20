# Maria Hilmar - Portfólio

**Product Owner com base técnica em Python:** traduz necessidade de negócio em entregas versionadas, testadas e observáveis.

Este repositório é o **hub do meu portfólio no Git**. Aqui concentro a narrativa profissional, documentação e o site em [`web/`](web/). O código de referência fica no projeto [JurisSync](https://github.com/MariaHilmar/juris-sync), que serve como evidência técnica das competências abaixo.

**Live:** [mariahilmar-portfolio.vercel.app](https://mariahilmar-portfolio.vercel.app)  
**GitHub:** [MariaHilmar/maria-portfolio](https://github.com/MariaHilmar/maria-portfolio)  
**Deploy:** [`docs/deploy.md`](docs/deploy.md)

---

## Perfil

| | |
|---|---|
| **Foco principal** | Gestão de produto e projetos com profundidade técnica |
| **Complementos** | Desenvolvimento backend, automação de testes, engenharia de dados, análise |
| **Público-alvo deste hub** | Recrutadores e hiring managers de produto/tech; tech leads que avaliam entrega e qualidade |

---

## Competências

Detalhamento completo com evidências verificáveis: **[`docs/competencias.md`](docs/competencias.md)**

| Área | O que demonstro |
|------|-----------------|
| **Gestão de produto / projetos** | Roadmap em sprints, requisitos rastreáveis, BDD, entrega incremental |
| **Desenvolvimento** | APIs REST async, arquitetura em camadas, Docker, CI/CD |
| **Automação de testes** | 43 testes em 5 camadas, Testcontainers, Schemathesis |
| **Engenharia de dados** | Pipeline ETL idempotente, migrações versionadas, integração DataJud |
| **Análise** | Endpoints de jurimetria com agregações SQL sobre base local |

---

## Projetos

### JurisSync API

API REST assíncrona para monitoramento, ingestão e jurimetria de processos judiciais, integrada à [API Pública do DataJud (CNJ)](https://datajud-wiki.cnj.jus.br/api-publica/).

- **Repositório:** [github.com/MariaHilmar/juris-sync](https://github.com/MariaHilmar/juris-sync)
- **Destaques:**
  - Pipeline de sincronização idempotente (DataJud → validação → persistência)
  - 43 testes em 5 camadas (unitário, API, mock HTTP, reconciliação, integração e contrato)
  - Documentação viva de requisitos com rastreabilidade requisito → código → teste
- **Case study:** [`docs/case-study-juris-sync.md`](docs/case-study-juris-sync.md)
- **Site:** [mariahilmar-portfolio.vercel.app](https://mariahilmar-portfolio.vercel.app)

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

- **`maria-portfolio`** concentra a vitrine e a documentação narrativa.
- **`web/`** - site Astro. Desenvolvimento: `cd web && npm install && npm run dev` (http://localhost:4321).
- **`juris-sync`** é projeto âncora em repositório separado: [MariaHilmar/juris-sync](https://github.com/MariaHilmar/juris-sync). No workspace local `D:\git-portfolio\`, fica em pasta irmã (`../juris-sync`).

---

## Plano de execução

O desenvolvimento deste hub segue fases documentadas em [`PORTFOLIO_EXECUTION_PLAN.md`](PORTFOLIO_EXECUTION_PLAN.md):

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
