import boto3
import json
from app.config import AWS_REGION, LLM_MODEL

client = boto3.client(
    "bedrock-runtime",
    region_name=AWS_REGION
)

def generate_answer(context, query):

    prompt = f"""
You are a helpful AI assistant similar to ChatGPT.

Instructions:
1. Use the provided context if it is relevant to the user's question.
2. If the context is not relevant, answer using your general knowledge.
3. Be clear, concise, and helpful.
4. If the context is empty, answer normally.

Context:
{context}

User Question:
{query}
"""

    response = client.invoke_model(
        modelId=LLM_MODEL,
        body=json.dumps({
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ]
        }),
        contentType="application/json",
        accept="application/json"
    )

    result = json.loads(
        response["body"].read()
    )

    return result["output"]["message"]["content"][0]["text"]