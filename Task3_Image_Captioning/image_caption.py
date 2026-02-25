from transformers import pipeline
from PIL import Image

print("Loading AI model... (first run may take 2-3 minutes)")

# Load BLIP caption model
captioner = pipeline(
    "image-to-text",
    model="Salesforce/blip-image-captioning-base"
)

def generate_caption(image_path):
    image = Image.open(image_path).convert("RGB")
    result = captioner(image)
    return result[0]["generated_text"]

# Test image
image_path = "test.jpg"

caption = generate_caption(image_path)

print("\nGenerated Caption:")
print(caption)