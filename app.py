import streamlit as st
import logging
from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
import os

# Configure logging for debugging
logging.basicConfig(
    level=logging.DEBUG,  # Change to logging.INFO to reduce verbosity
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
logger.debug("Environment variables loaded successfully.")

# Configuration for Azure OpenAI in python test
API_KEY = os.getenv("EPAM_DIAL_KEY", "dial-m12nz8lbct9y8rgvholhpr2dhwb")  # Default in case env variable fails
logger.debug(f"Using API Key: {API_KEY}")
AZURE_MODEL = "gpt-4o-mini-2024-07-18"
AZURE_ENDPOINT = "https://ai-proxy.lab.epam.com"
logger.debug(f"Using Azure Endpoint: {AZURE_ENDPOINT}, Model: {AZURE_MODEL}")

# Check for missing configuration
if not API_KEY:
    error_message = "Missing API_KEY! Ensure 'EPAM_DIAL_KEY' is set as an environment variable."
    logger.error(error_message)
    st.error(error_message)
    st.stop()  # Stop execution if critical setup is missing

# Initialize AzureChatOpenAI
try:
    epam_dial = AzureChatOpenAI(
        api_key=API_KEY,
        api_version="2024-08-01-preview",
        azure_endpoint=AZURE_ENDPOINT,
        model=AZURE_MODEL,
        temperature=0.0,
    )
    logger.info("Successfully initialized AzureChatOpenAI client.")
except Exception as e:
    error_message = f"Failed to initialize AzureChatOpenAI: {str(e)}"
    logger.error(error_message)
    st.error(error_message)
    st.stop()

# Streamlit app title
st.title("Azure OpenAI + Streamlit Debug App")
logger.debug("Streamlit app title set.")

# Prompting user to enter input
user_input = st.text_input("Enter your question:", placeholder="What is the capital of India?")
logger.debug(f"User Input: {user_input}")

if st.button("Get Answer"):
    logger.info("Get Answer button pressed.")
    if user_input.strip():
        try:
            # Log user input
            logger.info(f"Invoking Azure OpenAI with user input: {user_input}")

            # Pass user input to AzureChatOpenAI
            response = epam_dial.invoke(user_input)  # Call Azure OpenAI API
            
            # Validate the response object
            logger.info(f"Raw response object: {response}")
            print(f"[DEBUG] Raw response object: {response}")

            # Display the parsed response content
            st.success(f"Answer: {response.content}")
        except Exception as e:
            error_message = f"An error occurred during API invocation: {str(e)}"
            logger.error(error_message)
            print(f"[ERROR] {error_message}")
            st.error(error_message)
    else:
        warning_message = "No valid input provided. Please enter a question."
        logger.warning(warning_message)
        print(f"[WARNING] {warning_message}")
        st.warning(warning_message)