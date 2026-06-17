import streamlit as st
import requests

st.title("Multimodal RAG System")

query = st.text_input("Ask something")

file = st.file_uploader(
    "Upload File",
    type=["pdf", "png", "jpg", "jpeg", "webp"]
)

if st.button("Submit"):

    files = None

    if file:
        files = {
            "file": (
                file.name,          # filename
                file.getvalue(),    # file content
                file.type           # MIME type
            )
        }

    res = requests.post(
        "http://localhost:8000/query",
        params={"q": query},
        files=files
    )

    st.write(res.json())