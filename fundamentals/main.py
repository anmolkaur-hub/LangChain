import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
load_dotenv()
def generatePrompt():
    template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful agent that summarizes text. Your task is to summarize the text provided."),
            ("human", "Summarize this {text}?"),
        ]
    )
    return template

text = """
The Moon is Earth's only natural satellite, orbiting our planet at an average distance of about 384,400 kilometers (238,900 miles). Formed roughly 4.5 billion years ago from debris following a massive collision, it does not produce its own light; instead, it shines in the night sky by reflecting sunlight. Because the Moon is tidally locked—meaning its rotation and orbital period both take about 27.3 days—the exact same side always faces Earth. Its gravitational pull drives ocean tides and helps stabilize Earth's axial tilt, making our companion a vital force for conditions on our home planet."""

prompt = generatePrompt()

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.2,
   
    api_key=os.getenv("GROQ_API_KEY"),
)
parser = StrOutputParser()

chain = prompt | llm | parser

try:
    response = chain.invoke({"text": text})
    print(response)

except Exception as e:
    print(f"Exception : {e}")