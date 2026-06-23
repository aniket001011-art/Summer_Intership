# Challenge 3: Row vs Column Sums (Axis Math)
# Goal: Calculate sums along specific directions of a matrix.
# Tasks:Copy this matrix:python
# import numpy as np
# matrix = np.array([[1, 2, 3], 
#                    [4, 5, 6]])
# Use code with caution.Use np.sum() with axis=0 to calculate and print the sum of each column.
# Use np.sum() with axis=1 to calculate and print the sum of each row.

import numpy as np
matrix = np.array([[1, 2, 3], 
                   [4, 5, 6]])
column_arr = np.sum(matrix,axis=0)
row_arr = np.sum(matrix,axis=1)
print(column_arr)
print(row_arr) 