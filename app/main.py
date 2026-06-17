from fastapi import FastAPI, UploadFile, File
from app.pipeline.rag_pipeline import run_rag
import os

app = FastAPI()

@app.post("/query")
async def query(q: str, file: UploadFile = File(None)):

    file_path = None

    if file is not None:

        print("=" * 50)
        print("Filename:", file.filename)
        print("Content Type:", file.content_type)

        ext = os.path.splitext(file.filename)[1].lower()
        print("Extension:", ext)
        print("=" * 50)

        if ext == ".pdf":
            os.makedirs("data/pdfs", exist_ok=True)
            file_path = os.path.join("data/pdfs", file.filename)

        elif ext in [".png", ".jpg", ".jpeg", ".webp"]:
            os.makedirs("data/images", exist_ok=True)
            file_path = os.path.join("data/images", file.filename)

        else:
            return {"response": f"Unsupported file type: {ext}"}

        with open(file_path, "wb") as f:
            f.write(await file.read())

        print("Saved file:", file_path)

    result = run_rag(q, file_path)

    return {"response": result}