import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader



# Token-Based
path= r"C:/Users/DELL/Downloads/Networking-Interview-Questions.pdf"

loader = PyMuPDFLoader(
    file_path=path,
    mode="page", 
)
try:
  
    splitter = CharacterTextSplitter.from_tiktoken_encoder(
    encoding_name="cl100k_base", chunk_size=100, chunk_overlap=20,
    separator="\n"
)

    documents=loader.load()
    document_string=""

    for doc in documents:
        document_string+=doc.page_content
    chunked_text = splitter.split_text(document_string)
    i=0
    for chunk in chunked_text:
            if(i==4):
                break
            print(f"CHUNK {i}")
            print(chunk)
            i=i+1


except Exception as e:
    print(f"ERROR : {e}")
 





