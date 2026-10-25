import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters import CharacterTextSplitter


path="C:/Users/DELL/Downloads/Hotel_Booking_Analytics_Report.docx"

loader=Docx2txtLoader(
  file_path=path,

)
documents=loader.load()
