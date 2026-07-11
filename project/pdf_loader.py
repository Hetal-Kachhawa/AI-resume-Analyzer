"""
pdf_loader.py

Extracts text from an uploaded PDF resume.
"""

from pypdf import PdfReader


def extract_text_from_pdf(uploaded_file) -> str:
    """
    Reads a PDF file and returns all extracted text.

    Args:
        uploaded_file: Streamlit uploaded PDF file

    Returns:
        str: Extracted text
    """

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text.strip()