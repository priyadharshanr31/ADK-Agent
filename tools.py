from pathlib import Path
from .utils import extract_text_from_pdf

def answer_question_from_pdf(file_path: str, question: str) -> dict:
    content = extract_text_from_pdf(Path(file_path))
    prompt = (
        f"Answer the following question based on this PDF:\n\n{content}\n\nQuestion: {question}"
    )
    return {"status": "success", "report": prompt}


def summarize_pdf(file_path: str) -> dict:
    content = extract_text_from_pdf(Path(file_path))
    prompt = f"Summarize the following PDF content:\n\n{content}"
    return {"status": "success", "report": prompt}
