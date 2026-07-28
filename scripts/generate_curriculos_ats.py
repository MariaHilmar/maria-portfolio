# -*- coding: utf-8 -*-
"""Gera currículos 100% ATS-friendly em Word (.docx) e PDF texto.

Padrões aplicados:
- Coluna única, alinhamento à esquerda
- Contato no corpo (não header/footer)
- Sem tabelas, text boxes, imagens, bordas ou cores
- Fonte Calibri 10-12pt
- Títulos de seção padrão
- Datas MM/AAAA
- Bullets em texto simples (- )
- Ordem: Contato > Resumo > Experiência > Projetos > Formação > Habilidades > Certificações
- Export .docx + PDF texto (quando Word estiver disponível)
"""
from __future__ import annotations

import sys
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from curriculos_ats_content import (  # noqa: E402
    CERTIFICATIONS,
    CONTACT,
    EDUCATION,
    LEAD_TECH_PM_ENGINEER,
    PM_TECH_PM,
    QA_REQUISITOS,
)

DEFAULT_OUT_DIR = SCRIPT_DIR.parent / "docs" / "curriculos"
SITE_PUBLIC_DIR = SCRIPT_DIR.parent / "web" / "public"
SITE_CV_STEM = "MariaHilmar_Curriculo_ATS"
DESKTOP_OUT_DIR = Path(r"C:\Users\maria\OneDrive\Área de Trabalho\Curriculos ATS")
BLACK = RGBColor(0, 0, 0)


def set_run_font(run, size=10.5, bold=False, name="Calibri"):
    run.font.name = name
    run._element.rPr.rFonts.set(qn("w:eastAsia"), name)
    run.font.size = Pt(size)
    run.bold = bold
    run.font.color.rgb = BLACK


class AtsResumeBuilder:
    def __init__(self):
        self.doc = Document()
        for section in self.doc.sections:
            section.top_margin = Inches(0.7)
            section.bottom_margin = Inches(0.7)
            section.left_margin = Inches(0.7)
            section.right_margin = Inches(0.7)
            section.page_width = Inches(8.27)
            section.page_height = Inches(11.69)
            # Garante header/footer vazios (ATS ignora/perde conteúdo nessas áreas)
            section.header.is_linked_to_previous = False
            section.footer.is_linked_to_previous = False

        style = self.doc.styles["Normal"]
        style.font.name = "Calibri"
        style.font.size = Pt(10.5)
        style.font.color.rgb = BLACK
        style._element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")

    def add_paragraph(
        self,
        text,
        size=10.5,
        bold=False,
        space_before=0,
        space_after=4,
    ):
        p = self.doc.add_paragraph()
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.left_indent = Inches(0)
        p.alignment = None  # left (default)
        run = p.add_run(text)
        set_run_font(run, size=size, bold=bold)
        return p

    def add_heading_ats(self, text):
        """Título de seção ATS: negrito, preto, sem borda e sem cor."""
        return self.add_paragraph(
            text.upper(),
            size=11,
            bold=True,
            space_before=10,
            space_after=4,
        )

    def add_job_header(self, title, company, period):
        self.add_paragraph(
            f"{title} | {company}",
            size=10.5,
            bold=True,
            space_before=8,
            space_after=1,
        )
        self.add_paragraph(period, size=10, bold=False, space_before=0, space_after=2)

    def add_bullet(self, text):
        """Bullet em texto puro (- ), sem estilo List Bullet do Word."""
        p = self.doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.left_indent = Inches(0.15)
        run = p.add_run(f"- {text}")
        set_run_font(run, size=10)
        return p

    def add_contact_header(self, subtitle: str):
        self.add_paragraph(CONTACT["name"], size=16, bold=True, space_after=2)
        self.add_paragraph(subtitle, size=11, bold=True, space_after=4)
        self.add_paragraph(CONTACT["location"], size=10, space_after=1)
        self.add_paragraph(f"Telefone: {CONTACT['phone']}", size=10, space_after=1)
        self.add_paragraph(f"E-mail: {CONTACT['email']}", size=10, space_after=1)
        self.add_paragraph(f"LinkedIn: {CONTACT['linkedin']}", size=10, space_after=1)
        self.add_paragraph(f"GitHub: {CONTACT['github']}", size=10, space_after=1)
        self.add_paragraph(f"Portfólio: {CONTACT['portfolio']}", size=10, space_after=4)

    def build(self, content: dict) -> Document:
        # Ordem ATS clássica e parseável
        self.add_contact_header(content["subtitle"])

        self.add_heading_ats("Resumo Profissional")
        self.add_paragraph(content["summary"], size=10.5, space_after=2)

        self.add_heading_ats("Experiência Profissional")
        for job in content["experience"]:
            self.add_job_header(job["title"], job["company"], job["period"])
            for bullet in job["bullets"]:
                self.add_bullet(bullet)

        self.add_heading_ats(content.get("projects_heading", "Projetos"))
        for project in content["projects"]:
            self.add_job_header(project["title"], project["company"], project["period"])
            if project.get("note"):
                self.add_paragraph(project["note"], size=10, space_after=2)
            for bullet in project["bullets"]:
                self.add_bullet(bullet)

        self.add_heading_ats("Formação Acadêmica")
        for item in EDUCATION:
            self.add_paragraph(item, size=10, space_after=2)

        self.add_heading_ats("Habilidades")
        for skill in content["skills"]:
            self.add_bullet(skill)

        self.add_heading_ats("Certificações")
        for item in CERTIFICATIONS:
            self.add_paragraph(item, size=10, space_after=1)

        return self.doc


