
import os
import requests
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
  
}

data = {
    "model": "openai/gpt-oss-20b",
    "messages": [
        {"role": "user", "content": "How far is moon from the earth?"}
    ]
}

try:
    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    print(result)

    if response.status_code == 200:
        print("GROQ RESPONSE:")
        print(result["choices"][0]["message"]["content"])
    else:
        print("API ERROR:", result)

except Exception as e:
    print("ERROR:", e)
