from pathlib import Path
from .utils import extract_text_from_pdf
from .memory import store_pdf_content, get_pdf_content




def answer_question_from_pdf(
    file_path: str,
    question: str
) -> dict:
    path = Path(file_path)
    content = extract_text_from_pdf(path)
    store_pdf_content(content, path.name)
    return {
        "status": "success",
        "report": f"Answer the following question based on this PDF:\n\n{content}\n\nQuestion: {question}"
    }



def summarize_pdf(
    file_path: str
) -> dict:
    path = Path(file_path)
    content = extract_text_from_pdf(path)
    store_pdf_content(content, path.name)
    return {
        "status": "success",
        "report": f"Summarize the following PDF content:\n\n{content}"
    }



def ask_about_uploaded_pdf(
    question: str
) -> dict:
    content = get_pdf_content()
    if not content:
        return {
            "status": "error",
            "report": "No PDF has been uploaded yet. Please upload a PDF file first."
        }
    return {
        "status": "success",
        "report": f"Answer this question based on previously uploaded PDF:\n\n{content}\n\nQuestion: {question}"
    }
