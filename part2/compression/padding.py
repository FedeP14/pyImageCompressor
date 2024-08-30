import numpy as np

# Function to add padding to the image
def add_padding(image, block_size):
    M, N = image.shape
    # Calculate the new dimensions with padding
    padded_M = M + (block_size - M % block_size) if M % block_size != 0 else M
    padded_N = N + (block_size - N % block_size) if N % block_size != 0 else N

    # Create a new array with the padded dimensions
    padded_image = np.zeros((padded_M, padded_N), dtype=image.dtype)
    # Copy the original image into the new array with padding
    padded_image[:M, :N] = image

    # Return the padded image along with the original dimensions
    return padded_image, M, N

# Function to remove the padding from the image
def remove_padding(image, original_M, original_N):
    # Remove the padding by cropping the image to the original dimensions
    return image[:original_M, :original_N]