# 📄 Document Summarizer

Easily upload a PDF or image (JPEG/PNG) and get a summary using T5 or BART transformer models. Includes a simple web GUI!

---

## 🏗️ Project Architecture

- **Frontend:** Streamlit web app for file upload, model selection, and displaying summaries.
- **Backend:** FastAPI server for handling file uploads, OCR, and text summarization.
- **OCR Engine:** Tesseract (via pytesseract) for extracting text from images and PDFs.
- **Summarization Models:** HuggingFace Transformers (T5 and BART) for abstractive text summarization.
- **Storage:** Uploaded files and generated outputs are stored in dedicated folders for traceability.

---

## 🧑‍💻 Technology Stack

- **Python 3.8+**
- **FastAPI** for high-performance async API
- **Streamlit** for rapid, beautiful web UI
- **PyMuPDF (fitz)** for PDF parsing
- **Pillow** for image processing
- **pytesseract** for OCR
- **transformers** (HuggingFace) for state-of-the-art NLP models
- **torch** for deep learning backend

---

## 🤖 Model Details

- **T5 (Text-to-Text Transfer Transformer):**
  - Pre-trained on a large corpus for general-purpose text summarization.
  - Handles a wide range of document types and writing styles.
- **BART (Bidirectional and Auto-Regressive Transformers):**
  - Excels at abstractive summarization and paraphrasing.
  - Robust to noisy or unstructured input.

Both models are loaded at startup for fast inference and can be easily swapped or extended with other HuggingFace models.

---

## 🔌 Extensibility

- **Add More Models:** Plug in any HuggingFace summarization model with minimal code changes.
- **API-First:** Easily integrate with other apps or workflows via REST API.
- **Custom OCR:** Swap Tesseract for another OCR engine if needed.
- **Cloud Ready:** Can be containerized and deployed to cloud platforms (Dockerfile not included by default).

---

## 💡 Use Cases

- Summarize research papers, reports, or contracts
- Extract and condense text from scanned documents
- Quickly review meeting notes or handwritten memos
- Build into larger document management or knowledge systems

---

## 🛠️ Quick Start Guide

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/document-summarizer.git
cd document-summarizer
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Tesseract OCR (Required for Image/PDF Text Extraction)
- **Download for Windows:**
  - [UB Mannheim Tesseract Installer (recommended)](https://github.com/UB-Mannheim/tesseract/wiki)
  - Install to the default location (e.g., `C:\Users\YOURNAME\AppData\Local\Programs\Tesseract-OCR`)
- **No need to add Tesseract to PATH!**
- The code is set up to use the default install location. If you install Tesseract elsewhere, update this line in `app/ocr.py`:
  ```python
  pytesseract.pytesseract.tesseract_cmd = r"C:\\Users\\YOURNAME\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
  ```

### 4. Start the Backend (API)
```bash
uvicorn app.main:app --reload
```
- You should see: `Uvicorn running on http://127.0.0.1:8000`
- Test the API at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 5. Start the Web GUI (Frontend)
```bash
streamlit run app/gui.py
```
- Open [http://localhost:8501](http://localhost:8501) in your browser.
- Upload a PDF or image, select a model, and click Summarize!

---

## ✨ Features
- Upload PDF or image files (PNG, JPG, JPEG)
- Choose between T5 and BART summarization models
- Get a concise summary in seconds
- Clean, modern, and user-friendly interface
- Error handling and loading indicators for a smooth experience

---

## 🛠️ Troubleshooting
- **Tesseract not found?**
  - Make sure you installed Tesseract as above.
  - If you installed to a custom location, update the path in `app/ocr.py` as shown above.
- **Can't connect to backend?**
  - Make sure you started the backend (`uvicorn ...`) and see the correct message in the terminal.
  - The GUI and backend must both be running at the same time.
- **Other issues?**
  - Restart both the backend and GUI after making changes.
  - Check for typos in file paths.

---

Developed with ❤️ using FastAPI & Streamlit.

AI, NLP, DocumentSummarizer, SummarizeX, OCR, DeepLearning, FastAPI, Streamlit, HuggingFace, Python, OpenSource, Productivity, TextSummarization, PDFTools