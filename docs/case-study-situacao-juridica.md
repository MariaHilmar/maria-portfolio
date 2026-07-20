# Case study: Situação Jurídica (produto próprio)

> **Produto privado** | Código e operação não são públicos | Evidências técnicas públicas: [JurisSync](https://github.com/MariaHilmar/juris-sync) e [MGI KPI](https://github.com/MariaHilmar/mgi-kpi-dashboard) (recorte independente, não o produto)

**Escopo deste documento:** narrativa de produto e mapa de capacidades, sem exposição de repositórios privados, credenciais, dados de clientes ou detalhes internos de implementação.

---

## 1. Contexto e problema

Escritórios, departamentos jurídicos e times de compliance precisam acompanhar processos, medir risco e apoiar decisões com dados. O mercado jurídico brasileiro concentra informação em fontes heterogêneas; transformar isso em produto confiável exige:

- Ingestão e normalização de dados processuais
- Separação clara entre staging, serving e camadas analíticas
- APIs e interfaces para métricas, risco e consulta
- Isolamento multi-tenant e conformidade com LGPD
- Proximidade entre produto, dados e engenharia

## 2. Papel

Atuação como **Product Owner / Product Lead com base técnica** em produto próprio de estudo (não é vínculo empregatício):

- Definição de visão, roadmap e priorização
- Engenharia de requisitos e alinhamento com arquitetura
- Governança de qualidade, segurança e documentação
- Validação de decisões de dados, APIs e jornadas

## 3. Visão do ecossistema (alto nível)

Arquitetura em caixas - sem detalhar código privado:

```text
Fontes externas / coleta
        ↓
  Staging / raw
        ↓
  Serving (API + banco multi-tenant)
        ↓
  ┌─────────────┬──────────────┬────────────┐
  Analytics/BI  Apps (web)     ML / busca
  └─────────────┴──────────────┴────────────┘
```

**Stack do produto (resumo, sem repositórios):** Python, FastAPI, PostgreSQL/Supabase, RLS, Redis, Next.js, pipelines de dados, fundamentos de ML e busca vetorial, documentação e CI.

## 4. Mapa de capacidades

O que o trabalho no Situação Jurídica demonstra - e onde o portfólio público oferece prova parcial:

| Capacidade | No produto (privado) | Evidência pública (recorte) |
|------------|----------------------|-----------------------------|
| Gestão de produto e requisitos | Roadmap, BDD, priorização | Case e requisitos do JurisSync |
| API backend | FastAPI, contratos, auth | [juris-sync](https://github.com/MariaHilmar/juris-sync) |
| Frontend de dados | Apps web Next.js | [juris-sync-web](https://github.com/MariaHilmar/juris-sync-web) |
| Engenharia de dados / BI | Pipelines, staging vs serving | [mgi-kpi-pipeline](https://github.com/MariaHilmar/mgi-kpi-pipeline) + dashboard |
| Multi-tenant, RLS, LGPD | Privacy by Design no produto | Narrativa neste case (código privado) |
| ML / RAG / jurimetria preditiva | Modelos e busca no produto | Narrativa + estudos em APIs públicas do portfólio |
| Qualidade e testes | Governança no ciclo do produto | Suítes e CI nos repos públicos |

**Importante:** JurisSync e MGI KPI **não** são o Situação Jurídica. São projetos públicos no mesmo domínio ou em BI de engenharia, usados para mostrar profundidade técnica sem abrir o código do produto.

## 5. Resultados (ambiente do produto)

Resultados observados no ciclo do projeto próprio (não são métricas de cliente externo publicado):

- Otimização de latência em consultas após segregação staging/ETL versus serving (~60% no ambiente do projeto)
- Redução relevante do esforço de especificação com fluxos de documentação e critérios BDD assistidos por IA (~70% no ciclo do projeto)
- Modelagem com isolamento multi-tenant (RLS) e premissas de Privacy by Design / LGPD

## 6. O que permanece privado

- Código-fonte e repositórios do produto
- Credenciais, chaves e configurações de infraestrutura
- Dados reais de processos, clientes ou tenants
- Runbooks internos e detalhes de schema além do necessário para a narrativa

## 7. Como avaliar minha profundidade técnica

1. Ler este case (amplitude e decisões de produto)
2. Clonar e rodar [JurisSync](https://github.com/MariaHilmar/juris-sync) + [juris-sync-web](https://github.com/MariaHilmar/juris-sync-web) (API, testes, docs)
3. Explorar [MGI KPI](https://web-mgi-delog.vercel.app) (ETL + dashboard)
4. Ver o hub: [mariahilmar-portfolio.vercel.app](https://mariahilmar-portfolio.vercel.app)

---

*Documento público de portfólio. Atualizado para deixar explícita a fronteira entre produto privado e evidências abertas.*
