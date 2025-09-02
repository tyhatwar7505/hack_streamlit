import streamlit as st

st.title("🚀 Streamlit on Azure Web App")
st.write("This is a demo Streamlit app deployed to Azure.")

name = st.text_input("Enter your name:")
if name:
    st.success(f"Hello {name}, welcome to Azure + Streamlit!")
