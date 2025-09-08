from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ.get("EPAM_DIAL_KEY")
AZURE_MODEL = "gpt-4o-mini-2024-07-18"

epam_dial = AzureChatOpenAI(
    api_key         = API_KEY,
    api_version     = "2024-08-01-preview",
    azure_endpoint  = "https://ai-proxy.lab.epam.com",
    model           = AZURE_MODEL,
    temperature     = 0.0
)

resp = epam_dial.invoke("What is the capital of India?")
print('resp: ', resp.content)