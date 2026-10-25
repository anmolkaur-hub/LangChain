import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader

path_pdf = "C:/Users/DELL/Downloads/Digital India .pdf"

loader = PyMuPDFLoader(
    file_path=path_pdf,
    mode="page"
)
document=loader.load()
try:
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=500,
        chunk_overlap=50,
        length_function=len
    )


    chunked_text = splitter.split_text(document[0].page_content)

    i = 0
    for chunk in chunked_text:
        print(f"CHUNK {i}")
        print(chunk)
        print()
        i += 1

except Exception as e:
    print(f"ERROR: {e}")