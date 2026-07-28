# -*- coding: utf-8 -*-
"""Conteúdo dos currículos ATS.

Versões:
- LEAD_TECH_PM_ENGINEER: alinhada ao site (mariahilmar.vercel.app) - Lead Tech PM / Engineer
- PM_TECH_PM: candidaturas Product Manager / Tech PM / PO
- QA_REQUISITOS: candidaturas Analista de Requisitos / QA
"""

CONTACT = {
    "name": "Maria Hilmar Gomes da Silva",
    "location": "João Pessoa, PB | Disponível para atuação remota",
    "phone": "(61) 98206-2117",
    "email": "mariahilmar@gmail.com",
    "linkedin": "linkedin.com/in/mariahilmar",
    "github": "github.com/MariaHilmar",
    "portfolio": "mariahilmar.vercel.app",
}

EDUCATION = [
    "MBA em Ciência de Dados: Business Intelligence, Big Data e Analytics - Faculdade Anhanguera - 2025",
    "MBA em Gestão de Projetos e Metodologias Ágeis - Faculdade Anhanguera - 2025",
    "MBA em Teste de Software - Unieuro - 2012",
    "Graduação em Análise de Sistemas - Instituto Nossa Senhora de Fátima - 2011",
]

CERTIFICATIONS = [
    "CSPO (Certified Product Owner) - Scrum Alliance",
    "PSM I (Professional Scrum Master) - Scrum.org",
    "CTAL-TM (Certified Tester Advanced Level - Test Manager) - ISTQB",
    "Management 3.0",
]

