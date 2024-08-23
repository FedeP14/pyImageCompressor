import numpy as np
from PIL import Image

# Funzione per caricare un'immagine in toni di grigio
def load_image(filepath):
    img = Image.open(filepath).convert('L')
    return np.array(img)

# Funzione per salvare l'immagine compressa
def save_image(image, filepath):
    img = Image.fromarray(image)
    img.save(filepath)
