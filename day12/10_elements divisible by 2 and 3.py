import numpy as np
arr = np.arange(1,21)
arr_1 = []
print(arr)
for i in arr:
    if i%2==0 and i%3==0:
        arr_1.append(i)
    else:
        pass
print(arr[arr_1])
