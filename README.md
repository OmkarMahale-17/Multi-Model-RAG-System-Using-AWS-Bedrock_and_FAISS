Multi-Model-RAG-System-Using-AWS-Bedrock_and_FAISS
Overview

This project implements a Multimodal Retrieval-Augmented Generation (RAG) System that enables users to interact with and retrieve information from multiple data formats, including PDFs, images, and text documents. The system leverages AWS Bedrock for embeddings and Large Language Model (LLM) inference, while FAISS (Facebook AI Similarity Search) is used for efficient vector storage and semantic retrieval.

By combining retrieval and generation, the system provides context-aware and accurate responses based on user-provided knowledge sources, reducing hallucinations and improving answer reliability.

Features
Multimodal document processing
PDF documents
Images
Text files
Retrieval-Augmented Generation (RAG)
Semantic search using FAISS Vector Database
AWS Bedrock integration for:
Amazon Titan Embeddings
Foundation Models for response generation
FastAPI backend for API services
Real-time document querying
Context-aware question answering
Scalable and efficient vector search
Architecture
User uploads documents (PDF, Image, Text).
Content is extracted and preprocessed.
Embeddings are generated using AWS Bedrock.
Embeddings are stored in a FAISS vector database.
User submits a query.
Similar documents are retrieved from FAISS.
Retrieved context is sent to the LLM through AWS Bedrock.
Context-aware response is generated and returned.
Tech Stack
Programming Language
Python
Backend
FastAPI
AI & Machine Learning
AWS Bedrock
Amazon Titan Embeddings
Anthropic Claude
Vector Database
FAISS
Libraries
LangChain
NumPy
Pandas
Frontend
Streamlit
Project Structure
Multimodal_rag_system/
│
├── backend/
├── frontend/
├── data/
├── vector_store/
├── uploads/
├── app.py
├── requirements.txt
└── README.md
Installation
Clone the Repository
git clone https://github.com/OmkarMahale-17/Multi-Model-RAG-System-Using-AWS-Bedrock_and_FAISS.git
cd Multi-Model-RAG-System-Using-AWS-Bedrock_and_FAISS
Create Virtual Environment
python -m venv venv

Activate:

venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
AWS Configuration

Configure AWS credentials:

aws configure

Provide:

AWS Access Key
AWS Secret Key
Region (e.g., ap-south-1)

Ensure access to:

Amazon Bedrock
Amazon Titan Embeddings
Claude Models
Running the Application
Start FastAPI Backend
uvicorn app:app --reload

Backend URL:

http://127.0.0.1:8000
Start Streamlit Frontend
streamlit run app.py
Use Cases
Enterprise Knowledge Base Assistant
Document Question Answering
Research Assistant
Internal Company Documentation Search
Educational Content Retrieval
Future Enhancements
Support for audio and video files
Hybrid Search (Keyword + Semantic Search)
User Authentication
Cloud Deployment
Multi-user document management
Author

Omkar Mahale

Full Stack Developer
GenAI Engineer
AI Enthusiast

GitHub: https://github.com/OmkarMahale-17
