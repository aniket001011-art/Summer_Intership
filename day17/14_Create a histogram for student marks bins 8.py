import matplotlib.pyplot as plt
import numpy as np
arr = np.array([20,25,23,43,56,85,76,65,23,33,88,65,24,12])
plt.hist(arr,bins=8,color='g',edgecolor='black')
plt.grid()
plt.show()