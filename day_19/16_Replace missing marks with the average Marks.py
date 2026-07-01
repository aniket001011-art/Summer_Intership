import pandas as pd

data = {
    "Name":["Aniket","Rahul","Priya","Aman"],
    "Age":[21,None,20,None],
    "Marks":[95,88,None,80]
}

df = pd.DataFrame(data)
x=df["Marks"].mean()
print(df.fillna({"Marks":x},inplace=True))

#another way to do this without using built in function.
c = df["Marks"].sum()//3
print(c)
print(df.fillna(c))