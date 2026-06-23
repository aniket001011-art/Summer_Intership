import numpy as np 
arr = np.array([1,2,3,4,5,6,7,8])
def my_arr(num):
    if num % 2 == 0:
        return num * num
    else:
        return 0 

my_even = np.frompyfunc(my_arr,1,1)
print(my_even(arr))