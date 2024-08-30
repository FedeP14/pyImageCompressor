import os
from inputoutput.image_io import load_image, save_image
from compression.dct_functions import compress_image
from compression.padding import add_padding, remove_padding
from cli.image_selection import select_image
from cli.user_input import get_window_size, get_threshold
import matplotlib.pyplot as plt


# Funzione principale per il compressore di immagini con CLI
def main():
    resource_folder = os.path.join(os.getcwd(), "resources")

    # Seleziona l'immagine da processare
    selected_image, img_path = select_image(resource_folder)
    if not selected_image or not img_path:
        return

    # Carica l'immagine selezionata
    try:
        img = load_image(img_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        return

    # L'utente sceglie l'ampiezza delle finestre F
    F = None
    while F is None:
        F = get_window_size()

    # Chiedi all'utente di inserire il valore di d
    d = get_threshold(F)

    # Aggiungi padding se necessario
    padded_img, original_M, original_N = add_padding(img, F)

    # Esegui la compressione dell'immagine con padding
    compressed_img = compress_image(padded_img, F, d)

    # Rimuovi il padding per ritornare alla dimensione originale
    compressed_img = remove_padding(compressed_img, original_M, original_N)

    # Salva l'immagine compressa nella cartella 
    compress_image_name = f"compressed_F{F}_d{d}_{selected_image}"
    compressed_image_path = os.path.join(os.getcwd(), "out", compress_image_name)

    # Salva l'immagine compressa
    save_image(compressed_img, compressed_image_path)

    # Carica l'immagine compressa per la visualizzazione
    compressed_img_loaded = load_image(compressed_image_path)

    # Mostra l'immagine originale e quella compressa affiancate
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(img, cmap='gray')
    axes[0].set_title('Original Image')
    axes[0].axis('off')

    axes[1].imshow(compressed_img_loaded, cmap='gray')
    axes[1].set_title('Compressed Image, F = {}, d = {:.2f}'.format(F, d))
    axes[1].axis('off')

    plt.show()


if __name__ == "__main__":
    main()
