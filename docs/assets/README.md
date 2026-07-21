# Assets visuais - JurisSync

Evidências visuais referenciadas no [case study](../case-study-juris-sync.md).

## Evidências já disponíveis

| Evidência | Referência |
|-----------|------------|
| Site do portfólio | https://mariahilmar.vercel.app |
| CI (badge) | https://github.com/MariaHilmar/juris-sync/actions/workflows/ci.yml/badge.svg |
| Cobertura (badge) | ~89% no README do JurisSync |
| Jurimetria ilustrativa | Seção Análise do site (`#jurimetria`) |

## Screenshots opcionais (captura local)

Se quiser enriquecer o case study ou o site (Fase 4), capture e salve nesta pasta:

| Arquivo sugerido | Como capturar |
|------------------|---------------|
| `swagger-docs.png` | Suba a API (`python app/main.py` em `juris-sync/`) e abra http://localhost:8000/docs |
| `ci-green.png` | Acesse https://github.com/MariaHilmar/juris-sync/actions e capture um workflow verde |
| `pytest-coverage.png` | Rode `python -m pytest --cov=app --cov-report=term-missing` e capture o terminal |

### Passo a passo - Swagger

```powershell
cd juris-sync
.venv\Scripts\Activate.ps1
alembic upgrade head
python app/main.py
```

Abra http://localhost:8000/docs no navegador e salve a captura como `swagger-docs.png` nesta pasta.

### Passo a passo - CI

1. Acesse https://github.com/MariaHilmar/juris-sync/actions
2. Abra o último workflow com status verde
3. Capture a tela dos 3 jobs (Lint, Test, Integration)
4. Salve como `ci-green.png`

## Uso no case study

Após capturar, adicione no `case-study-juris-sync.md`:

```markdown
![Swagger UI](assets/swagger-docs.png)
![CI verde](assets/ci-green.png)
```
