# 🖼️ AI Image Captioning System

## 📌 Project Overview

This project implements an **AI-based Image Captioning system** that automatically generates meaningful textual descriptions for images using **Computer Vision** and **Natural Language Processing (NLP)**.

The application uses a pretrained deep learning model to understand visual features from an image and convert them into human-readable captions.

---

## 🎯 Objective

To build an AI agent that:

* Extracts visual features from an image
* Understands image content
* Generates a descriptive caption automatically

This project fulfills **Task 3 – Image Captioning** of the CodSoft Artificial Intelligence Internship.

---

## 🧠 Technologies Used

* Python 3.x
* Hugging Face Transformers
* PyTorch
* Pillow (Image Processing)
* Streamlit (Web Interface)

---

## ⚙️ Model Used

**BLIP (Bootstrapping Language-Image Pretraining)**
Model: `Salesforce/blip-image-captioning-base`

The model combines:

* Vision Transformer (Image Understanding)
* Language Model (Text Generation)


---

###  Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run Project

### Run Python Script

```
python image_caption.py
```

### Run Web Application

```
streamlit run app.py
```

Open browser:

```
http://localhost:8501
```

---

## 🖼️ How It Works

1. User uploads an image.
2. The pretrained vision model extracts image features.
3. The language model generates a caption.
4. Caption is displayed to the user.


---

## 📚 Concepts Covered

* Computer Vision
* Natural Language Processing
* Transformer Models
* Deep Learning Inference
* Image-to-Text Generation



