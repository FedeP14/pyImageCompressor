import os
import sys
import numpy as np
from PIL import Image

# Function to get the list of files in the "resources" folder
def list_files(directory):
    try:
        return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

# Function to load an image in grayscale
def load_image(filepath):
    img = Image.open(filepath).convert('L')
    return np.array(img)

# Function to save the compressed image
def save_image(image, filepath):
    img = Image.fromarray(image)
    img.save(filepath)