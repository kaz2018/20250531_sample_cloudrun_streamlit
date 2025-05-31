import streamlit as st
import pandas as pd

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

# Text input section
st.subheader("Tell us about yourself")
name = st.text_input("What's your name?", placeholder="Enter your name here")
if name:
    st.write(f"Nice to meet you, {name}!")

# Text area for longer input
message = st.text_area("Share your thoughts:", placeholder="Tell us what's on your mind...")
if message:
    st.info(f"You shared: {message}")

# File upload section
st.subheader("Upload a file")
uploaded_file = st.file_uploader("Choose a file", type=['txt', 'csv', 'json', 'png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    file_details = {
        "Filename": uploaded_file.name,
        "File size": f"{uploaded_file.size} bytes",
        "File type": uploaded_file.type
    }
    st.write("File details:")
    st.json(file_details)
    
    # Display file content based on type
    if uploaded_file.type.startswith('text') or uploaded_file.type == 'text/csv':
        st.text("File preview:")
        content = str(uploaded_file.read(), "utf-8")
        st.text(content[:500] + "..." if len(content) > 500 else content)
    elif uploaded_file.type.startswith('image'):
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

# Selection widgets
st.subheader("Make some selections")

# Selectbox
favorite_color = st.selectbox("What's your favorite color?", 
                             ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"])
st.write(f"Your favorite color is {favorite_color}")

# Multi-select
hobbies = st.multiselect("What are your hobbies?", 
                        ["Reading", "Sports", "Music", "Travel", "Cooking", "Gaming", "Art"])
if hobbies:
    st.write(f"Your hobbies: {', '.join(hobbies)}")

# Slider
age = st.slider("How old are you?", 0, 100, 25)
st.write(f"You are {age} years old")

# Number input
lucky_number = st.number_input("Enter your lucky number", min_value=1, max_value=100, value=7)
st.write(f"Your lucky number is {lucky_number}")

# Date input
birthday = st.date_input("When is your birthday?")
st.write(f"Your birthday is {birthday}")

# Button interactions
st.subheader("Interactive buttons")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Say Hello", type="primary"):
        st.balloons()
        st.success("Hello there! 👋")

with col2:
    if st.button("Show Info"):
        st.info("This is an information message!")

with col3:
    if st.button("Random Fact"):
        facts = [
            "Honey never spoils!",
            "Octopuses have three hearts!",
            "Bananas are berries, but strawberries aren't!",
            "A group of flamingos is called a 'flamboyance'!",
            "The shortest war in history lasted only 38-45 minutes!"
        ]
        import random
        st.write(f"🎲 Fun fact: {random.choice(facts)}")

# Optional: Add some visual separation
st.divider()

# Simple message with emphasis
st.markdown("### Have a wonderful day! 🌟")
