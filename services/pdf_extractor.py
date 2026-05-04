import fitz

def extract_text_from_pdf(content: bytes):
    try:
        pdf = fitz.open(stream=content, filetype="pdf")
        text = ""

        for page in pdf:
            text += page.get_text()

        if not text.strip():
            raise ValueError("No text found in PDF")

        return text

    except Exception:
        raise ValueError("Error extracting text from PDF")