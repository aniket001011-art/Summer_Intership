import matplotlib.pyplot as plt
monthly={
    'html':int(input("Enter the marks of Python..")),
    'java':int(input("Enter the marks of Java..")),
    'c++':int(input("Enter the marks of C++.."))
}
print(monthly)
sizes = list(monthly.values())
labls = list(monthly.keys())
plt.pie(sizes, labels=labls, startangle=90)
plt.show()