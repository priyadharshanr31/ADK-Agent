#utils.py

from pathlib import Path
import fitz  # PyMuPDF

def extract_text_from_pdf(file_path: Path) -> str:
    doc = fitz.open(str(file_path))
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip()
