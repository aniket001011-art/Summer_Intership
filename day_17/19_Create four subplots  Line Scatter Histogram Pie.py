import matplotlib.pyplot as plt
x = [10,20,30,40]
y = [100,200,150,300]
plt.subplot(2,2,1)
plt.plot(x,y,'ro--')
plt.title("line Chart")

plt.subplot(2,2,2)
plt.scatter(x,y,color='m')
plt.title("scatter Chart")

plt.subplot(2,2,3)
plt.hist(y, bins=4,color='y')
plt.title("histogram Chart")

plt.subplot(2,2,4)
plt.pie(y, labels=x)
plt.title("pie Chart")
plt.show()