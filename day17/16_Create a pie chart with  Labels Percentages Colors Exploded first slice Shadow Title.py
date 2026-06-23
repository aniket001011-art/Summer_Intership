import matplotlib.pyplot as plt
monthly={
    'python':int(input("Enter the marks of Python..")),
    'java':int(input("Enter the marks of Java..")),
    'c++':int(input("Enter the marks of C++.."))
}
print(monthly)
sizes = list(monthly.values())
labls = list(monthly.keys())
color=["r",'b','y']
explode=[0.1,0,0]
plt.pie(sizes, labels=labls,
         colors=color,
         startangle=90,
         explode=explode,
         shadow=True)
plt.title("this is my pie chart")
plt.show()