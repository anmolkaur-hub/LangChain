from langchain_community.document_loaders import PyMuPDFLoader


path= r"C:/Users/DELL/Downloads/Networking-Interview-Questions.pdf"

loader = PyMuPDFLoader(
    file_path=path,
    mode="page", 
)

documents = loader.load()

for i, document in enumerate(documents, start=1):
    print(type(document))
    if(i==4):
        break
    print("-_-_-_-_-_-_")
    print(f"Page {i}")
    print("________________________________" )

    print("Metadata:")
    print(document.metadata)

    print("Extracted text:")
    print(document.page_content)
