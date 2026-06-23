import numpy as np
arr = np.arange(-9,10)
print(arr)
filter = []
count = 0
for i in arr:
    if i<0:
        filter.append(True)
        count+=1
    else:
        filter.append(False)
print(arr[filter])
print(count)
