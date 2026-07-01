import pandas as pd
data = {
    "Name":["Aniket","Rahul","Priya"],
    "Age":[21,250,20]
}

df = pd.DataFrame(data)
x = df.replace({"Age":250},value=22)
print(x)