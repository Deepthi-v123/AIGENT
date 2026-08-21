import pymupdf as fitz

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

if __name__ == "__main__":
    extracted_text = extract_text("sample.pdf")
    print(extracted_text[:1000])  # first 1000 characters print madutte, check madoke