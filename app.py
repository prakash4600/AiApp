import os
from openai import AzureOpenAI

endpoint = "https://bhanu-ml92txcy-eastus2.cognitiveservices.azure.com/"
model_name = "gpt-4o-mini"
deployment = "gpt-4o-mini"

subscription_key = "6WlG5cOGtxMFAW6dkUUCskYgDi3JWFQUh9nGRM7EBiaJxl1pBxHTJQQJ99CBACHYHv6XJ3w3AAAAACOGmPFf"
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
<<<<<<< HEAD
            "content": "I am going to Paris, what should I see?",
=======
            "content": "Explain Kubernetes ConfigMaps in simple words?",
>>>>>>> f18b1ee (Initial Azure OpenAI app code)
        }
    ],
    max_tokens=4096,
    temperature=1.0,
    top_p=1.0,
    model=deployment
)

print(response.choices[0].message.content)