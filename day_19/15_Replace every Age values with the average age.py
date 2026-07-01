import pandas as pd

data = {
    "Name":["Aniket","Rahul","Priya","Aman"],
    "Age":[21,None,20,None],
    "Marks":[95,88,None,80]
}

df = pd.DataFrame(data)
x=df["Age"].mean()
print(df.fillna({"Age":x},inplace=True))

#another way to do this without using built in function.
c = df["Age"].sum()//3
print(c)
print(df.fillna(c))