import os
import sys
import numpy as np
from dct_compression import load_image, save_image, compress_image

# Funzione per ottenere la lista dei file nella cartella "resource"
def list_files(directory):
    try:
        return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

# Funzione per aggiungere padding all'immagine
def add_padding(image, block_size):
    M, N = image.shape
    padded_M = M + (block_size - M % block_size) if M % block_size != 0 else M
    padded_N = N + (block_size - N % block_size) if N % block_size != 0 else N

    padded_image = np.zeros((padded_M, padded_N), dtype=image.dtype)
    padded_image[:M, :N] = image  # Copia l'immagine originale nel nuovo array con padding

    return padded_image, M, N  # Restituisce anche le dimensioni originali

# Funzione per rimuovere il padding
def remove_padding(image, original_M, original_N):
    return image[:original_M, :original_N]  # Rimuovi il padding ritagliando l'immagine

# Funzione principale per il compressore di immagini con CLI
def main():
    resource_folder = os.path.join(os.getcwd(), "part2\\resources")

    # Ottieni la lista dei file nella cartella "resources"
    file_list = list_files(resource_folder)
    
    # Verifica che ci siano file nella cartella
    if not file_list:
        print("No images found in the 'resources' folder.")
        return

    # Stampa la lista dei file disponibili
    print("Available images:")
    for i, file in enumerate(file_list):
        print(f"{i+1}. {file}")

    # L'utente seleziona l'immagine da caricare
    try:
        selected_image_index = int(input("Select an image to process: "))
        if selected_image_index < 1 or selected_image_index > len(file_list):
            print("Invalid selection.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    selected_image = file_list[selected_image_index - 1]
    img_path = os.path.join(resource_folder, selected_image)

    # Carica l'immagine selezionata
    try:
        img = load_image(img_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        return

    # L'utente sceglie l'ampiezza delle finestre F
    try:
        F = int(input("Enter the window size F: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    max_d = 2 * F - 2

    # Chiedi all'utente di inserire il valore di d
    while True:
        try:
            d = int(input(f"Enter the threshold d (between 0 and {max_d}): "))
            if 0 <= d <= max_d:
                break
            else:
                print(f"Invalid input. Please enter a value between 0 and {max_d}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Aggiungi padding se necessario
    padded_img, original_M, original_N = add_padding(img, F)

    # Esegui la compressione dell'immagine con padding
    compressed_img = compress_image(padded_img, F, d)

    # Rimuovi il padding per ritornare alla dimensione originale
    compressed_img = remove_padding(compressed_img, original_M, original_N)

    # Salva l'immagine compressa nella cartella 
    compress_image_name = f"compressed_{selected_image}"
    compressed_image_path = os.path.join(os.getcwd(), "parte2\\out", compress_image_name)
    
    save_image(compressed_img, compressed_image_path)

    print(f"Compressed image saved at: {compressed_image_path}")

if __name__ == "__main__":
    main()
