import matplotlib.pyplot as plt
students = ["A","B","C","D","E"]
marks = [78,85,90,66,88]
attendance = [90,85,95,80,92]
plt.subplot(2,2,1)
plt.title("Line chart for Marks")
plt.plot(students,marks,'or--')
plt.xlabel("student")
plt.ylabel("Marks")
plt.grid()


plt.subplot(2,2,2)
plt.title("Bar chart for Attendance.")
plt.bar(students,attendance,color='g')
plt.xlabel("student")
plt.ylabel("Attendance")


plt.subplot(2,2,3)
plt.title("Scatter plot for Marks.")
plt.scatter(students,marks,color='m')
plt.xlabel("student")
plt.ylabel("Marks")
plt.grid()

plt.subplot(2,2,4)
plt.title("Pie chart showing Marks Percentage")
plt.pie(marks,labels=students)

plt.tight_layout()
plt.show()
