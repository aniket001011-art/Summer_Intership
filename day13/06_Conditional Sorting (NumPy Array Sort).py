# Challenge 3: Conditional Sorting (NumPy Array Sort)
# Goal: Sort an unsorted array in place or returning a copy.
# Tasks:Copy this unsorted array
# import numpy as np
# unordered = np.array([8, 3, 1, 7, 4])
# Use np.sort() to arrange the numbers in ascending order.
# Print the sorted array.

import numpy as np
arr = np.array([8, 3, 1, 7, 4])
ordered = np.sort(arr)
print(ordered)
 
# without in built function
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print(arr)