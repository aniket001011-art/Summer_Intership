import numpy as np
arr = np.array([1,0,2,0,3,4,0])
print("\nbefore move zeros..",arr)
arr = np.sort(arr)
arr = arr[::-1]
print("\nmove all the zeros in the end..",arr)