def write_markdown(content: dict, path: Path):
    lines = [
        f"# {CONTACT['name']}",
        f"## {content['subtitle']}",
        "",
        CONTACT["location"],
        f"Telefone: {CONTACT['phone']}",
        f"E-mail: {CONTACT['email']}",
        f"LinkedIn: {CONTACT['linkedin']}",
        f"GitHub: {CONTACT['github']}",
        f"Portfólio: {CONTACT['portfolio']}",
        "",
        "## Resumo Profissional",
        "",
        content["summary"],
        "",
        "## Experiência Profissional",
        "",
    ]
    for job in content["experience"]:
        lines.append(f"### {job['title']} | {job['company']}")
        lines.append(job["period"])
        lines.append("")
        for bullet in job["bullets"]:
            lines.append(f"- {bullet}")
        lines.append("")
    lines.extend([f"## {content.get('projects_heading', 'Projetos')}", ""])
    for project in content["projects"]:
        lines.append(f"### {project['title']} | {project['company']}")
        lines.append(project["period"])
        if project.get("note"):
            lines.append("")
            lines.append(project["note"])
        lines.append("")
        for bullet in project["bullets"]:
            lines.append(f"- {bullet}")
        lines.append("")
    lines.extend(["## Formação Acadêmica", ""])
    for item in EDUCATION:
        lines.append(f"- {item}")
    lines.extend(["", "## Habilidades", ""])
    for skill in content["skills"]:
        lines.append(f"- {skill}")
    lines.extend(["", "## Certificações", ""])
    for item in CERTIFICATIONS:
        lines.append(f"- {item}")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def export_pdf_with_word(docx_path: Path, pdf_path: Path) -> bool:
    """Exporta PDF texto via Microsoft Word (Windows). Retorna True se ok."""
    try:
        import win32com.client  # type: ignore
    except ImportError:
        print(f"AVISO: pywin32 não instalado; PDF não gerado para {docx_path.name}")
        return False

    word = None
    try:
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False
        doc = word.Documents.Open(str(docx_path.resolve()))
        # 17 = wdFormatPDF
        doc.SaveAs(str(pdf_path.resolve()), FileFormat=17)
        doc.Close(False)
        return True
    except Exception as exc:  # noqa: BLE001
        print(f"AVISO: falha ao gerar PDF ({docx_path.name}): {exc}")
        return False
    finally:
        if word is not None:
            try:
                word.Quit()
            except Exception:  # noqa: BLE001
                pass


def generate_all(out_dirs: list[Path], also_pdf: bool = True):
    variants = [
        # Versão do site (Lead Tech PM / Engineer) - também publicada em web/public
        ("Lead_Tech_PM_Engineer_Maria_Hilmar_ATS", LEAD_TECH_PM_ENGINEER),
        ("PM_Tech_PM_Maria_Hilmar_ATS", PM_TECH_PM),
        ("QA_Requisitos_Maria_Hilmar_ATS", QA_REQUISITOS),
    ]
    generated = []
    site_pdf_source: Path | None = None
    site_docx_source: Path | None = None

    for out_dir in out_dirs:
        out_dir.mkdir(parents=True, exist_ok=True)
        for stem, content in variants:
            docx_path = out_dir / f"{stem}.docx"
            md_path = out_dir / f"{stem}.md"
            pdf_path = out_dir / f"{stem}.pdf"

            builder = AtsResumeBuilder()
            builder.build(content).save(docx_path)
            write_markdown(content, md_path)
            generated.extend([docx_path, md_path])

            if also_pdf:
                if export_pdf_with_word(docx_path, pdf_path):
                    generated.append(pdf_path)

            if stem.startswith("Lead_Tech_PM_Engineer") and out_dir == DEFAULT_OUT_DIR:
                site_docx_source = docx_path
                if pdf_path.exists():
                    site_pdf_source = pdf_path

    # Publica a versão Lead Tech PM no download do site
    SITE_PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    if site_docx_source and site_docx_source.exists():
        dest_docx = SITE_PUBLIC_DIR / f"{SITE_CV_STEM}.docx"
        dest_docx.write_bytes(site_docx_source.read_bytes())
        generated.append(dest_docx)
    if site_pdf_source and site_pdf_source.exists():
        dest_pdf = SITE_PUBLIC_DIR / f"{SITE_CV_STEM}.pdf"
        dest_pdf.write_bytes(site_pdf_source.read_bytes())
        generated.append(dest_pdf)
    elif site_docx_source:
        dest_pdf = SITE_PUBLIC_DIR / f"{SITE_CV_STEM}.pdf"
        if export_pdf_with_word(site_docx_source, dest_pdf):
            generated.append(dest_pdf)

    return generated


def main():
    out_dirs = [DEFAULT_OUT_DIR]
    if DESKTOP_OUT_DIR.parent.exists():
        out_dirs.append(DESKTOP_OUT_DIR)
    paths = generate_all(out_dirs, also_pdf=True)
    for path in paths:
        print(f"OK: {path}")
    print(f"\nTotal: {len(paths)} arquivo(s)")
    print(f"CV do site: {SITE_PUBLIC_DIR / (SITE_CV_STEM + '.pdf')}")


if __name__ == "__main__":
    main()
