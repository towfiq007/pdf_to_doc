import fitz  # PyMuPDF
import pytesseract
from PIL import Image
from docx import Document
import io

def scanned_pdf_to_docx(pdf_path, docx_path):
    doc = Document()
    pdf = fitz.open(pdf_path)

    for page_num in range(len(pdf)):
        pix = pdf[page_num].get_pixmap(dpi=300)
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        text = pytesseract.image_to_string(img)
        doc.add_paragraph(text)
    
    doc.save(docx_path)
    print(f"OCR conversion complete: {pdf_path} → {docx_path}")

# Example usage
scanned_pdf_to_docx("scanned.pdf", "scanned_output.docx")
