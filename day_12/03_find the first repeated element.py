import numpy as np
arr = np.array([5,1,3,4,3,5,6])
arr_filter = []
for i in arr:
    for j in range(arr):
     if j is i:
          arr_filter.append(True)
     else:
          arr_filter.append(False)
print([arr_filter])  