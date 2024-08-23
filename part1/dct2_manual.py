import numpy as np
import time
from scipy.fftpack import dct

# DCT 1D applicata per righe e poi per colonne (manuale)
def dct2_manual(image):
    M, N = image.shape
    # Applicare DCT per righe
    dct_rows = np.apply_along_axis(dct, 1, image, norm='ortho')
    # Applicare DCT per colonne
    dct_cols = np.apply_along_axis(dct, 0, dct_rows, norm='ortho')
    return dct_cols

# Funzione per calcolare i tempi di esecuzione della DCT manuale e della FFT
def compare_dct_times(N_values):
    times_manual = []
    times_scipy = []
    for N in N_values:
        image = np.random.rand(N, N)
        
        # DCT manuale
        start_time = time.time()
        dct2_manual(image)
        times_manual.append(time.time() - start_time)

        # DCT con scipy
        start_time = time.time()
        dct(image, norm='ortho')
        times_scipy.append(time.time() - start_time)
        
    return times_manual, times_scipy

