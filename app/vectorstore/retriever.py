import faiss
import pickle
import numpy as np
from app.config import FAISS_PATH

def load_index():
    index = faiss.read_index(FAISS_PATH + "index.faiss")
    with open(FAISS_PATH + "metadata.pkl", "rb") as f:
        docs = pickle.load(f)
    return index, docs

def search(query_embedding, index, docs, k=3):
    D, I = index.search(np.array([query_embedding]).astype("float32"), k)
    return [docs[i] for i in I[0]]