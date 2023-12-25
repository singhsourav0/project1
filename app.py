import streamlit as st

st.title("Hello, Streamlit!")

st.write("This is a simple Streamlit app.")

# Add a text input widget
name = st.text_input("Enter your name:")

# Display a greeting based on the input
if name:
    st.write("Welcome, " + name + "!")
