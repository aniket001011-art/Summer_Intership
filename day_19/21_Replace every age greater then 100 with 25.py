import pandas as pd
data = {
    "Name":["Aniket","Rahul","Priya"],
    "Age":[21,250,20]
}

df = pd.DataFrame(data)
for x in df.index:
    if df.loc[x,"Age"]>100:
        df.loc[x,"Age"]=25
print(df)
