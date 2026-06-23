import matplotlib.pyplot as plt
x = [10,20,30,40]
y = [100,200,150,300]
plt.subplot(2,1,1)
plt.plot(x,y, marker='o')
plt.subplot(2,1,2)
plt.hist(y, bins=3)
plt.show()