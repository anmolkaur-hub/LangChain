from langchain_core.prompts import ChatPromptTemplate

template_generate=ChatPromptTemplate(
    [
        ("system","You are a smart email assistant that will generate emails based on the users provided information that will identify the title of the text provided "
        ".Just follow what's told.Give  a dictionary"),
        ("human",
         """Generate an Email-
        recipient:{recipient},
        user:{user}  ,
        tone:{tone}, 
        subject:{subject},
        
        """),
        
    ]
)




template_rewrite=ChatPromptTemplate(
[
    ("system","You are an email expert that will rewrite the emails in an "
    "improved way based on th information provided by user ."),
    ("human","""Rewrite this email:{email} in {tone}
        
    """)



]



)