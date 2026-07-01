import pandas as pd
df1 = pd.read_csv("day_22/cvsfile/duplicate_data.csv")
df2 = pd.read_csv("day_22/cvsfile/employees.csv")

df = pd.merge(df1,df2, on="Name")

df = df.drop_duplicates()
df = df.dropna()
print(df)
df = df.drop_duplicates(subset="Email")
print(df)