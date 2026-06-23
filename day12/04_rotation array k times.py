import numpy as np
arr = np.array([1,2,4,5,6])
print("\nbefore rotation arrey is...",arr)
k = 2
part1 = arr[-k:]
part2 = arr[:-k]
print(part1)
print(part2)
fianl_arr = np.concatenate((part1,part2),axis=0)
print("\nHere is the final arrey after rotation it from k times....",fianl_arr)
