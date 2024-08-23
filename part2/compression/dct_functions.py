import numpy as np
from scipy.fftpack import dct, idct

# Funzione per eseguire la DCT2 sui blocchi
def block_dct2(block):
    return dct(dct(block.T, norm='ortho').T, norm='ortho')

# Funzione per eseguire la IDCT2 sui blocchi
def block_idct2(block):
    return idct(idct(block.T, norm='ortho').T, norm='ortho')

# Funzione principale di compressione con DCT
def compress_image(image, block_size, d):
    M, N = image.shape

    # Assicurati che le dimensioni dell'immagine siano divisibili per il blocco
    if M % block_size != 0 or N % block_size != 0:
        raise ValueError(f"L'immagine deve avere dimensioni multiple di {block_size}. Dimensioni attuali: {M}x{N}")

    compressed_image = np.zeros_like(image)

    # Suddividere l'immagine in blocchi
    for i in range(0, M, block_size):
        for j in range(0, N, block_size):
            block = image[i:i+block_size, j:j+block_size]
            
            # Applica la DCT2
            dct_block = block_dct2(block)

            # Elimina le frequenze con k + l >= d
            for k in range(block_size):
                for l in range(block_size):
                    if k + l >= d:
                        dct_block[k, l] = 0

            # Applica la IDCT inversa
            idct_block = block_idct2(dct_block)

            # Arrotonda i valori
            idct_block = np.round(idct_block).clip(0, 255)

            # Ricompone l'immagine
            compressed_image[i:i+block_size, j:j+block_size] = idct_block

    return compressed_image.astype(np.uint8)
