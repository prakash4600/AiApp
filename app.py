from openai import OpenAI

# ⚠️ WARNING: Do NOT hardcode keys in production
AZURE_OPENAI_KEY = "AteKCBWIp6MdJApCAc6kSVRYlayZYx14D9AutRLhNSZwopcejz2fJQQJ99CBACYeBjFXJ3w3AAABACOGWxe6"
AZURE_OPENAI_ENDPOINT = "https://myfirstaiapp.openai.azure.com/"

client = OpenAI(
    api_key=AZURE_OPENAI_KEY,
    api_base=AZURE_OPENAI_ENDPOINT,
    api_type="azure",
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