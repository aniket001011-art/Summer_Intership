import pandas as pd
df = pd.read_csv("day_22/cvsfile/sales.csv")

df["Date"]= pd.to_datetime( df["Date"], errors="coerce")

df["Month"]= df["Date"].dt.month
print(df)
Month_sales_region = df.groupby(["Month","Region"])["Sales"].sum()
print(Month_sales_region)

monthly_sales = df.groupby(["Month","Product"])["Sales"].sum().reset_index()
print(monthly_sales)
top_3 = monthly_sales.groupby("Month")["Sales"].nlargest(3).reset_index()
print(top_3)

Growth_percentage = df.groupby("Month")["Sales"].sum()

print(Growth_percentage)
for i, j in zip(Growth_percentage, Growth_percentage[1:]):
    growth = ((j - i) / i) * 100
    print(growth)