import matplotlib.pyplot as plt
expenses={
    "Food" :300,
    "Rent" : 500,
    "Travel" : 150,
    "Shopping" : 250
}
size = list(expenses.values())
labal = list(expenses.keys())
plt.pie(size,labels=labal)
plt.show()