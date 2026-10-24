
# import re


# def analyze_resume(resume_text, job_description):

#     resume_text = resume_text.lower()
#     job_description = job_description.lower()

#     # Extract words from the job description
#     words = set(
#         re.findall(
#             r"\b[a-zA-Z][a-zA-Z+#.]*\b",
#             job_description
#         )
#     )

#     # Ignore common words
#     common_words = {
#         "the", "and", "for", "with", "you",
#         "your", "are", "our", "this", "that",
#         "will", "have", "has", "from", "job",
#         "work", "role", "who", "what", "their",
#         "they", "can", "all", "but", "not",
#         "any", "into", "about", "using", "is",
#         "a", "an", "to", "of", "in", "on", "at"
#     }

#     keywords = words - common_words

#     # Match complete words
#     matched = {
#         word for word in keywords
#         if re.search(
#             r"(?<!\w)" + re.escape(word) + r"(?!\w)",
#             resume_text
#         )
#     }

#     missing = keywords - matched

#     # Calculate the keyword match percentage
#     if keywords:
#         score = round(len(matched) / len(keywords) * 100)
#     else:
#         score = 0

#     return {
#         "ats_score": score,
#         "matched_skills": sorted(matched),
#         "missing_skills": sorted(missing)
#     }


import os
from io import BytesIO

import streamlit as st
from pypdf import PdfReader
from docx import Document


def extract_resume_text(uploaded_file):
    """Extract text from PDF, DOCX or TXT resumes."""

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):
        reader = PdfReader(BytesIO(uploaded_file.getvalue()))

        text = "\n".join(
            page.extract_text() or ""
            for page in reader.pages
        )

    elif file_name.endswith(".docx"):
        document = Document(BytesIO(uploaded_file.getvalue()))

        text = "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )

    elif file_name.endswith(".txt"):
        text = uploaded_file.getvalue().decode(
            "utf-8",
            errors="replace"
        )

    else:
        raise ValueError(
            "Please upload a PDF, DOCX or TXT file."
        )

    if not text.strip():
        raise ValueError(
            "No readable text was found in this resume."
        )

    return text


def analyze_resume(resume_text, job_description=""):
    """Analyze resume using the Gemini API."""

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is missing. "
            "Configure your Gemini API key first."
        )

    from google import genai

    client = genai.Client(api_key=api_key)

    prompt = f"""
You are a professional resume reviewer.

Analyze the following resume.

Job description:
{job_description or "No job description provided."}

Resume:
{resume_text[:25000]}

Provide a clear report containing:

1. Overall resume quality score out of 100.
2. Resume strengths.
3. Areas that need improvement.
4. Important skills identified.
5. Education and experience feedback.
6. Formatting and readability suggestions.
7. Missing or recommended keywords based on the
   supplied job description, if available.
8. Five practical recommendations for improvement.

Explain that the score is an estimate, not an official
ATS score or a guarantee of getting hired.

Use clear headings and bullet points.
Do not invent qualifications or experience.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    if not response.text:
        raise ValueError(
            "The AI did not return an analysis. Please try again."
        )

    return response.text
