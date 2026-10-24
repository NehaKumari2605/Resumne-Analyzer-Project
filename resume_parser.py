
from pypdf import PdfReader


def extract_resume_text(uploaded_file):
    pdf = PdfReader(uploaded_file)

    resume_text = ""

    for page in pdf.pages:
        resume_text += page.extract_text() or ""

    return resume_text
