# Function to get the window size F
def get_window_size():
    try:
        F = int(input("Enter the window size F: "))
        return F
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return None

# Function to get the threshold d
def get_threshold(F):
    max_d = 2 * F - 2

    while True:
        try:
            d = int(input(f"Enter the threshold d (between 0 and {max_d}): "))
            if 0 <= d <= max_d:
                return d
            else:
                print(f"Invalid input. Please enter a value between 0 and {max_d}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")