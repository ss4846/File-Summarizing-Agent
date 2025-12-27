import pdfplumber
from docx import Document

def read_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                # Replace bad characters
                page_text = page_text.encode("utf-8", errors="replace").decode("utf-8")
                text += page_text + "\n"
    return text

def read_docx(path):
    doc = Document(path)
    return "\n".join([para.text for para in doc.paragraphs])

def read_file(path):
    if path.endswith(".pdf"):
        return read_pdf(path)
    elif path.endswith(".docx"):
        return read_docx(path)
    else:
        # TXT file
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
