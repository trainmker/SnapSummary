from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.ocr import extract_text_from_pdf, extract_text_from_image
from app.summarize import summarize_text
from pathlib import Path
import shutil

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = Path("uploads")
UPLOAD_FOLDER.mkdir(exist_ok=True)
OUTPUT_FOLDER = Path("outputs")
OUTPUT_FOLDER.mkdir(exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Document Summarizer API. Use /upload/ to POST a file for summarization."}

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), model: str = "t5"):
    file_path = UPLOAD_FOLDER / file.filename
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    ext = file.filename.lower().split('.')[-1]
    try:
        if ext == "pdf":
            text = extract_text_from_pdf(file_path)
        elif ext in ["png", "jpg", "jpeg"]:
            text = extract_text_from_image(file_path)
        else:
            return JSONResponse(status_code=400, content={"error": "Unsupported file type."})

        summary = summarize_text(text, model=model)
        return {"summary": summary}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})