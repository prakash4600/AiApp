import os
from openai import AzureOpenAI

# Read from environment variables
AZURE_OPENAI_KEY = os.environ.get("1BxVzsb78lleMXlGdNd6quSxnOZITtbS7zl2dG0rh8R60v8h5VMPJQQJ99CBACYeBjFXJ3w3AAABACOGZKSJ")
AZURE_OPENAI_ENDPOINT = os.environ.get("https://demo324123423.openai.azure.com/")

if not AZURE_OPENAI_KEY or not AZURE_OPENAI_ENDPOINT:
    raise ValueError("Missing required environment variables")

client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version="2023-07-01-preview"
)

def ask_llm(question):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful DevOps assistant."},
            {"role": "user", "content": question}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    question = "Explain Kubernetes ConfigMaps in simple words"
    print("Answer:\n", ask_llm(question))