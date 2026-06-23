# Challenge 2: Search and Replace (Data Cleaning)
# Goal: Fix specific values in a dataset without loops.
# Tasks:Copy this array containing a mistake (-999 represents missing data)
## import numpy as np
## dataset = np.array([10, 20, -999, 40, -999, 50])
# Use code with caution.
# Write a single line of code to find all occurrences of -999 and change them to 0.Print the updated dataset

import numpy as np
dataset = np.array([10, 20, -999, 40, -999, 50])
arr = np.where(dataset==-999,'0',dataset)
print(arr)