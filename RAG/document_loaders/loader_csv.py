import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain_community.document_loaders import CSVLoader


def normal_load(path:str):
    
    loader=CSVLoader(
    file_path=path,
    source_column="Email",
)

    documents=loader.load()
    return documents

def load_lazy(path:str):
    loader=CSVLoader(
        file_path=path,
        source_column="Email",
    )
 
    documents=loader.lazy_load()
    return documents




def main():

    normal_load_response=normal_load("C:/Users/DELL/Downloads/customers-100.csv")
    
    for i,doc in enumerate(normal_load_response[0:5],start=1):
        print(f"RECORD {i} ____________")
        print("CONTENT________")
        print(doc.page_content)

        print("METADATA____________________")
        print(doc.metadata)



    lazy_load_response=load_lazy("C:/Users/DELL/Downloads/customers-100.csv")
    print(lazy_load_response)

    i=0
    for doc in lazy_load_response:
        if(i==4):
            break
        print(f"DOCUMENT {i}_______")
        print(doc)
        i=i+1
   



main()