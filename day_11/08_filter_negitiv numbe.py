import numpy as np
arr = np.array([15, -30, 45, 30, -60])
filter_arr = []
for i in arr:
    if i < 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
print(arr[filter_arr])
    