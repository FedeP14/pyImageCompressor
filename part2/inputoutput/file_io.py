import os
import sys

# Funzione per ottenere la lista dei file nella cartella "resources"
def list_files(directory):
    try:
        return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
