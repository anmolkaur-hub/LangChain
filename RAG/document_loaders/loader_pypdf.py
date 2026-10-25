from langchain_community.document_loaders import PyPDFLoader
from typing import Literal

loader=PyPDFLoader(
   file_path= r"C:/Users/DELL/Downloads/Networking-Interview-Questions.pdf",
#    mode="page",
#    extraction_mode=Literal['plain', 'layout'] = 'plain'
 
)



documents = loader.load()

for i, document in enumerate(documents, start=1):
    if(i==4):
            break
    print("-_-_-_-_-_-_")
    print(f"Page {i}")
    print("________________________________" )

    print("Metadata:")
    print(document.metadata)

    print("Extracted text:")
    print(document.page_content)
