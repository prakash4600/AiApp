import os
from openai import AzureOpenAI

# ⚠️ WARNING: Do NOT hardcode keys in production. Use env variables!
AZURE_OPENAI_KEY = os.environ.get("AteKCBWIp6MdJApCAc6kSVRYlayZYx14D9AutRLhNSZwopcejz2fJQQJ99CBACYeBjFXJ3w3AAABACOGWxe6")
AZURE_OPENAI_ENDPOINT = os.environ.get("https://myfirstaiapp.openai.azure.com/")

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version="2023-07-01-preview"
)

def ask_llm(question):
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # This should be your Azure deployment name
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