import os
import json
from dotenv import load_dotenv
load_dotenv()
from langchain_apify import ApifyScrapeUrlTool

api_key=os.getenv("APIFY_TOKEN")

tool = ApifyScrapeUrlTool()
text=json.loads(tool.invoke({"url": "https://www.britannica.com/science/pollution-environment"}))
# print(type(text))
# print(text['content'])
print(text)



