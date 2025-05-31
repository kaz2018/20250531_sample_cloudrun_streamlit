import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Greeting App",
    page_icon="👋",
    layout="centered"
)

# Main greeting display
st.title("👋 Hello!")

# Additional friendly message
st.write("Welcome to our simple greeting application!")

# Optional: Add some visual separation
st.divider()

# Simple message with emphasis
st.markdown("### Have a wonderful day! 🌟")
