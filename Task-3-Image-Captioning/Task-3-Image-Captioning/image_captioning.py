# Image Captioning 

import tensorflow as tf
import numpy as np
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense
from PIL import Image

# Load pre-trained ResNet50 model
base_model = ResNet50(weights='imagenet')
model = Model(inputs=base_model.input,
              outputs=base_model.layers[-2].output)

# Simple vocabulary (demo purpose)
vocab = {
    0: "a",
    1: "man",
    2: "woman",
    3: "dog",
    4: "cat",
    5: "standing",
    6: "on",
    7: "road",
    8: "with",
    9: "ball"
}

# Load and preprocess image
def preprocess_image(img_path):
    img = load_img(img_path, target_size=(224, 224))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img

# Extract image features
def extract_features(img_path):
    img = preprocess_image(img_path)
    features = model.predict(img)
    return features

# Generate caption (simple logic)
def generate_caption(features):
    caption = ["a", "man", "standing", "on", "road"]
    return " ".join(caption)

# ---- Run ----
image_path = "test.jpg"   # apni image ka path yaha do

features = extract_features(image_path)
caption = generate_caption(features)

print("Generated Caption:")
print(caption)
