# pdf_agent/memory.py

pdf_memory = {
    "content": None,
    "file_name": None,
}


def store_pdf_content(content: str, file_name: str):
    pdf_memory["content"] = content
    pdf_memory["file_name"] = file_name


def get_pdf_content():
    return pdf_memory["content"]


def get_file_name():
    return pdf_memory["file_name"]
