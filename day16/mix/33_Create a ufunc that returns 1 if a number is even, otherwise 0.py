import numpy as np 
arr = np.array([1,2,3,4,5])
def myarr(num):
        if num % 2 == 0:
            return 1
        else:
            return 0 
my_even =np.frompyfunc(myarr,1,1)
print(my_even(arr))

