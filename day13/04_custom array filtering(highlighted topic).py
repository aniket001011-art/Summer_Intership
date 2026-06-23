# Challenge 4: Custom Array Filtering (Highlighted Topic)
# Goal: Create a filtered array using a custom boolean mask list.
# Tasks:Copy this array:
# python
# import numpy as np
# arr = np.array([10, 20, 30, 40])
# Create a boolean list mask = [True, False, True, False].
# Filter arr using this mask and print the result. (Expected output: [10, 30]).


import numpy as np
arr = np.array([10, 20, 30, 40])
mask = [True,False,True,False]
filter_arr = arr[mask]
print(filter_arr) 