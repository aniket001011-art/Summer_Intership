import numpy as np 
arr = np.diag([1,2,4,5])
print("\nThe diagonal array is..",arr)
arr2 = np.sum(arr)
print("\nThe sum of the diagonal array is...",arr2)

arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print("\nhere is the arry...",arr)
arr2 = np.diag(arr)
print("\nhere is the diagonals of the arrey.....",arr2)
arr3 = np.sum(arr2)
print("\nhere is the sum of the arrey diagonals",arr3)