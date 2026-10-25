import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

path= r"C:/Users/DELL/Downloads/Networking-Interview-Questions.pdf"

loader = PyMuPDFLoader(
    file_path=path,
    mode="page", 
)
try:
    splitter =  RecursiveCharacterTextSplitter(
    chunk_size=200, 
    chunk_overlap=50)

    documents=loader.load()
    document_string=""

    for doc in documents:
        document_string+=doc.page_content
    chunked_text = splitter.split_text(document_string)


    print(type(chunked_text))
    print(len(chunked_text))
    # print(chunked_text[0:5])
    i=0
    for chunk in chunked_text:
        if(i==10):
            break
        print(f"CHUNK {i}")
        print(chunk)
        i=i+1

except Exception as e:
    print(f"ERROR : {e}")
 










# for i, document in enumerate(documents, start=1):
#     print(type(document))
#     if(i==4):
#         break
#     print("-_-_-_-_-_-_")
#     print(f"Page {i}")
#     print("________________________________" )

#     print("Metadata:")
#     print(document.metadata)

#     print("Extracted text:")
#     print(document.page_content)
