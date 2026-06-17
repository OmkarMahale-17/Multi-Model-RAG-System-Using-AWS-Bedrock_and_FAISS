import os
from app.config import DATA_TEXT_PATH

def load_text_files():
    docs = []
    for file in os.listdir(DATA_TEXT_PATH):
        with open(os.path.join(DATA_TEXT_PATH, file), "r", encoding="utf-8") as f:
            docs.append(f.read())
    return docs