# Versão do site / Featured do LinkedIn (público técnico)
LEAD_TECH_PM_ENGINEER = {
    "subtitle": "Lead Tech PM | Product Manager / Engineer (Dados & IA)",
    "summary": (
        "Líder de Produto e Engenharia na intersecção entre dados, IA e software. Mais de 15 anos "
        "em produtos digitais de alta complexidade (SaaS B2B, Real Estate e govtech), com gestão "
        "de squads ágeis, arquitetura de soluções e atuação hands-on em Python e FastAPI. "
        "Histórico de 9 anos na DFimoveis.com estruturando 6 produtos do zero ao Go-live "
        "(OKRs, cerca de 95% de entrega e redução de 15% no churn). Hoje atuo na Qintess em "
        "sistemas governamentais críticos e, em paralelo, no projeto próprio Situação Jurídica "
        "(jurimetria, APIs, pipelines e fundamentos de IA). Evidências públicas em "
        "mariahilmar.vercel.app e github.com/MariaHilmar. CSPO, PSM I e CTAL-TM."
    ),
    "skills": [
        (
            "Liderança e Produto: Tech Lead, Product Management, Roadmapping, Discovery, MVP, "
            "OKR, KPI, ROI, Stakeholder Management, Scrum, Kanban, Management 3.0"
        ),
        (
            "Engenharia e Arquitetura: Python, FastAPI, PostgreSQL, Redis, Docker, APIs REST, "
            "SQLAlchemy, Alembic, CI/CD, GitHub Actions, Next.js, Multi-tenant, RLS, LGPD"
        ),
        (
            "Dados e IA: ETL, SQL, Azure Data Factory, Power BI, Machine Learning, XGBoost, "
            "NLP, pgvector, LLM, RAG, Pipelines Staging/Serving"
        ),
        (
            "Requisitos e Qualidade: BDD, Gherkin, BPMN, UML, C4 Model, APF, QA, Testcontainers, "
            "Schemathesis, OpenAPI, Homologação"
        ),
    ],
    "experience": [
        {
            "title": "Scrum Master / Analista de Sistemas Sênior",
            "company": "Qintess",
            "period": "04/2025 - Presente | Remoto | PJ",
            "bullets": [
                (
                    "Facilitação ágil (Scrum/Kanban) e acompanhamento de Velocity e Lead Time "
                    "em squads de sistemas governamentais críticos."
                ),
                (
                    "Refinamento técnico de backlogs de alta complexidade: eNatJus 4.0, Portal "
                    "de Arrecadação e SAPRE (TJBA e MGI)."
                ),
                (
                    "Tradução de regulamentações em User Stories com BDD, BPMN/UML e "
                    "prototipação em Figma, reduzindo ambiguidade de escopo."
                ),
                (
                    "Aplicação de Análise de Pontos de Função (APF) para medição funcional e "
                    "aderência a critérios de auditoria pública."
                ),
            ],
        },
        {
            "title": "Gerente de Produtos / Product Owner Sênior",
            "company": "DFimoveis.com (Timipro)",
            "period": "02/2016 - 01/2025 | Remoto",
            "bullets": [
                (
                    "Estruturação do portfólio digital do zero: 6 produtos SaaS e Real Estate "
                    "de alta volumetria, do Discovery ao Go-live."
                ),
                (
                    "Liderança de squads multifuncionais (Scrum/Kanban) com retenção de "
                    "talentos técnicos acima de 90% e OKRs com cerca de 95% de entrega."
                ),
                (
                    "Concepção de produto de inteligência analítica para predição de preços, "
                    "com pipelines ETL (Azure Data Factory), SQL e dashboards no portal."
                ),
                (
                    "Integração de dados e CRM (HubSpot) entre Vendas, Financeiro, CS e TI, "
                    "com redução de cerca de 15% no churn."
                ),
                (
                    "Validação de APIs REST, testes ponta a ponta e iniciativas de SEO "
                    "(+15% acessos orgânicos, +20% conversão de leads)."
                ),
            ],
        },
        {
            "title": "Gerente de Produtos / Product Owner",
            "company": "Wimoveis",
            "period": "01/2012 - 05/2015 | Brasília, DF",
            "bullets": [
                (
                    "Modernização de sistemas fiscais e financeiros (NF-e, NFS-e, faturamento), "
                    "com redução de cerca de 95% nos erros de conciliação."
                ),
                (
                    "Liderança de time e BI (SQL Server, Excel Avançado/Power Pivot), "
                    "reduzindo cerca de 30% o SLA de atendimento."
                ),
                (
                    "Levantamento e documentação de requisitos com Casos de Uso, UML e BPMN."
                ),
            ],
        },
        {
            "title": "Analista de Requisitos / Garantia de Qualidade (QA)",
            "company": "Politec",
            "period": "01/2002 - 12/2011 | Brasília, DF",
            "bullets": [
                (
                    "Engenharia de requisitos e QA em projetos críticos para Banco do Brasil, "
                    "Petrobras e CNJ; atuação também em Linkdata e Cast no mesmo período."
                ),
            ],
        },
    ],
    "projects_heading": "Projetos",
    "projects": [
        {
            "title": "Lead de Produto e Engenharia (projeto próprio)",
            "company": "Situação Jurídica",
            "period": "01/2025 - Presente | Projeto pessoal | Evidências: github.com/MariaHilmar",
            "note": (
                "Produto próprio de jurimetria e dados jurídicos (não é vínculo empregatício). "
                "Código privado; evidências técnicas públicas em recortes independentes de portfólio."
            ),
            "bullets": [
                (
                    "Arquitetura e desenvolvimento hands-on: Python, FastAPI, PostgreSQL, Redis, "
                    "Next.js, autenticação JWT/SSO e isolamento multi-tenant (RLS / LGPD)."
                ),
                (
                    "Pipelines de dados Staging/ETL versus Serving, com redução de cerca de 60% "
                    "na latência das consultas no ambiente do projeto."
                ),
                (
                    "IA aplicada: Machine Learning (XGBoost), NLP, busca vetorial (pgvector) e "
                    "estratégias LLM/RAG para jurimetria preditiva."
                ),
                (
                    "Governança de requisitos e qualidade com BDD; evidências públicas: JurisSync "
                    "(43 testes em 5 camadas), PayCore e MGI KPI em mariahilmar.vercel.app."
                ),
            ],
        },
    ],
}

