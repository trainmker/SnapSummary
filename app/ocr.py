import fitz  # PyMuPDF
from PIL import Image
import pytesseract

# Explicitly set the Tesseract executable path for Windows
pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\hamza.ali\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    return pytesseract.image_to_string(image)