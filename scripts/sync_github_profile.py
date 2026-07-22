# -*- coding: utf-8 -*-
"""Alinha bio, README do perfil e pins do GitHub."""
from __future__ import annotations

import base64
import json
import subprocess
import sys


def gh_api(args: list[str], input_data: str | None = None) -> dict | list | str:
    result = subprocess.run(
        ["gh", "api", *args],
        input=input_data,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if result.returncode != 0:
        print("ERR:", result.stderr or result.stdout, file=sys.stderr)
        raise SystemExit(result.returncode)
    if not result.stdout.strip():
        return {}
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError:
        return result.stdout


def main() -> None:
    bio = (
        "Product Manager / Product Owner | Dados e IA | Base técnica em Python "
        "| Portfolio: mariahilmar.vercel.app"
    )

    print("1) Bio do perfil...")
    user = gh_api(
        [
            "--method",
            "PATCH",
            "user",
            "-f",
            f"bio={bio}",
            "-f",
            "blog=https://mariahilmar.vercel.app",
            "-f",
            "location=João Pessoa, PB",
        ]
    )
    print("   bio =", user.get("bio") if isinstance(user, dict) else user)

    print("2) README do perfil...")
    profile_readme = """# Olá, eu sou a Maria Hilmar

**Product Manager / Product Owner | Dados e IA | Base técnica em Python**

Liderança de produto em squads ágeis (SaaS B2B e sistemas governamentais), com projetos hands-on em Python, FastAPI, pipelines e fundamentos de IA.

## Links

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mariahilmar/)
[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://mariahilmar.vercel.app)
[![E-mail](https://img.shields.io/badge/E--mail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:mariahilmar@gmail.com)

## Em destaque

| Projeto | O que é |
|---------|---------|
| **Situação Jurídica** | jurimetria e benchmarking (FastAPI, Next.js, XGBoost, ML) |
| [juris-sync](https://github.com/MariaHilmar/juris-sync) | API FastAPI + ETL + testes em camadas |
| [juris-sync-web](https://github.com/MariaHilmar/juris-sync-web) | Dashboard Next.js de jurimetria |
| [paycore](https://github.com/MariaHilmar/paycore) | Ledger fintech: double-entry, PIX mock, 33 testes |
| [mgi-kpi-dashboard](https://github.com/MariaHilmar/mgi-kpi-dashboard) | BI de engenharia (demo live) |

## Stack em prática

Python, FastAPI, TypeScript, Next.js, Redis, Docker, XGBoost, React, Tailwind CSS, pytest, Vitest, Sentry
"""
    current = gh_api(["repos/MariaHilmar/MariaHilmar/contents/README.md"])
    sha = current["sha"]
    content_b64 = base64.b64encode(profile_readme.encode("utf-8")).decode("ascii")
    payload = json.dumps(
        {
            "message": "docs: alinhar README do perfil ao posicionamento PM/PO Dados e IA",
            "content": content_b64,
            "sha": sha,
        }
    )
    gh_api(
        [
            "--method",
            "PUT",
            "repos/MariaHilmar/MariaHilmar/contents/README.md",
            "--input",
            "-",
        ],
        input_data=payload,
    )
    print("   README atualizado")

    print("3) Pins...")
    q = """
    query {
      viewer {
        maria: repository(name: "maria-portfolio") { id name }
        juris: repository(name: "juris-sync") { id name }
        jurisWeb: repository(name: "juris-sync-web") { id name }
        paycore: repository(name: "paycore") { id name }
        mgiDash: repository(name: "mgi-kpi-dashboard") { id name }
        mgiPipe: repository(name: "mgi-kpi-pipeline") { id name }
      }
    }
    """
    data = gh_api(["graphql", "-f", f"query={q}"])
    viewer = data["data"]["viewer"]
    repo_ids = [
        viewer["maria"]["id"],
        viewer["juris"]["id"],
        viewer["jurisWeb"]["id"],
        viewer["paycore"]["id"],
        viewer["mgiDash"]["id"],
        viewer["mgiPipe"]["id"],
    ]
    names = [
        viewer["maria"]["name"],
        viewer["juris"]["name"],
        viewer["jurisWeb"]["name"],
        viewer["paycore"]["name"],
        viewer["mgiDash"]["name"],
        viewer["mgiPipe"]["name"],
    ]
    mut = """
    mutation($ids: [ID!]!) {
      updateItemsPinnedByViewer(input: {pinnedItemIds: $ids}) {
        clientMutationId
      }
    }
    """
    vars_json = json.dumps({"ids": repo_ids})
    pin = gh_api(
        ["graphql", "-f", f"query={mut}", "-f", f"variables={vars_json}"]
    )
    if isinstance(pin, dict) and pin.get("errors"):
        print("   aviso pins:", pin["errors"])
    else:
        print("   pinned:", ", ".join(names))

    print("\nOK - https://github.com/MariaHilmar")


if __name__ == "__main__":
    main()