PM_TECH_PM = {
    "subtitle": "Product Manager / Tech PM | SaaS B2B, Dados e IA",
    "summary": (
        "Product Manager e Product Owner sênior com mais de 15 anos em produtos digitais de alta "
        "complexidade (SaaS B2B, Real Estate e govtech). Liderei por 9 anos o portfólio da "
        "DFimoveis.com, estruturando 6 produtos do zero ao Go-live, com OKRs, squads ágeis e "
        "entrega orientada a resultado (cerca de 95% dos resultados-chave e redução de 15% no "
        "churn). Atuo hoje na Qintess em sistemas governamentais críticos. Combino visão de "
        "produto e stakeholders com base técnica hands-on em dados, APIs e IA (projeto próprio "
        "Situação Jurídica e portfólio público em mariahilmar.vercel.app). CSPO, PSM I e CTAL-TM."
    ),
    "skills": [
        (
            "Gestão de Produto: Continuous Product Discovery, MVP, Roadmapping, Backlog, ROI, "
            "OKR, KPI, NPS, Churn, LTV, Stakeholder Management, Scrum, Kanban, Lean, Management 3.0"
        ),
        (
            "Requisitos e Qualidade: BDD, Gherkin, User Stories, BPMN, UML, C4 Model, APF, "
            "QA, Validação de APIs, Homologação"
        ),
        (
            "Dados e IA: ETL, SQL, Power BI, Azure Data Factory, Python, FastAPI, PostgreSQL, "
            "Docker, Machine Learning, XGBoost, NLP, pgvector, LLM, RAG"
        ),
        (
            "Ferramentas: Jira, Confluence, Figma, Miro, HubSpot, Git, GitHub, CI/CD, Next.js, Redis"
        ),
    ],
    "experience": [
        {
            "title": "Scrum Master / Analista de Sistemas Sênior",
            "company": "Qintess",
            "period": "04/2025 - Presente | Remoto | PJ",
            "bullets": [
                (
                    "Facilitação ágil (Scrum e Kanban), remoção de impedimentos e acompanhamento "
                    "de Velocity e Lead Time em squads de sistemas governamentais."
                ),
                (
                    "Refinamento de backlogs de alta complexidade em plataformas críticas: "
                    "eNatJus 4.0, Portal de Arrecadação e SAPRE (TJBA e MGI)."
                ),
                (
                    "Tradução de regulamentações em User Stories com BDD, BPMN/UML e "
                    "prototipação em Figma, reduzindo ambiguidade de escopo."
                ),
                (
                    "Aplicação de Análise de Pontos de Função (APF) para medição funcional e "
                    "aderência a critérios de auditoria pública."
                ),
            ],
        },
        {
            "title": "Gerente de Produtos / Product Owner Sênior",
            "company": "DFimoveis.com (Timipro)",
            "period": "02/2016 - 01/2025 | Remoto",
            "bullets": [
                (
                    "Estruturação do portfólio digital do zero, com consolidação de 6 produtos "
                    "SaaS e Real Estate de alta volumetria, do Discovery ao Go-live."
                ),
                (
                    "Liderança de squads multifuncionais sob Scrum e Kanban, com taxa de "
                    "retenção de talentos técnicos acima de 90%."
                ),
                (
                    "Implantação de OKRs com adesão corporativa e cerca de 95% de entrega "
                    "histórica dos resultados-chave."
                ),
                (
                    "Concepção de produto de inteligência analítica para predição de preços "
                    "imobiliários, com pipelines ETL (Azure Data Factory), SQL e dashboards."
                ),
                (
                    "Integração do ecossistema de dados e CRM (HubSpot) entre Vendas, "
                    "Financeiro, Customer Success e TI, com redução de cerca de 15% no churn."
                ),
                (
                    "Iniciativas de SEO com aumento de 15% nos acessos orgânicos e 20% na "
                    "conversão de leads; validação de APIs REST e testes ponta a ponta."
                ),
            ],
        },
        {
            "title": "Gerente de Produtos / Product Owner",
            "company": "Wimoveis",
            "period": "01/2012 - 05/2015 | Brasília, DF",
            "bullets": [
                (
                    "Modernização de sistemas fiscais e financeiros (NF-e, NFS-e, faturamento, "
                    "contas a pagar/receber), com redução de cerca de 95% nos erros de conciliação."
                ),
                (
                    "Liderança de time multifuncional e BI (SQL Server, Excel Avançado/Power "
                    "Pivot), reduzindo cerca de 30% o tempo de atendimento (SLA) e aumentando "
                    "25% as vendas no primeiro ano."
                ),
                (
                    "Levantamento e documentação de requisitos complexos com Casos de Uso, UML "
                    "e BPMN."
                ),
            ],
        },
        {
            "title": "Analista de Requisitos / Garantia de Qualidade (QA)",
            "company": "Politec",
            "period": "01/2002 - 12/2011 | Brasília, DF",
            "bullets": [
                (
                    "Engenharia de requisitos e QA em projetos críticos para Banco do Brasil, "
                    "Petrobras e CNJ, com homologação funcional e padronização de documentação."
                ),
                (
                    "Atuação também em Linkdata e Cast no mesmo período, incluindo padronização "
                    "de testes no Banco do Brasil (Cast)."
                ),
            ],
        },
    ],
    "projects_heading": "Projetos",
    "projects": [
        {
            "title": "Product Lead / Engenharia de Produto (projeto próprio)",
            "company": "Situação Jurídica",
            "period": "01/2025 - Presente | Projeto pessoal | Evidências: github.com/MariaHilmar",
            "note": (
                "Produto próprio de jurimetria e dados jurídicos (não é vínculo empregatício). "
                "Consolida autonomia técnica em produto, APIs, pipelines e fundamentos de IA."
            ),
            "bullets": [
                (
                    "Roadmap, discovery e arquitetura de plataforma SaaS B2B de jurimetria e "
                    "processamento de dados jurídicos."
                ),
                (
                    "Implementação hands-on com FastAPI, PostgreSQL, Redis e Next.js; pipelines "
                    "Staging/ETL versus Serving com redução de cerca de 60% na latência."
                ),
                (
                    "Governança de requisitos e documentação com BDD; exploração de ML "
                    "(XGBoost), NLP, pgvector e LLM/RAG."
                ),
                (
                    "Artefatos públicos: JurisSync, PayCore e MGI KPI em mariahilmar.vercel.app."
                ),
            ],
        },
    ],
}

