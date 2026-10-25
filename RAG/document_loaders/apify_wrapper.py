import os
from dotenv import load_dotenv

from langchain_apify import ApifyWrapper
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
apify_token = os.getenv("APIFY_TOKEN")
openai_api_key = os.getenv("OPENAI_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY missing in .env")

if not apify_token:
    raise ValueError("APIFY_TOKEN missing in .env")


apify = ApifyWrapper(apify_token=apify_token)

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.2,
    api_key=groq_api_key
)
print("Calling website content crawler...")

loader = apify.call_actor(
    actor_id="apify/website-content-crawler",
    run_input={
        "startUrls": [
            {
                "url": "https://docs.langchain.com/oss/python/langchain/quickstart"
            }
        ],
        "maxCrawlPages": 10,
        "crawlerType": "cheerio"
    },
    dataset_mapping_function=lambda item: Document(
        page_content=item.get("text") or "",
        metadata={"source": item.get("url", "")}
    )
)

documents = loader.load()

documents = [
    doc for doc in documents
    if doc.page_content.strip()
]

if not documents:
    raise ValueError(
        "No content extracted. Check the Apify run and dataset."
    )

print(f"Extracted {len(documents)} documents")

print("Computing embeddings...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True}
)
vector_store = InMemoryVectorStore.from_documents(
    documents,
    embeddings
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)

prompt = ChatPromptTemplate.from_template(
    "Answer the question using only the context below. "
    "If the answer is not present, say you could not find it "
    "in the crawled documents.\n\n"
    "Context:\n{context}\n\n"
    "Question: {question}"
)

query = "What is LangChain?"

docs = retriever.invoke(query)

context = "\n\n".join(
    doc.page_content for doc in docs
)

if not context.strip():
    raise ValueError("No relevant context retrieved.")

answer = (
    prompt | llm
).invoke({
    "context": context,
    "question": query
}).content

sources = sorted({
    doc.metadata["source"]
    for doc in docs
    if doc.metadata.get("source")
})

print("\nAnswer:")
print(answer)

print("\nSources:")
for source in sources:
    print(source)
