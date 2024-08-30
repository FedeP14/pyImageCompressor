import os
from inputoutput.file_io import load_image, save_image
from compression.dct_functions import compress_image
from compression.padding import add_padding, remove_padding
from cli.image_selection import select_image
from cli.user_input import get_window_size, get_threshold
import matplotlib.pyplot as plt


# Main function for the image compressor with CLI
def main():
    resource_folder = os.path.join(os.getcwd(), "resources")

    # Select the image to process
    selected_image, img_path = select_image(resource_folder)
    if not selected_image or not img_path:
        return

    # Load the selected image
    try:
        img = load_image(img_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        return

    # User chooses the window size F
    F = None
    while F is None:
        F = get_window_size()

    # Ask the user to input the threshold value d
    d = get_threshold(F)

    # Add padding if necessary
    padded_img, original_M, original_N = add_padding(img, F)

    # Perform image compression with padding
    compressed_img = compress_image(padded_img, F, d)

    # Remove padding to return to the original size
    compressed_img = remove_padding(compressed_img, original_M, original_N)

    # Save the compressed image in the folder
    compress_image_name = f"compressed_F{F}_d{d}_{selected_image}"
    compressed_image_path = os.path.join(os.getcwd(), "out", compress_image_name)

    # Save the compressed image
    save_image(compressed_img, compressed_image_path)

    # Load the compressed image for display
    compressed_img_loaded = load_image(compressed_image_path)

    # Get original image size in KB
    image_size = os.path.getsize(img_path) / 1024

    # Get compressed image size in KB
    compressed_image_size = os.path.getsize(compressed_image_path) / 1024

    # Display the original and compressed images side by side
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(img, cmap='gray')
    axes[0].set_title('Original Image', pad=20)
    axes[0].axis('off')
    axes[0].text(0.5, -0.6, 'Size = {:.2f} KB'.format(image_size))  

    axes[1].imshow(compressed_img_loaded, cmap='gray')
    axes[1].set_title('Compressed Image', pad=20)
    axes[1].axis('off')
    axes[1].text(0.5, -0.6, 'F = {}, d = {:.2f}, size = {:.2f} KB'.format(F, d, compressed_image_size))  

    plt.show()

if __name__ == "__main__":
    main()