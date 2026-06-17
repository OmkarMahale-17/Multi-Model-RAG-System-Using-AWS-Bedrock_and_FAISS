FROM python:3.10

WORKDIR /app
COPY . .

RUN pip install fastapi uvicorn boto3 faiss-cpu numpy streamlit requests

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]