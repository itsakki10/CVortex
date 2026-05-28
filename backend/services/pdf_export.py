import io
import logging

from bs4 import BeautifulSoup

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.lib.pagesizes import (
    letter
)


logger = logging.getLogger(
    'ats_resume_scorer'
)


def clean_html(html:str)->str:

    soup = BeautifulSoup(
        html,
        "html.parser"
    )

    return soup.get_text(
        separator="\n"
    )


def generate_combined_pdf(
    html_docs: dict[str, str]
) -> bytes:

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter
    )

    styles = getSampleStyleSheet()

    story=[]


    title = Paragraph(
        "CVortex ATS Report",
        styles['Title']
    )

    story.append(title)

    story.append(
        Spacer(1,20)
    )


    for name,content in html_docs.items():

        heading = Paragraph(
            f"<b>{name}</b>",
            styles['Heading2']
        )

        story.append(heading)

        story.append(
            Spacer(1,10)
        )


        cleaned_text = clean_html(
            str(content)
        )


        paragraphs = cleaned_text.split(
            "\n"
        )


        for p in paragraphs:

            p=p.strip()

            if p:

                para = Paragraph(
                    p,
                    styles['BodyText']
                )

                story.append(para)

                story.append(
                    Spacer(1,8)
                )


        story.append(
            PageBreak()
        )


    doc.build(story)

    pdf_bytes = buffer.getvalue()

    buffer.close()

    return pdf_bytes