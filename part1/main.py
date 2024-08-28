import numpy as np
import matplotlib.pyplot as plt
from part1.compare_dct2 import compare_dct_times

# Define a list of different sizes for the Discrete Cosine Transform (DCT) to be tested
N_values = [500, 750, 1000, 2500, 5000, 7500, 10000, 12500, 15000]

# Call the function to compare execution times of homemade DCT and scipy's DCT for the given sizes
times_homemade, times_scipy = compare_dct_times(N_values)

# Print the results for each size
for i in range(len(N_values)):
    print(f"N = {N_values[i]}")
    print(f"Manual DCT time: {times_homemade[i]:.5f} s")
    print(f"Scipy DCT time: {times_scipy[i]:.5f} s")

# Create a new figure for plotting the results
plt.figure()

# Plot the execution times on a semilogarithmic scale for better visualization
plt.semilogy(N_values, times_homemade, label='Home made DCT')
plt.semilogy(N_values, times_scipy, label='Scipy DCT')

# Label the axes
plt.xlabel('Size N')
plt.ylabel('Time (s)')

# Add a title to the plot
plt.title('Comparison of DCT2 Execution Times')

# Add a legend to distinguish between manual and scipy DCT times
plt.legend()

# Add a grid to the plot for better readability, with both major and minor lines
plt.grid(True, which="both", ls="--")

# Print a message indicating that the plot is being saved
print("Saving the plot in out folder...")

# Save the plot as a PNG file in the 'out' directory
plt.savefig('out/dct_times.png')

# Display the plot
plt.show()
