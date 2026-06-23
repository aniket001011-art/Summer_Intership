import numpy as np
arr = np.array([1,30,3,4,10,6])
arr[0], arr[-1] = arr[-1], arr[0]
print(arr)