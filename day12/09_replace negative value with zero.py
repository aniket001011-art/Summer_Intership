import numpy as np
arr = np.array([12,12,4,-4,23,-45])
s = np.where(arr<0,0,arr)
print(s)

for i in range(len(arr)):
    if arr[i] <0:
        arr[i] = 0
    else:
        pass
print(arr)

