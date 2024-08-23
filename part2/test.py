import numpy as np
from part2.compression.dct_functions import block_dct2, block_idct2, dct

def test_dct2d():
    # Matrice di esempio
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

    # Calcola DCT
    dct_result = block_dct2(matrix)
    
    # Stampa i risultati della DCT2D
    print("DCT2D Result:")
    print(dct_result)

def test_idct2d():
    # Matrice di esempio
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

    # Calcola DCT e IDCT
    dct_result = block_dct2(matrix)
    idct_result = block_idct2(dct_result)

    # Stampa i risultati della IDCT2D
    print("IDCT2D Result:")
    print(idct_result)

def test_dct1d():
    # Matrice di esempio
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

    # Calcola DCT monodimensionale sulla prima riga
    dct1d = dct(matrix[0], norm='ortho')

    # Stampa i risultati della DCT1D in notazione scientifica
    print("DCT1D Result (in notazione scientifica):")
    formatted_dct1d = ["{:.2e}".format(val) for val in dct1d]
    print(" ".join(formatted_dct1d))

# Blocco principale per eseguire i test
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
        print("Esecuzione test DCT2D")
        test_dct2d()
        print("\nEsecuzione test IDCT2D")
        test_idct2d()
        print("\nEsecuzione test DCT1D")
        test_dct1d()


