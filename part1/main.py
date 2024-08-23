import numpy as np
import matplotlib.pyplot as plt
from dct2_manual import compare_dct_times

# Parametri per la prova
N_values = [500, 750, 1000, 2500, 5000, 7500, 10000, 12500, 15000]

# Confronta i tempi di DCT manuale vs scipy
times_manual, times_scipy = compare_dct_times(N_values)

# Plot dei risultati su scala semilogaritmica
plt.figure()
plt.semilogy(N_values, times_manual, label='DCT manuale (N^3)')
plt.semilogy(N_values, times_scipy, label='DCT scipy (N^2 log N)')
plt.xlabel('Dimensione N')
plt.ylabel('Tempo (s)')
plt.title('Confronto Tempi di Esecuzione DCT2')
plt.legend()
plt.savefig('out\\dct_times.png')
