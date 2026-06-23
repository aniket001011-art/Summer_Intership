import numpy as np
numbers = np.array([11, 22, 33, 44, 55, 66, 77, 88])
filter_arr = []
for i in numbers:
    if i % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
print(numbers[filter_arr])
# new_arr = numbers[filter_arr]
# print(new_arr)