import pandas as pd
data = {
    "Name":["Aniket","Rahul","Rahul","Priya","Priya"],
    "Age":[21,22,22,20,20]
}

df = pd.DataFrame(data)
print(df.duplicated())