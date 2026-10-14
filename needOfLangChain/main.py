import os
from dotenv import load_dotenv
load_dotenv()

from mistralai.client import Mistral
from groq import Groq

api_key = os.getenv("MISTRALAi_API_KEY")
model = "mistral-small-latest"

client_mistral = Mistral(api_key=api_key)

mistral_response = client_mistral.chat.complete(
    model = model,
    messages = [
        {
            "role": "user",
            "content": "How far is the moon from earth?",
        },
    ]
)
print(mistral_response)





client_groq = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

groq_response = client_groq.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="openai/gpt-oss-20b",
    include_reasoning=False
)

print(groq_response.choices[0].message.content)



