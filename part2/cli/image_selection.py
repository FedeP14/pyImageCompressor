import os
from inputoutput.file_io import list_files

# Funzione per selezionare l'immagine da processare
def select_image(resource_folder):
    # Ottieni la lista dei file nella cartella "resources"
    file_list = list_files(resource_folder)
    
    # Verifica che ci siano file nella cartella
    if not file_list:
        print("No images found in the 'resources' folder.")
        return None, None

    # Stampa la lista dei file disponibili
    print("Available images:")
    for i, file in enumerate(file_list):
        print(f"{i+1}. {file}")

    # L'utente seleziona l'immagine da caricare
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
