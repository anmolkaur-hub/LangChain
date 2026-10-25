import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters import CharacterTextSplitter


# path_txt="C:/Users/DELL/Downloads/Digital India.docx"
path_txt="C:/Users/DELL/Downloads/sample_pdf.docx"

loader=Docx2txtLoader(
  file_path=path_txt,
)
documents=loader.load()

try:
    splitter = CharacterTextSplitter(
        separator="\n\n",
        chunk_size=100,
        chunk_overlap=5,
        length_function=len
    )
   
    chunked_text = splitter.split_text(documents[0].page_content)
  

    for idx,chunk in enumerate(chunked_text,start=1):
        print(f"CHUNK {idx}")
        print(chunk)
        print()


except Exception as e:
    print(f"ERROR: {e}")

















path = "C:/Users/DELL/Downloads/Digital India.pdf"