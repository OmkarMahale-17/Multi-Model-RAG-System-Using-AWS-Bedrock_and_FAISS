import faiss
import numpy as np
import pickle
import os
from app.config import FAISS_PATH

def build_faiss(embeddings, docs):
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)

    index.add(np.array(embeddings).astype("float32"))

    os.makedirs(FAISS_PATH, exist_ok=True)
    faiss.write_index(index, FAISS_PATH + "index.faiss")

    with open(FAISS_PATH + "metadata.pkl", "wb") as f:
        pickle.dump(docs, f)