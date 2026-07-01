import pandas as pd 
df = pd.read_csv("day_22/cvsfile/employees_missing.csv")
print(df)

#Fill missing salaries with department averages.
a = df["Salary"].mean()
ab = df.fillna({"Salary":a},inplace=True)
print(ab)

# Fill missing cities with the most common city.
b = df["City"].mode()[0]
bc = df.fillna({"City":b},inplace=True)
print(bc)
# Remove rows where more than 50% of values are missing.
c= len(df.columns) / 2
df_cleaned = df.dropna(thresh=c)
print(df_cleaned)


