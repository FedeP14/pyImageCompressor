import numpy as np

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
