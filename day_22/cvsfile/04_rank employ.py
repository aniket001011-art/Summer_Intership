import pandas as pd 
df = pd.read_csv("day_22/cvsfile/employees.csv")
d = df.groupby(["Department","EmployeeID"])["Salary"].sum().reset_index()

rak = d.groupby("Department")["Salary"].nlargest().reset_index()
print(rak)