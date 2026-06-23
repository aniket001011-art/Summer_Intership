import numpy as np
A=np.array([2,4,6,8])
B=np.array([6,8,10,12])
print(np.union1d(A,B))
print(np.intersect1d(A,B))
print(np.setdiff1d(A,B))
print(np.setxor1d(A,B))