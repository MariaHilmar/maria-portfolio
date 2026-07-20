# Competências com evidências

Cada área abaixo aponta para **evidência verificável** no projeto [JurisSync](https://github.com/MariaHilmar/juris-sync). Nada é só buzzword: há arquivo, endpoint, teste ou documento para conferir.

**Case study completo:** [`case-study-juris-sync.md`](case-study-juris-sync.md) · **Site:** [mariahilmar-portfolio.vercel.app](https://mariahilmar-portfolio.vercel.app)

---

## Visão geral

| Área | Nível | Projeto | Evidência principal |
|------|-------|---------|---------------------|
| Gestão de produto / projetos | Avançado | JurisSync | Roadmap em sprints, requisitos rastreáveis, BDD |
| Desenvolvimento backend | Avançado | JurisSync | FastAPI async, camadas, Docker, CI |
| Automação de testes | Avançado | JurisSync | 43 testes em 5 camadas, Testcontainers, Schemathesis |
| Engenharia de dados | Intermediário-avançado | JurisSync | Pipeline ETL idempotente, Alembic, integração DataJud |
| Análise de dados | Intermediário | JurisSync | Endpoints de jurimetria com agregações SQL |

*Níveis são autoavaliação com base no escopo do projeto de portfólio, não em anos de experiência formal.*

---

## 1. Gestão de produto e projetos

**O que demonstro:** priorização em sprints, requisitos funcionais e não funcionais, critérios de aceite, rastreabilidade e entrega incremental.

| Evidência | Onde ver |
|-----------|----------|
| Roadmap de 5 sprints com status | [`juris-sync/README.md`](../../juris-sync/README.md#roadmap-sprints) |
| Visão do produto, glossário e escopo | [`juris-sync/docs/requisitos.md`](../../juris-sync/docs/requisitos.md#1-visão-do-produto) |
| 16 regras de negócio documentadas (RN01-RN16) | [`juris-sync/docs/requisitos.md`](../../juris-sync/docs/requisitos.md#4-regras-de-negócio) |
| Histórias de usuário e cenários BDD | [`juris-sync/docs/requisitos.md`](../../juris-sync/docs/requisitos.md#5-histórias-de-usuário) |
| Rastreabilidade requisito → código → teste | [`juris-sync/docs/requisitos.md`](../../juris-sync/docs/requisitos.md#9-rastreabilidade-requisito---código---teste) |
| Narrativa de entrega (case study) | [`case-study-juris-sync.md`](case-study-juris-sync.md#6-gestão-da-entrega) |
| Coleção Postman para demo e onboarding | [`juris-sync/postman/`](../../juris-sync/postman/) |

**Exemplo citável:** *"Requisitos escritos em paralelo ao código, com 16 regras de negócio rastreáveis até testes automatizados."*

---

## 2. Desenvolvimento backend

**O que demonstro:** APIs REST assíncronas, arquitetura em camadas, validação na fronteira, containerização e pipeline de CI.

| Evidência | Onde ver |
|-----------|----------|
| Entrypoint FastAPI | [`juris-sync/app/main.py`](../../juris-sync/app/main.py) |
| Rotas e contratos OpenAPI | [`juris-sync/app/api/process.py`](../../juris-sync/app/api/process.py) |
| Schemas Pydantic v2 | [`juris-sync/app/schemas/process.py`](../../juris-sync/app/schemas/process.py) |
| Modelos ORM SQLAlchemy 2.0 async | [`juris-sync/app/models/process.py`](../../juris-sync/app/models/process.py) |
| Config centralizada | [`juris-sync/app/core/config.py`](../../juris-sync/app/core/config.py) |
| Logs estruturados | [`juris-sync/app/core/logging.py`](../../juris-sync/app/core/logging.py) |
| Dockerfile multi-stage | [`juris-sync/Dockerfile`](../../juris-sync/Dockerfile) |
| Docker Compose (PostgreSQL) | [`juris-sync/docker-compose.yml`](../../juris-sync/docker-compose.yml) |
| CI (lint + test + integração) | [`juris-sync/.github/workflows/ci.yml`](../../juris-sync/.github/workflows/ci.yml) |
| Swagger UI (local) | http://localhost:8000/docs |

**Stack:** Python 3.12+, FastAPI, SQLAlchemy 2.0 async, Alembic, Pydantic v2, httpx, structlog, Docker.

**Exemplo citável:** *"API REST async com camadas api/core/models/schemas/services, documentada via OpenAPI e validada com Pydantic na fronteira."*

---

## 3. Automação de testes

**O que demonstro:** pirâmide de testes, mocks de HTTP, reconciliação de dados, integração com banco real e contract testing.

| Camada | O que valida | Arquivo(s) |
|--------|--------------|------------|
| Unitário / schemas | Validação Pydantic, regras isoladas | [`juris-sync/tests/test_schemas.py`](../../juris-sync/tests/test_schemas.py), [`test_sync_service.py`](../../juris-sync/tests/test_sync_service.py), [`test_rag_enricher.py`](../../juris-sync/tests/test_rag_enricher.py) |
| API (ASGI) | Endpoints HTTP reais contra FastAPI | [`juris-sync/tests/test_api.py`](../../juris-sync/tests/test_api.py) |
| Mock HTTP | Contrato da chamada DataJud, fallbacks | [`juris-sync/tests/test_datajud_client.py`](../../juris-sync/tests/test_datajud_client.py), [`test_datajud_client_contract.py`](../../juris-sync/tests/test_datajud_client_contract.py) |
| Reconciliação | Fidelidade dos dados, atomicidade, sem órfãos | [`juris-sync/tests/test_sync_reconciliation.py`](../../juris-sync/tests/test_sync_reconciliation.py) |
| Integração | PostgreSQL real via Testcontainers + Alembic | [`juris-sync/tests/integration/test_sync_service_postgres.py`](../../juris-sync/tests/integration/test_sync_service_postgres.py) |
| Contrato OpenAPI | Fuzzing com Schemathesis | [`juris-sync/tests/contract/test_openapi_contract.py`](../../juris-sync/tests/contract/test_openapi_contract.py) |

| Métrica | Valor | Onde ver |
|---------|-------|----------|
| Total de testes | 43 | [`juris-sync/README.md`](../../juris-sync/README.md#-testes-automatizados) |
| Cobertura (suíte padrão) | ~89,9% | [`juris-sync/pyproject.toml`](../../juris-sync/pyproject.toml) (`--cov-fail-under=85`) |
| CI verde | Badge | https://github.com/MariaHilmar/juris-sync/actions/workflows/ci.yml |

**Ferramentas:** pytest, pytest-asyncio, pytest-cov, httpx, respx, factory-boy, Testcontainers, Schemathesis, Hypothesis, Mypy.

**Exemplo citável:** *"43 testes em 5 camadas, incluindo Postgres real via Testcontainers e fuzzing OpenAPI com Schemathesis."*

---

## 4. Engenharia de dados

**O que demonstro:** pipeline de ingestão, normalização, persistência idempotente, versionamento de schema e integração com fonte externa.

| Evidência | O que prova | Onde ver |
|-----------|-------------|----------|
| Cliente DataJud + mock determinístico | Extração e fallback sem chave API | [`juris-sync/app/services/datajud_client.py`](../../juris-sync/app/services/datajud_client.py) |
| Orquestrador de sync (ETL) | Extração → enriquecimento → validação → upsert | [`juris-sync/app/services/sync_service.py`](../../juris-sync/app/services/sync_service.py) |
| Enriquecimento RAG | Normalização de classe, assunto, tribunal | [`juris-sync/app/services/rag/enricher.py`](../../juris-sync/app/services/rag/enricher.py) |
| Migration inicial | Modelagem relacional versionada | [`juris-sync/alembic/versions/`](../../juris-sync/alembic/versions/) |
| RN03 - idempotência incremental | Movimentações novas apenas | [`juris-sync/docs/requisitos.md`](../../juris-sync/docs/requisitos.md#rn03---movimentações-são-inseridas-apenas-se-novas-idempotência-incremental) |
| RN04 - atomicidade | Rollback em falha parcial | [`juris-sync/docs/requisitos.md`](../../juris-sync/docs/requisitos.md#rn04---pipeline-de-sincronização-é-atômico-tudo-ou-nada) |
| Teste de reconciliação | Fidelidade persistida vs. fonte | [`juris-sync/tests/test_sync_reconciliation.py`](../../juris-sync/tests/test_sync_reconciliation.py) |
| Integração Postgres | Pipeline contra banco real | [`juris-sync/tests/integration/test_sync_service_postgres.py`](../../juris-sync/tests/integration/test_sync_service_postgres.py) |

**Fluxo ETL:**

```
DataJud (ou mock) → RAG (normalização) → Pydantic (validação) → upsert idempotente
```

**Exemplo citável:** *"Pipeline ETL idempotente com reconciliação: re-sync não duplica processos nem movimentações."*

---

## 5. Análise de dados

**O que demonstro:** agregações SQL sobre base persistida, endpoints de jurimetria e regra de negócio para análise local.

| Evidência | O que prova | Onde ver |
|-----------|-------------|----------|
| Stats por tribunal | `GROUP BY` tribunal | [`juris-sync/app/api/process.py`](../../juris-sync/app/api/process.py) (rota `stats/por-tribunal`) |
| Stats por assunto | `GROUP BY` assunto | [`juris-sync/app/api/process.py`](../../juris-sync/app/api/process.py) (rota `stats/por-assunto`) |
| RN15 - jurimetria local | Análise sempre sobre base persistida | [`juris-sync/docs/requisitos.md`](../../juris-sync/docs/requisitos.md#rn15---jurimetria-é-sempre-sobre-a-base-local) |
| Testes dos endpoints de stats | Comportamento validado | [`juris-sync/tests/test_api.py`](../../juris-sync/tests/test_api.py) (`test_api_jurimetria_stats_endpoints`) |
| Case study - seção jurimetria | Contexto de negócio | [`case-study-juris-sync.md`](case-study-juris-sync.md#3-solução) |

**Endpoints:**

| Método | Rota | Descrição |
|--------|------|-----------|
| `GET` | `/api/v1/processos/stats/por-tribunal` | Contagem de processos por tribunal |
| `GET` | `/api/v1/processos/stats/por-assunto` | Contagem de processos por assunto |

**Exemplo citável:** *"Jurimetria via agregações SQL sobre a base local, sem nova consulta ao DataJud a cada análise."*

---

## Mapa rápido: competência → artefato

```mermaid
graph LR
    PM[Gestão de produto] --> REQ[requisitos.md]
    PM --> CS[case-study]
    PM --> ROAD[roadmap sprints]

    DEV[Desenvolvimento] --> APP[app/]
    DEV --> DOCKER[Docker + CI]

    QA[Automação de testes] --> TESTS[tests/]
    QA --> CI[GitHub Actions]

    DATA[Eng. dados] --> SYNC[sync_service]
    DATA --> ALEMBIC[alembic/]

    ANALISE[Análise] --> STATS[stats endpoints]
    ANALISE --> RN15[RN15]
```

---

## Próximas evidências (opcional)

| Item | Status |
|------|--------|
| Site live | https://mariahilmar-portfolio.vercel.app |
| Screenshots locais (Swagger, CI) | Instruções em [`docs/assets/README.md`](assets/README.md) |
| Domínio customizado | Opcional |
| API demo pública | Não implantada (sob pedido) |

---

*Documento elaborado na Fase 3 do hub de portfólio. Última atualização: 2026-07-20.*
