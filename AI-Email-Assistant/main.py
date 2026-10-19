import os
import json
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

from templates import template_generate, template_rewrite


load_dotenv()


model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.2,
    api_key=os.getenv("GROQ_API_KEY")
)

parser = StrOutputParser()


generate_chain = template_generate | model | parser
rewrite_chain = template_rewrite | model | parser


#Generate email
def generate_email():
    response = generate_chain.invoke({
        "recipient": "Customer support",
        "user": "Anmol Kaur",
        "tone": "Formal",
        "subject": "Technical support request"
    })

    # Remove Markdown code fences if the model adds them
    response = response.strip()
    response = response.removeprefix("```json").strip()
    response = response.removesuffix("```").strip()

    email_data = json.loads(response)

    print("\nGenerated Email")
    print("--------------------")
    print("Recipient:", email_data["recipient"])
    print("Subject:", email_data["subject"])
    print("Body:", email_data["body"])


# Rewrite an existing email
def rewrite_email():
    with open("email.txt", "r", encoding="utf-8") as file:
        email = file.read()

    response = rewrite_chain.invoke({
        "email": email,
        "tone": "Funny"
    })

    print("\nRewritten Email")
    print("--------------------")
    print(response)


if __name__ == "__main__":
    generate_email()
    rewrite_email()
