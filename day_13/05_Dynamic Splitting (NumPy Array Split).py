# Challenge 5: Dynamic Splitting (NumPy Array Split)
# Goal: Divide a single array into multiple smaller sub-arrays.
# Tasks:Create a 1D array with numbers from 1 to 6 using np.arange().
# Use np.array_split() to divide this array into exactly 3 equal parts.
# Print the resulting list of arrays.

import numpy as np
arr = np.arange(1,7)
arr = np.array_split(arr,3)
print(arr)