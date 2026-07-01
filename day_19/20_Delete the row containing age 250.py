import pandas as pd
data = {
    "Name":["Aniket","Rahul","Priya"],
    "Age":[21,250,20]
}

df = pd.DataFrame(data)
for x in df.index:
  if df.loc[x, "Age"] == 250:
    df.drop(x, inplace = True)
print(df)

# another way
df = df[df["Age"] != 250]
print(df)