from langchain_docling.loader import DoclingLoader

FILE_PATH = r"C:\Users\DELL\OneDrive\Desktop\Document\Basic JavaScript Concepts and Functions Q&A.pdf"

loader = DoclingLoader(file_path=FILE_PATH)

documents = loader.load()

print(f"Number of documents loaded: {len(documents)}")

for document in documents:
    print(document.page_content)
  