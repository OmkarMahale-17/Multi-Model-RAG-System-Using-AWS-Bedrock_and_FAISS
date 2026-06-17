from app.ingestion.loader import load_text_files
from app.ingestion.chunker import chunk_text
from app.embeddings.bedrock_embed import get_embedding
from app.vectorstore.faiss_store import build_faiss

docs = load_text_files()

chunks = []
for doc in docs:
    chunks.extend(chunk_text(doc))

embeddings = [get_embedding(c) for c in chunks]

build_faiss(embeddings, chunks)

print("FAISS index created!")