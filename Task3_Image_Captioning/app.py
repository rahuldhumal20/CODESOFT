import streamlit as st
from transformers import pipeline
from PIL import Image

st.title("🖼 AI Image Caption Generator")

@st.cache_resource
def load_model():
    return pipeline(
        "image-to-text",
        model="Salesforce/blip-image-captioning-base"
    )

captioner = load_model()

uploaded = st.file_uploader("Upload Image", type=["jpg","png","jpeg"])

if uploaded:
    image = Image.open(uploaded).convert("RGB")
    st.image(image, caption="Uploaded Image")

    result = captioner(image)
    st.subheader("Generated Caption:")
    st.write(result[0]["generated_text"])