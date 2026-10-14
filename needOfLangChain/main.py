print("Program started")
import os
from dotenv import load_dotenv
load_dotenv()
from groq import Groq
# from google import genai
from ollama import chat


# Gemini
# client_gemini = genai.Client()
# try:
#    gemini_response = client_gemini.interactions.create(
#     model="gemini-4-argon",
#     input="How far is moon from the earth?"
# )
#    print("GEMINI RESPONSE-----------------")
#    print(gemini_response.output_text)
# except Exception as e:
#    print(f"ERROR : {e}")



# Groq
client_groq = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

try:
   groq_response = client_groq.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "How far is moon from the earth?",
        }
    ],
    model="openai/gpt-oss-20b",
    include_reasoning=False
)
   print("GROQ RESPONSE-----------------")
   print(groq_response.choices[0].message.content)

except Exception as e:
   print(f"ERROR : {e}")



# Ollama
try:
    response = chat(
        model="qwen2.5:0.5b",
        messages=[
            {
                "role": "user",
                "content": "How far is the moon from the earth?"
            }
        ]
    )
    result = response.message.content
    print("OLLAMA RESPONSE______")
    print(result)
except Exception as e:
   print(f"ERROR : {e}")


# from mistralai.client import Mistral
# api_key_mistral= os.getenv("MISTRALAi_API_KEY")
# model = "mistral-small-latest"
# client_mistral = Mistral(api_key=api_key_mistral)
# mistral_response = client_mistral.chat.complete(
#     model = model,
#     messages = [
#         {
#             "role": "user",
#             "content": "How far is the moon from earth?",
#         },
#     ]
# )
# print(mistral_response)


