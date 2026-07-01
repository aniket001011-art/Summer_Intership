import pandas as pd

data = {
    "Name":["Aniket","Rahul","Priya","Aman"],
    "Age":[21,None,20,None],
    "Marks":[95,88,None,80]
}

df = pd.DataFrame(data)
print(df.fillna(0))