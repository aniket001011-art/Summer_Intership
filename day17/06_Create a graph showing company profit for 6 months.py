import matplotlib.pyplot as plt
import numpy as np 
arr = np.array(["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","num","dec"])
arr_1 = np.random.randint(100,1000,12)
plt.plot(arr,arr_1,'og--')
plt.xlabel("Months")
plt.ylabel("profit")
plt.show()