import matplotlib.pyplot as plt
x = [10,20,30,40]
y = [100,200,150,300]
plt.subplot(1,2,1)
plt.bar(x,y)
plt.title("Bar Chart")
plt.subplot(1,2,2)
plt.pie(y, labels=x)
plt.title("pie Chart")
plt.show()