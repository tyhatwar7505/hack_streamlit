import streamlit as st
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configuration for Azure OpenAI
API_KEY = "dial-m12nz8lbct9y8rgvholhpr2dhwb"
AZURE_MODEL = "gpt-4o-mini-2024-07-18"
AZURE_ENDPOINT = "https://ai-proxy.lab.epam.com"

# Initialize AzureChatOpenAI
epam_dial = AzureChatOpenAI(
    api_key=API_KEY,
    api_version="2024-08-01-preview",
    azure_endpoint=AZURE_ENDPOINT,
    model=AZURE_MODEL,
    temperature=0.0,
)

# Streamlit app
st.title("Azure OpenAI + Streamlit App")

# Prompting user to enter input
user_input = st.text_input("Enter your question:", placeholder="What is the capital of India?")

# Button to invoke AzureChatOpenAI
if st.button("Get Answer"):
    if user_input.strip():
        try:
            # Pass user input to AzureChatOpenAI
            response = epam_dial.invoke(user_input)
            # Display the AI response
            st.success("Answer: " + response.content)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a question to get an answer.")