QA_REQUISITOS = {
    "subtitle": "Analista de Requisitos e Qualidade de Software Sênior | CTAL-TM",
    "summary": (
        "Analista de Requisitos e Líder de Qualidade com mais de 15 anos em sistemas corporativos "
        "e governamentais de grande porte. Certificação CTAL-TM (ISTQB), CSPO e PSM I. Especialista "
        "em engenharia de requisitos (BDD/Gherkin, BPMN, UML, APF), homologação funcional, "
        "rastreabilidade requisito-teste e governança de qualidade. Atuo na Qintess em backlog "
        "crítico (eNatJus 4.0, SAPRE, TJBA e MGI). Histórico em BB, Petrobras e CNJ. Projeto "
        "próprio com evidências públicas de testes automatizados (43 testes em 5 camadas no "
        "JurisSync)."
    ),
    "skills": [
        (
            "Engenharia de Requisitos: Levantamento de Requisitos, Refinamento, User Stories, "
            "INVEST, BDD, Gherkin, Casos de Uso, BPMN, UML, C4 Model, APF, Figma, Miro"
        ),
        (
            "Qualidade e Testes: CTAL-TM, Estratégia de QA, Planos de Teste, Casos de Teste, "
            "Homologação Funcional, Validação de APIs REST, Rastreabilidade, Mitigação de Riscos"
        ),
        (
            "Automação e Evidências: pytest, Testcontainers, Schemathesis, Contract Testing, "
            "GitHub Actions, CI/CD, OpenAPI"
        ),
        (
            "Ferramentas e Contexto: Jira, Confluence, Scrum, Kanban, SQL, Sistemas Fiscais, "
            "Integrações Corporativas, GovTech"
        ),
    ],
    "experience": [
        {
            "title": "Scrum Master / Analista de Sistemas Sênior",
            "company": "Qintess",
            "period": "04/2025 - Presente | Remoto | PJ",
            "bullets": [
                (
                    "Levantamento, refinamento e mapeamento técnico de backlogs em sistemas "
                    "governamentais críticos: eNatJus 4.0, Portal de Arrecadação e SAPRE "
                    "(TJBA e MGI)."
                ),
                (
                    "Elaboração de User Stories com critérios de aceite em BDD (Gherkin), "
                    "modelagem BPMN/UML e prototipação em Figma para eliminar ambiguidades."
                ),
                (
                    "Aplicação de Análise de Pontos de Função (APF) para medição do tamanho "
                    "funcional e conformidade com critérios de auditoria pública."
                ),
                (
                    "Facilitação ágil (Scrum/Kanban), remoção de impedimentos e acompanhamento "
                    "de métricas de eficiência (Velocity e Lead Time)."
                ),
            ],
        },
        {
            "title": "Gerente de Produtos / Analista de Sistemas Sênior",
            "company": "DFimoveis.com (Timipro)",
            "period": "02/2016 - 01/2025 | Remoto",
            "bullets": [
                (
                    "Mapeamento de jornadas de usuário e especificação de requisitos funcionais "
                    "e não funcionais para 6 produtos SaaS corporativos de alta volumetria."
                ),
                (
                    "Concepção de regras de negócio complexas (NF-e/NFS-e, faturamento, CRM e "
                    "integrações), com User Stories em BDD, UML/BPMN e prototipação em Figma."
                ),
                (
                    "Garantia da integridade técnica do ecossistema por validação de APIs REST "
                    "e testes ponta a ponta em releases de produto."
                ),
                (
                    "Governança de entrega com OKRs e coordenação de squads ágeis (Scrum/Kanban) "
                    "do Discovery à homologação."
                ),
            ],
        },
        {
            "title": "Gerente de Produtos / Analista de Requisitos",
            "company": "Wimoveis",
            "period": "01/2012 - 05/2015 | Brasília, DF",
            "bullets": [
                (
                    "Levantamento e especificação de regras de negócio para sistemas fiscais e "
                    "financeiros (NF-e, contas a pagar/receber), com redução de cerca de 95% "
                    "nos erros de conciliação."
                ),
                (
                    "Desenho de Casos de Uso, fluxogramas, UML/BPMN e homologação funcional "
                    "junto aos usuários de negócio."
                ),
                (
                    "Reestruturação de processos de atendimento com dashboards de performance, "
                    "reduzindo cerca de 30% o SLA de suporte."
                ),
            ],
        },
        {
            "title": "Analista de Requisitos / Garantia de Qualidade (QA)",
            "company": "Politec",
            "period": "01/2002 - 12/2011 | Brasília, DF",
            "bullets": [
                (
                    "Engenharia de software, mapeamento de requisitos e QA em sistemas críticos "
                    "para Banco do Brasil, Petrobras e CNJ."
                ),
                (
                    "Atuação também em Linkdata e Cast no mesmo período; integração à primeira "
                    "equipe de testes do Banco do Brasil na Cast, com padronização de documentação."
                ),
                (
                    "Condução da esteira completa de testes: planos, cenários, homologações "
                    "funcionais e validação com usuários de negócio."
                ),
            ],
        },
    ],
    "projects_heading": "Projetos",
    "projects": [
        {
            "title": "Engenharia de Requisitos e Qualidade (projeto próprio)",
            "company": "Situação Jurídica",
            "period": "01/2025 - Presente | Projeto pessoal | Evidências: github.com/MariaHilmar",
            "note": (
                "Produto próprio de jurimetria (não é vínculo empregatício). Foco em governança "
                "de requisitos, critérios de aceite e qualidade verificável em repositórios públicos."
            ),
            "bullets": [
                (
                    "Estruturação de governança de documentação técnica e requisitos com critérios "
                    "BDD (Gherkin), fluxos operacionais e contratos de APIs RESTful."
                ),
                (
                    "Rastreabilidade requisito-código-teste documentada; redução de cerca de 70% "
                    "do esforço de especificação no ciclo do projeto."
                ),
                (
                    "Evidência pública JurisSync: 43 testes automatizados em 5 camadas (unitário, "
                    "API, mock HTTP, reconciliação, integração Postgres e contrato OpenAPI com "
                    "Schemathesis), com cerca de 90% de cobertura."
                ),
                (
                    "Homologação e validação de integrações de dados (DataJud/CNJ) com pipeline "
                    "idempotente e testes de reconciliação."
                ),
            ],
        },
    ],
}
