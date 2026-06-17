from pypdf import PdfReader

from app.embeddings.bedrock_embed import get_embedding
from app.vectorstore.retriever import load_index, search
from app.llm.bedrock_llm import generate_answer
from app.embeddings.image_embed import image_to_text

index, docs = load_index()


def extract_pdf_text(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def run_rag(query, file_path=None):

    extra_context = ""

    if file_path:

        if file_path.lower().endswith(".pdf"):
            extra_context = extract_pdf_text(file_path)

        elif file_path.lower().endswith(
            (".png", ".jpg", ".jpeg", ".webp")
        ):
            extra_context = image_to_text(file_path)

    full_query = query + " " + extra_context

    query_embedding = get_embedding(full_query)

    retrieved = search(query_embedding, index, docs)

    context = " ".join(retrieved)

    context += "\n" + extra_context

    return generate_answer(context, query)