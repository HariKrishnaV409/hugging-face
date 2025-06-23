import streamlit as st
import requests
import io
from PIL import Image
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("HUGGINGFACE_API_KEY")

API_URL = "https://api-inference.huggingface.co/models/alvdansen/littletinies"
headers = {"Authorization": f"Bearer {API_KEY}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

st.title("AI Image Generator")
st.write("Enter a description to generate an image:")

# Get user input
description = st.text_input("Description")

if st.button("Generate Image"):
    if description:
        with st.spinner('Generating image...'):
            image_bytes = query({"inputs": description})
if uploaded_file is not None:
    image_bytes = uploaded_file.read()
    print(len(image_bytes))  # Debug to see if file is empty
# Validate that it's an image
    import imghdr
    if imghdr.what(None, image_bytes) is None:
        st.error("That file is not a valid image!")
    else:
        image = Image.open(io.BytesIO(image_bytes))
        st.image(image)
           # image = Image.open(io.BytesIO(image_bytes))
            image = image.open(https://huggingface.co/spaces/YUFI-API/BytesIOtoBase64)
            st.image(image, caption=description)
    else:
        st.warning("Please enter a description.")

# Add a footer
st.markdown("---")
st.markdown("Made by Hari")
