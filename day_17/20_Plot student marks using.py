import matplotlib.pyplot as plt

students = ["A","B","C","D","E"]
marks = [65,80,75,90,85]

plt.subplot(2,2,1)
plt.plot(students,marks,'ro--')
plt.title("line Chart")

plt.subplot(2,2,2)
plt.scatter(students,marks,color='m')
plt.title("scatter Chart")

plt.subplot(2,2,3)
plt.bar(students,marks)
plt.title("bar Chart")
plt.show()