# Manual de Posicionamento e Busca de Emprego

**Maria Hilmar Gomes da Silva**  
Atualizado: 28/07/2026

Este documento reúne, em um só lugar:

- Estratégia de candidatura (PM / Tech PM + QA / Requisitos)
- Como usar os currículos ATS
- Textos prontos do LinkedIn (headline, Sobre, experiências)
- Situação Jurídica como projeto próprio
- Como regenerar os currículos
- Checklist semanal e mensagens para recrutadores

Portfólio: [mariahilmar.vercel.app](https://mariahilmar.vercel.app)  
GitHub: [github.com/MariaHilmar](https://github.com/MariaHilmar)  
LinkedIn: [linkedin.com/in/mariahilmar](https://linkedin.com/in/mariahilmar)

---

## 1. Diagnóstico (o que estava acontecendo)

### Problema principal

Não era falta de experiência. Era **posicionamento confuso**.

Sinais:

- Currículos de PM e QA quase iguais (só mudava o título)
- Resumo começando com "Líder de Produto" também na versão QA
- Situação Jurídica parecendo emprego formal ("Startup / Consultora")
- Dois "presente" sem contexto (Qintess + Situação Jurídica)
- Muita candidatura por Easy Apply, pouco retorno

### O que você tem de forte

- 9 anos como Gerente de Produtos / PO na DFimoveis (6 produtos SaaS)
- Atuação atual em govtech na Qintess (eNatJus, SAPRE, TJBA, MGI)
- CTAL-TM (ISTQB), CSPO, PSM I, Management 3.0
- Portfólio técnico acima da média (JurisSync, PayCore, MGI KPI)
- Histórico em BB, Petrobras e CNJ (requisitos e QA)

### Decisão estratégica

Concorrer em **duas frentes**, com materiais diferentes:

| Frente | Quando usar | Arquivo |
|--------|-------------|---------|
| PM / Tech PM | Product Manager, Tech PM, PO, Product Lead | `PM_Tech_PM_Maria_Hilmar_ATS` |
| Requisitos & QA | Analista de Requisitos, QA Sênior, Test Manager, Analista de Sistemas | `QA_Requisitos_Maria_Hilmar_ATS` |

**Não** criar currículo separado só de Requisitos e só de QA. Para o seu perfil, **Requisitos + QA juntos** é mais forte.

**Proporção sugerida (8-12 semanas):**

- 50-60% candidaturas QA / Requisitos
- 30-40% candidaturas PM / Tech PM
- 5 candidaturas **personalizadas** por semana valem mais que 30 Easy Apply

---

## 2. Situação Jurídica (regra de ouro)

### O que é

Produto / sistema **seu** (projeto próprio). Serve para mostrar experiência hands-on em desenvolvimento, requisitos, qualidade, dados e IA.

### O que NÃO é

- Emprego CLT
- Consultoria em startup de terceiros
- Vínculo empregatício paralelo "escondido"

### Como escrever sempre

Use sempre uma destas fórmulas:

- `projeto próprio`
- `produto próprio`
- `não é vínculo empregatício`

Evite:

- `Startup Situação Jurídica - Consultora...`
- Linguagem que pareça cargo corporativo em empresa alheia

### Ângulo por trilha

| Trilha | Como destacar |
|--------|----------------|
| PM / Tech PM | Roadmap, discovery, arquitetura de produto SaaS B2B |
| QA / Requisitos | BDD, rastreabilidade, testes, homologação (JurisSync) |
| Dev (se usar) | FastAPI, PostgreSQL, pipelines, CI, testes |

Código do produto: **privado**.  
Evidências públicas: JurisSync, PayCore, MGI KPI + site.

---

## 3. Currículos ATS

### Três versões (papel de cada uma)

| Versão | Uso | Arquivo |
|--------|-----|---------|
| **Lead Tech PM / Engineer** | Site + Featured LinkedIn (público técnico) | `Lead_Tech_PM_Engineer_Maria_Hilmar_ATS` + `web/public/MariaHilmar_Curriculo_ATS.pdf` |
| **PM / Tech PM** | Candidaturas Product Manager / PO | `PM_Tech_PM_Maria_Hilmar_ATS` |
| **QA / Requisitos** | Candidaturas Analista de Requisitos / QA | `QA_Requisitos_Maria_Hilmar_ATS` |

O botão **Baixar Currículo** do site aponta para a versão Lead Tech PM / Engineer.

### Onde estão

**No repositório:**

`maria-portfolio/docs/curriculos/`

- `Lead_Tech_PM_Engineer_Maria_Hilmar_ATS.docx` / `.pdf` / `.md`
- `PM_Tech_PM_Maria_Hilmar_ATS.docx` / `.pdf` / `.md`
- `QA_Requisitos_Maria_Hilmar_ATS.docx` / `.pdf` / `.md`

**Download do site:**

`maria-portfolio/web/public/MariaHilmar_Curriculo_ATS.pdf`

**Na Área de Trabalho:**

`Curriculos ATS\` (mesmos arquivos)

### Scripts (fluxo único)

| Arquivo | Função |
|---------|--------|
| `maria-portfolio/scripts/curriculos_ats_content.py` | Conteúdo editável (textos) |
| `maria-portfolio/scripts/generate_curriculos_ats.py` | Gera DOCX, PDF e MD |

O gerador antigo `generate_curriculo_ats.py` foi removido.

### Regenerar

```powershell
cd D:\git-portfolio\maria-portfolio\scripts
python generate_curriculos_ats.py
```

Dependências: `python-docx` e, para PDF, Word + `pywin32`.

### Padrões ATS aplicados

- Coluna única, alinhamento à esquerda
- Contato no corpo (não header/footer)
- Sem tabelas, imagens, bordas ou cores
- Fonte Calibri
- Datas no formato `MM/AAAA`
- Bullets em texto puro (`- `)
- Seções: Resumo → Experiência → Projetos → Formação → Habilidades → Certificações

### Palavras-chave

O script **não descobre** keywords sozinho. Elas estão fixas em `curriculos_ats_content.py`.

Para personalizar uma vaga:

1. Leia a descrição
2. Copie 5-10 termos importantes
3. Ajuste resumo / skills / 1-2 bullets no content
4. Regenere
5. Renomeie o arquivo com o título da vaga, ex.: `Maria_Hilmar_Product_Manager.docx`

### Ajuste rápido por vaga (2 minutos)

1. Subtítulo no topo = título da vaga
2. 2-3 palavras-chave da vaga no resumo
3. Reordene 1-2 bullets da experiência mais recente

---

## 4. LinkedIn - visão geral

### Regra

- **1 LinkedIn híbrido** (atrai PM e QA/Requisitos)
- **2 PDFs específicos** (um por tipo de vaga)

O LinkedIn conta a história completa. O PDF faz o recorte.

### Ordem para publicar

1. Headline
2. Sobre
3. Situação Jurídica (experiência)
4. Qintess (marcar PJ)
5. DFimoveis
6. Wimoveis e Politec (opcional revisar)
7. Skills (fixar top 5)
8. Featured / Destaques com portfólio

### Tipo de emprego no LinkedIn

| Experiência | Tipo sugerido |
|-------------|----------------|
| Qintess | Contrato / Autônomo / PJ (o que o LinkedIn permitir) |
| Situação Jurídica | Autônomo / Projeto próprio / Freelance |
| DFimoveis | Tempo integral (ou o que for verdade) |

---

## 5. LinkedIn - Headline

### Opção recomendada (híbrida)

```text
Product Manager / Analista de Requisitos & QA Sênior | SaaS B2B, GovTech, BDD | CSPO · CTAL-TM · PSM I | Python & Dados
```

### Alternativa mais PM

```text
Product Manager / Tech PM | SaaS B2B, Dados e IA | Ex-DFimoveis (9 anos) | CSPO · PSM I · CTAL-TM
```

### Alternativa mais QA / Requisitos

```text
Analista de Requisitos & QA Sênior | CTAL-TM | BDD, APF, Homologação | GovTech | CSPO · PSM I
```

**Use a híbrida no perfil.** Nas candidaturas, o PDF específico faz o recorte.

---

## 6. LinkedIn - Sobre (About)

Copie e cole:

```text
Product Manager / Product Owner e Analista de Requisitos & Qualidade, com mais de 15 anos em produtos digitais de alta complexidade (SaaS B2B, Real Estate e govtech).

Na DFimoveis.com (Timipro), liderei por 9 anos o portfólio de produto: 6 produtos SaaS do Discovery ao Go-live, implantação de OKRs (cerca de 95% de entrega dos resultados-chave), redução de cerca de 15% no churn e coordenação de squads ágeis com alta retenção de talentos.

Hoje atuo na Qintess como Scrum Master / Analista de Sistemas Sênior (PJ), em sistemas governamentais críticos (eNatJus 4.0, Portal de Arrecadação, SAPRE - TJBA e MGI): refinamento de backlog, User Stories em BDD (Gherkin), BPMN/UML, APF e métricas de entrega (Velocity e Lead Time).

Também trago base sólida em engenharia de requisitos e qualidade de software (CTAL-TM / ISTQB), com histórico em homologação e projetos críticos (Banco do Brasil, Petrobras e CNJ).

Em paralelo, desenvolvo Situação Jurídica - projeto próprio de jurimetria e dados jurídicos (não é vínculo empregatício). Uso esse trabalho para consolidar autonomia técnica em produto, requisitos, APIs, pipelines e fundamentos de IA. Evidências públicas: JurisSync, PayCore e MGI KPI.

Como atuo:
• Produto: discovery, roadmap, priorização por valor (ROI), OKRs e alinhamento com stakeholders
• Requisitos e QA: BDD/Gherkin, rastreabilidade, homologação, APF e governança de qualidade
• Base técnica: Python, FastAPI, SQL, dados e IA aplicada (portfólio público)

Certificações: CSPO (Scrum Alliance) | PSM I (Scrum.org) | CTAL-TM (ISTQB) | Management 3.0

Portfólio: mariahilmar.vercel.app
GitHub: github.com/MariaHilmar

Aberta a desafios remotos em Product Management / Tech PM, Analista de Requisitos e Qualidade de Software (QA).
```

---

## 7. LinkedIn - Situação Jurídica

### Campos

| Campo | Valor |
|--------|--------|
| Cargo | Product Lead / Engenharia de Produto (projeto próprio) |
| Tipo | Autônomo / Freelance / Projeto próprio |
| Empresa | Situação Jurídica |
| Local | Remoto |
| Período | jan/2025 - Presente |
| Emprego atual | Sim (em paralelo à Qintess) |

### Descrição

```text
Projeto próprio de jurimetria e dados jurídicos (não é vínculo empregatício).

Atuo ponta a ponta na concepção do produto e na entrega técnica:
• Roadmap, discovery e arquitetura de plataforma SaaS B2B de inteligência analítica jurídica
• Engenharia de requisitos com critérios de aceite em BDD (Gherkin), documentação e contratos de API
• Desenvolvimento hands-on: Python, FastAPI, PostgreSQL, Redis e Next.js
• Pipelines de dados (Staging/ETL vs Serving), com redução de cerca de 60% na latência no ambiente do projeto
• Exploração de ML (XGBoost), NLP, busca vetorial (pgvector) e estratégias LLM/RAG
• Governança de qualidade e evidências públicas de testes automatizados (JurisSync: 43 testes em 5 camadas, ~90% de cobertura)

Importante: o código do produto Situação Jurídica é privado. As evidências técnicas públicas são recortes independentes de portfólio:
• github.com/MariaHilmar/juris-sync
• github.com/MariaHilmar/paycore
• github.com/MariaHilmar/mgi-kpi-dashboard
• Portfólio: mariahilmar.vercel.app
```

---

## 8. LinkedIn - Qintess

### Campos

| Campo | Valor |
|--------|--------|
| Cargo | Scrum Master / Analista de Sistemas Sênior |
| Empresa | Qintess |
| Local | Remoto |
| Período | abr/2025 - Presente |
| Tipo | Contrato / PJ / Autônomo (conforme realidade) |

### Descrição

```text
Atuação como Scrum Master / Analista de Sistemas Sênior (PJ) em sistemas governamentais críticos.

• Facilitação ágil (Scrum e Kanban), remoção de impedimentos e acompanhamento de Velocity e Lead Time
• Refinamento e mapeamento técnico de backlogs de alta complexidade: eNatJus 4.0, Portal de Arrecadação e SAPRE (TJBA e MGI)
• Tradução de regulamentações em User Stories com critérios de aceite em BDD (Gherkin), modelagem BPMN/UML e prototipação em Figma
• Aplicação de Análise de Pontos de Função (APF) para medição funcional e aderência a critérios de auditoria pública
• Alinhamento contínuo entre negócio, engenharia e qualidade para reduzir ambiguidade de escopo e acelerar entrega
```

---

## 9. LinkedIn - DFimoveis.com (Timipro)

### Campos

| Campo | Valor |
|--------|--------|
| Cargo | Gerente de Produtos / Product Owner Sênior |
| Empresa | DFimoveis.com (Timipro) |
| Local | Remoto |
| Período | fev/2016 - jan/2025 |

### Descrição

```text
Liderança de produto por 9 anos em portfólio digital SaaS e Real Estate de alta volumetria.

• Estruturação do portfólio do zero, com consolidação de 6 produtos do Discovery ao Go-live
• Gestão de squads multifuncionais sob Scrum e Kanban, com retenção de talentos técnicos acima de 90%
• Implantação de OKRs com adesão corporativa e cerca de 95% de entrega histórica dos resultados-chave
• Concepção de produto de inteligência analítica para predição de preços imobiliários, com pipelines ETL (Azure Data Factory), SQL e dashboards
• Integração do ecossistema de dados e CRM (HubSpot) entre Vendas, Financeiro, Customer Success e TI, com redução de cerca de 15% no churn
• Engenharia de requisitos com User Stories em BDD, UML/BPMN e prototipação em Figma
• Validação de APIs REST, testes ponta a ponta e iniciativas de SEO (+15% acessos orgânicos, +20% conversão de leads)
```

---

## 10. LinkedIn - Wimoveis (opcional, recomendado)

### Campos

| Campo | Valor |
|--------|--------|
| Cargo | Gerente de Produtos / Product Owner |
| Empresa | Wimoveis |
| Local | Brasília, DF |
| Período | jan/2012 - mai/2015 |

### Descrição

```text
• Modernização de sistemas fiscais e financeiros (NF-e, NFS-e, faturamento, contas a pagar/receber), com redução de cerca de 95% nos erros de conciliação
• Liderança de time multifuncional e BI (SQL Server, Excel Avançado/Power Pivot), reduzindo cerca de 30% o SLA de atendimento e aumentando 25% as vendas no primeiro ano
• Levantamento e documentação de requisitos complexos com Casos de Uso, UML e BPMN
• Homologação funcional junto aos usuários de negócio
```

---

## 11. LinkedIn - Politec / Linkdata / Cast (opcional, importante para QA)

### Campos

| Campo | Valor |
|--------|--------|
| Cargo | Analista de Requisitos / Garantia de Qualidade (QA) |
| Empresa | Politec |
| Local | Brasília, DF |
| Período | jan/2002 - dez/2011 |

Se o LinkedIn não permitir múltiplas empresas no mesmo cargo, mantenha Politec como principal e cite Linkdata/Cast na descrição (como no currículo ATS).

### Descrição

```text
Engenharia de requisitos e garantia de qualidade em sistemas críticos de grande porte.

• Projetos para Banco do Brasil, Petrobras e CNJ
• Atuação também em Linkdata e Cast no mesmo período
• Integração à primeira equipe de testes do Banco do Brasil na Cast, com padronização de documentação de qualidade
• Esteira completa: levantamento de requisitos, Casos de Uso, planos e casos de teste, homologação funcional com usuários de negócio
```

---

## 12. LinkedIn - Skills e Featured

### Top 5 para fixar

1. Product Management  
2. Engenharia de Requisitos  
3. BDD / Gherkin (ou Behavior Driven Development)  
4. Agile / Scrum  
5. Quality Assurance / Test Management  

### Outras skills relevantes

APF, BPMN, UML, Jira, Confluence, Python, FastAPI, SQL, OKR, Stakeholder Management, Kanban, Homologação, ISTQB, Product Owner

### Featured / Destaques

Adicione links:

1. [mariahilmar.vercel.app](https://mariahilmar.vercel.app)
2. [github.com/MariaHilmar/juris-sync](https://github.com/MariaHilmar/juris-sync)
3. [github.com/MariaHilmar/paycore](https://github.com/MariaHilmar/paycore)
4. Demo MGI KPI (se estiver no ar)

---

## 13. Mensagens prontas para recrutadores

### QA / Requisitos

```text
Olá, [nome]. Vi a vaga de [cargo] na [empresa]. Tenho CTAL-TM, experiência em sistemas críticos (BB, Petrobras, CNJ) e atuo hoje na Qintess em backlog governamental (eNatJus/SAPRE) com BDD, APF e homologação. Também tenho base sólida em produto (9 anos na DFimoveis). Posso enviar currículo focado em requisitos/qualidade?
```

### PM / Tech PM

```text
Olá, [nome]. Vi a vaga de Product Manager na [empresa]. Liderei produto por 9 anos na DFimoveis (6 produtos SaaS, OKRs, -15% churn) e hoje atuo em govtech na Qintess. Tenho base técnica hands-on em projeto próprio (Python/FastAPI, dados e IA) com portfólio público em mariahilmar.vercel.app. Posso enviar um resumo alinhado à vaga?
```

### Pedido de indicação (ex-colegas)

```text
Oi, [nome]. Estou em busca de oportunidades em [PM / Requisitos / QA], remoto. Se souber de abertura na sua rede ou empresa, agradeço muito uma indicação. Posso te mandar um PDF de 2 páginas e o link do portfólio.
```

---

## 14. Estratégia semanal (execução)

### Meta realista

| Canal | Volume/semana | Observação |
|-------|---------------|------------|
| Candidaturas personalizadas | 5-10 | Sempre com o PDF certo |
| Mensagens a recrutadores / hiring managers | 10-15 | Texto curto + link |
| Pedidos de indicação | 2-5 | Ex-colegas DFimoveis / Qintess |
| Posts no LinkedIn | 2 | 1 produto + 1 requisitos/QA |

### Proporção de candidaturas

- 6 QA / Requisitos (PDF QA)
- 4 PM / Tech PM (PDF PM)

### O que NÃO fazer

1. Enviar PDF de PM para vaga de QA (e vice-versa)
2. Easy Apply em massa sem mensagem
3. Apresentar Situação Jurídica como emprego formal
4. Currículo genérico de 4 páginas
5. Headline só de uma trilha se você quer as duas

---

## 15. Empresas-alvo (direção)

### Mais aderentes agora

- Consultorias e integradores govtech
- Fábricas de software com contratos públicos
- SaaS B2B (imobiliário, jurídico, fintech, proptech)
- Times que pedem Analista de Requisitos + BDD / APF
- Vagas de QA sênior / Test Manager com foco em processo (não só automação júnior)

### Mais difíceis (sem descartar)

- Backend puro sem título prévio de desenvolvedora
- PM C-level altamente competitivo sem rede ativa

---

## 16. Plano de 30 dias

### Semana 1

- [ ] Publicar Headline híbrida
- [ ] Publicar Sobre
- [ ] Atualizar Situação Jurídica (projeto próprio)
- [ ] Atualizar Qintess (PJ)
- [ ] Atualizar DFimoveis
- [ ] Fixar Skills e Featured

### Semana 2

- [ ] Lista de 40 empresas (20 govtech/consultoria + 20 SaaS)
- [ ] 10 candidaturas QA + 5 PM com mensagem
- [ ] 10 abordagens a recrutadores

### Semana 3

- [ ] 5 pedidos de indicação
- [ ] 2 posts LinkedIn (1 QA/requisitos, 1 produto)
- [ ] Revisar respostas e ajustar PDF se necessário

### Semana 4

- [ ] Medir: visualizações, respostas, entrevistas por trilha
- [ ] Dobrar esforço na trilha que responder melhor
- [ ] Manter a outra trilha ativa (não zerar)

---

## 17. Checklist antes de cada candidatura

- [ ] Li a vaga e escolhi o PDF certo (PM ou QA/Requisitos)
- [ ] Renomeei o arquivo com meu nome + título da vaga
- [ ] Ajustei 2-3 keywords do anúncio no resumo/skills (se fizer sentido)
- [ ] Enviei mensagem curta (não só o botão Easy Apply)
- [ ] Situação Jurídica está descrita como projeto próprio no PDF e no LinkedIn

---

## 18. Arquivos e caminhos úteis

### README do hub (GitHub)

Caminho local:

`D:\git-portfolio\maria-portfolio\README.md`

No GitHub (após push): página inicial do repositório `maria-portfolio`.

Esse README é a porta de entrada para quem chega pelo Git - alinhado a PM/PO com base técnica. O **site** (`web/`) é a vitrine Lead Tech PM / Engineer para o Featured do LinkedIn.

### Estrutura

```text
D:\git-portfolio\maria-portfolio\
├── README.md                                # hub GitHub
├── docs\
│   ├── curriculos\                          # 3 versões ATS (DOCX/PDF/MD)
│   └── MANUAL_POSICIONAMENTO_LINKEDIN.md    # este manual
├── scripts\
│   ├── curriculos_ats_content.py            # editar textos aqui
│   └── generate_curriculos_ats.py           # gerar currículos (+ copia PDF do site)
└── web\
    ├── public\MariaHilmar_Curriculo_ATS.pdf # Baixar Currículo do site
    └── src\pages\index.astro                # vitrine Lead Tech PM
```

Portfólio: https://mariahilmar.vercel.app  
GitHub: https://github.com/MariaHilmar  
LinkedIn: https://linkedin.com/in/mariahilmar

---

## 19. Resumo em uma frase

**LinkedIn híbrido + 2 currículos ATS diferentes + Situação Jurídica como projeto próprio + candidaturas personalizadas (não só volume).**

Isso é o posicionamento. O retorno vem da execução semanal.
