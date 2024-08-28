import numpy as np
from scipy.fft import dct
import time
from dct2_homemade import dct2_created  # Import the custom DCT2 function

def compare_dct_times(N_values):
    """
    Compare execution times of custom DCT2 and scipy's DCT2 for different matrix sizes.
    
    Parameters:
    N_values (list): List of matrix dimensions to test.
    
    Returns:
    tuple: Two lists containing execution times for custom DCT2 and scipy's DCT2 respectively.
    """
    
    times_manual = []
    times_scipy = []

    # Loop over each provided dimension N
    for N in N_values:
        # Create an NxN matrix with random values
        input_matrix = np.random.rand(N, N)
        
        # Measure execution time for the custom DCT2
        start_time = time.time()
        dct2_manual_result = dct2_created(input_matrix)
        end_time = time.time()
        times_manual.append(end_time - start_time)
        
        # Measure execution time for scipy's DCT2
        start_time = time.time()
        dct2_scipy_result = dct(dct(input_matrix, axis=0, norm='ortho'), axis=1, norm='ortho')
        end_time = time.time()
        times_scipy.append(end_time - start_time)
        
    return times_manual, times_scipy
