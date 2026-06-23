import matplotlib.pyplot as plt
x = [10,20,30,40]
y = [100,200,150,300]
plt.plot(x,y,'g--', marker='o',markersize=12,linewidth=4)
plt.title("hello",size=20,color='r')
plt.grid(axis='x',color='r',linestyle='--')
plt.grid(axis='y',color='blue',linewidth=2,linestyle='--')
plt.show()
