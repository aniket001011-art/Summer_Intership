import matplotlib.pyplot as plt
days = ["mon","tue","wed","thu","fri","sat","sun"]
temp = [22,34,54,76,98,34,54]
plt.plot(days,temp,'or--')
plt.xlabel("Days")
plt.ylabel("temprature")
plt.title("7 Days temprature")
plt.show()