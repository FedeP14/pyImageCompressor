import numpy as np
from scipy.fftpack import dct, idct

# Function to perform 2D DCT on blocks
def block_dct2(block):
    return dct(dct(block.T, norm='ortho').T, norm='ortho')

# Function to perform 2D inverse DCT on blocks
def block_idct2(block):
    return idct(idct(block.T, norm='ortho').T, norm='ortho')

# Main function for image compression using DCT
def compress_image(image, block_size, d):
    M, N = image.shape

    # Ensure the image dimensions are divisible by the block size
    if M % block_size != 0 or N % block_size != 0:
        raise ValueError(f"The image must have dimensions that are multiples of {block_size}. Current dimensions: {M}x{N}")

    compressed_image = np.zeros_like(image)

    # Divide the image into blocks
    for i in range(0, M, block_size):
        for j in range(0, N, block_size):
            block = image[i:i+block_size, j:j+block_size]
            
            # Apply 2D DCT
            dct_block = block_dct2(block)

            # Zero out frequencies where k + l >= d
            for k in range(block_size):
                for l in range(block_size):
                    if k + l >= d:
                        dct_block[k, l] = 0

            # Apply inverse 2D DCT
            idct_block = block_idct2(dct_block)

            # Round the values and clip to the valid range [0, 255]
            idct_block = np.round(idct_block).clip(0, 255)

            # Recompose the image
            compressed_image[i:i+block_size, j:j+block_size] = idct_block

    return compressed_image.astype(np.uint8)