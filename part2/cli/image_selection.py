import os
from inputoutput.file_io import list_files

# Function to select the image to process
def select_image(resource_folder):
    # Get the list of files in the "resources" folder
    file_list = list_files(resource_folder)
    
    # Check if there are any files in the folder
    if not file_list:
        print("No images found in the 'resources' folder.")
        return None, None

    # Print the list of available files
    print("Available images:")
    for i, file in enumerate(file_list):
        print(f"{i + 1}. {file}")

    # User selects the image to load
    try:
        selected_image_index = int(input("Select an image to process: "))
        if selected_image_index < 1 or selected_image_index > len(file_list):
            print("Invalid selection.")
            return None, None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None, None

    selected_image = file_list[selected_image_index - 1]
    img_path = os.path.join(resource_folder, selected_image)
    
    return selected_image, img_path