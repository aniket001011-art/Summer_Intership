import matplotlib.pyplot as plt
import numpy as np
arr = np.random.randint(1,100,1000)
print(arr)
plt.hist(arr, bins=20)
plt.show()