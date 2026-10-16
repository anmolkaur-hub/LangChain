import os
import json
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from templates import template_generate, template_rewrite
from langchain_core.output_parsers import StrOutputParser



api_key=os.getenv("GROQ_API_KEY")

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.2,
    api_key=api_key,
    reasoning_effort=None,
    
)

parser=StrOutputParser()


response1=template_generate|model|parser
response2=template_rewrite|model|parser


generated_email = response1.invoke({
"recipient":"Customer support",
"user":"Anmol Kaur",
"tone":"Formal",
"subject":"technical support request"
})


generated_email = generated_email.strip()

if generated_email.startswith("```json"):
    generated_email = generated_email[len("```json"):].strip()

if generated_email.endswith("```"):
    generated_email = generated_email[:-3].strip()


new_email = json.loads(generated_email)
print("Generated Email Contents___________")
print("***************************")

new_email=json.loads(generated_email)

print(new_email['recipient'])
print(new_email['subject'])
print(new_email['body'])




email=""
with open('email.txt', 'r') as file:
    email = file.read()

rewrite_email=response2.invoke({
    "email":email,
    "tone":"funny"
})


print("Rewritten Email___________")
print("***************************")
print(rewrite_email)










