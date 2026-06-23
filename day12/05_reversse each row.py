import numpy as np
arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print("\nhere is the arrey before reverse each roll's...",arr)
arr_2 = arr.flatten()
arr_2 = arr_2[::-1]
print(arr_2)
arr = arr_2.reshape(3,3)
arr = arr[::-1]
print("\nhere is the arrey after reverse each roll's...",arr)