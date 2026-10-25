from langchain_community.document_loaders import WebBaseLoader
from typing import List

def single_page_loader(url:str):
    loader = WebBaseLoader(
    web_path=(url),
    default_parser="html.parser",
    show_progress=True,
    raise_for_status=True,
)   
    documents = loader.load()
    return documents




def load_multiple_pages(urls:List[str]):
    loader = WebBaseLoader(
        web_path=tuple(urls),
        default_parser="html.parser",
        show_progress=True,
        raise_for_status=True,
    )   
    documents = loader.load()
    return documents






def main():
    
        print("SINGLE PAGE LOADER_-_-_-_-_-")
        single_page_data=single_page_loader("https://www.wikihow.com/Save-Trees")

        for i, doc in enumerate(single_page_data, start=1):
        
               print(f"DOCUMENT- {i}")
               print("________________________________" )
            
               print("Metadata:")
               print(doc.metadata)
               
               print("Extracted text:")
               print(doc.page_content)
       
        # print("____________MULTIPLE_PAGES_LOADER_________________") 
        # multiple_pages_content=load_multiple_pages(["https://www.investopedia.com/terms/s/swot.asp",
        #                    "https://friendsoftheearth.uk/sustainable-living/13-best-ways-save-water",
        #                    "https://www.britannica.com/science/pollution-environment"])
        # for i, doc in enumerate(multiple_pages_content, start=1):
                      
        #                print(f"DOCUMENT- {i}")
        #                print("________________________________" )
                    
        #                print("Metadata:")
        #                print(doc.metadata)
                       
        #                print("Extracted text:")
        #                print(doc.page_content)

main()























