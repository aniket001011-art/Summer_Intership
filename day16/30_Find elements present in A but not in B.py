import numpy as np
arr = np.array([1,2,3,4])
arr_1 = np.array([3,4,5])
a = np.setdiff1d(arr,arr_1)
print(a)