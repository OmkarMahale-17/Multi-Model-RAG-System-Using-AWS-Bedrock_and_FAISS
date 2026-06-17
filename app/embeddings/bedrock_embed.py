import boto3
import json
from app.config import AWS_REGION, EMBED_MODEL

client = boto3.client("bedrock-runtime", region_name=AWS_REGION)

def get_embedding(text):
    response = client.invoke_model(
        modelId=EMBED_MODEL,
        body=json.dumps({"inputText": text})
    )
    result = json.loads(response["body"].read())
    return result["embedding"]