import numpy as np 
arr = np.array([1,2,3,4,5])
def myarr(num):
    return num ** 3
my_cude =np.frompyfunc(myarr,1,1)
print(my_cude(arr))

