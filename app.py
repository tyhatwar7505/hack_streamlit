import streamlit as st

# App Title
st.title("📊 Streamlit Calculator on Azure")
st.write("Welcome to the Simple Calculator App — deployed on Azure!")

# Sidebar for input values
st.sidebar.header("Inputs")

# Input fields for first number and second number
num1 = st.sidebar.number_input("Enter the first number:", step=0.1)  # Allow decimal input
num2 = st.sidebar.number_input("Enter the second number:", step=0.1)

# Dropdown for operation selection
operation = st.sidebar.selectbox("Select an operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

# Perform calculation based on the selected operation
result = None
if st.sidebar.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.success(f"The result of {num1} + {num2} is {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"The result of {num1} - {num2} is {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"The result of {num1} × {num2} is {result}")
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.success(f"The result of {num1} ÷ {num2} is {result}")
        else:
            st.error("Division by zero is not allowed!")

# Footer
st.write("Powered by [Streamlit](https://streamlit.io) and hosted on Azure Web App 🚀")