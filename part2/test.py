import numpy as np
from compression.dct_functions import block_dct2, block_idct2, dct

def test_dct2d():
    # Example matrix
    matrix = np.array([
        [231, 32, 233, 161, 24, 71, 140, 245],
        [247, 40, 248, 245, 124, 204, 36, 107],
        [234, 202, 245, 167, 9, 217, 239, 173],
        [193, 190, 100, 167, 43, 180, 8, 70],
        [11, 24, 210, 177, 81, 243, 8, 112],
        [97, 195, 203, 47, 125, 114, 165, 181],
        [193, 70, 174, 167, 41, 30, 127, 245],
        [87, 149, 57, 192, 65, 129, 178, 228]
    ])

    # Compute 2D DCT
    dct_result = block_dct2(matrix)
    
    # Print the results of the 2D DCT
    print("DCT2D Result:")
    print(dct_result)

def test_idct2d():
    # Example matrix
    matrix = np.array([
        [231, 32, 233, 161, 24, 71, 140, 245],
        [247, 40, 248, 245, 124, 204, 36, 107],
        [234, 202, 245, 167, 9, 217, 239, 173],
        [193, 190, 100, 167, 43, 180, 8, 70],
        [11, 24, 210, 177, 81, 243, 8, 112],
        [97, 195, 203, 47, 125, 114, 165, 181],
        [193, 70, 174, 167, 41, 30, 127, 245],
        [87, 149, 57, 192, 65, 129, 178, 228]
    ])

    # Compute 2D DCT and then inverse DCT
    dct_result = block_dct2(matrix)
    idct_result = block_idct2(dct_result)

    # Print the results of the 2D IDCT
    print("IDCT2D Result:")
    print(idct_result)

def test_dct1d():
    # Example matrix
    matrix = np.array([
        [231, 32, 233, 161, 24, 71, 140, 245],
        [247, 40, 248, 245, 124, 204, 36, 107],
        [234, 202, 245, 167, 9, 217, 239, 173],
        [193, 190, 100, 167, 43, 180, 8, 70],
        [11, 24, 210, 177, 81, 243, 8, 112],
        [97, 195, 203, 47, 125, 114, 165, 181],
        [193, 70, 174, 167, 41, 30, 127, 245],
        [87, 149, 57, 192, 65, 129, 178, 228]
    ])

    # Compute 1D DCT on the first row
    dct1d = dct(matrix[0], norm='ortho')

    # Print the results of the 1D DCT in scientific notation
    print("DCT1D Result (in scientific notation):")
    formatted_dct1d = ["{:.2e}".format(val) for val in dct1d]
    print(" ".join(formatted_dct1d))

# Main block to execute the tests
if __name__ == "__main__":
    print("Select the test to run:")
    print("1. DCT2D Test")
    print("2. IDCT2D Test")
    print("3. DCT1D Test")
    print("4. Run All Tests")
    test_choice = input("Enter the test number: ")

    if test_choice == "1":
        test_dct2d()
    elif test_choice == "2":
        test_idct2d()
    elif test_choice == "3":
        test_dct1d()
    elif test_choice == "4":
        print("Running DCT2D Test")
        test_dct2d()
        print("\nRunning IDCT2D Test")
        test_idct2d()
        print("\nRunning DCT1D Test")
        test_dct1d()