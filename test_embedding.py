import boto3
import json

client = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1"
)

response = client.invoke_model(
    modelId="amazon.titan-embed-text-v2:0",
    body=json.dumps({
        "inputText": "Hello World"
    })
)

print(response["body"].read())