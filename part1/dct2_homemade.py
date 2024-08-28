import numpy as np
import math

# Calculate the transformation matrix once for dimension N
def create_transformation_matrix(n):
    # Create the alpha vector of length n
    alpha = np.ones(n) * np.sqrt(2 / n)
    alpha[0] = 1 / np.sqrt(n)

    # Create the transformation matrix
    transformation_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            transformation_matrix[i, j] = alpha[i] * np.cos((i * math.pi * (2 * j + 1)) / (2 * n))
    return transformation_matrix

# Function to perform DCT using the created transformation matrix
def dct_created(input_vector, transformation_matrix):
    # Multiply the transformation matrix by the input vector
    return np.dot(transformation_matrix, input_vector)

# Function to perform 2D DCT
def dct2_created(input_matrix):
    n, m = input_matrix.shape

    # Create the transformation matrix once for rows and columns
    transformation_matrix_n = create_transformation_matrix(n)
    transformation_matrix_m = create_transformation_matrix(m)

    # DCT for each column
    dct2_result = np.copy(input_matrix.astype('float64'))
    for j in range(m):
        dct2_result[:, j] = dct_created(dct2_result[:, j], transformation_matrix_n)

    # DCT for each row
    for i in range(n):
        dct2_result[i, :] = dct_created(dct2_result[i, :], transformation_matrix_m)

    return dct2_result
