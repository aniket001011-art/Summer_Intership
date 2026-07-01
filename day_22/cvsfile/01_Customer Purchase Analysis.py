import pandas as pd
df1 = pd.read_csv("day_22/cvsfile/customers.csv")
df2 = pd.read_csv("day_22/cvsfile/products.csv")
# df3 = pd.read_csv("day_22/cvsfile/sales.csv")
df4 = pd.read_csv("day_22/cvsfile/orders.csv")
df = pd.merge(df1, df4, on="CustomerID")
df = pd.merge(df, df2, on="ProductID")
df = df.drop_duplicates()
print(df)
df.to_csv("day_22/cvsfile/main.csv")

df["OrderDate"] = pd.to_datetime(df["OrderDate"])
purchase_history = df.groupby("CustomerID")["OrderDate"].agg(First_Purchase="min",Last_Purchase="max")
print(purchase_history)

df = df.sort_values(["CustomerID", "OrderDate"])
df["Gap_Days"] = df.groupby("CustomerID")["OrderDate"].diff().dt.days
avg_gap = df.groupby("CustomerID")["Gap_Days"].mean()
print(avg_gap)


# last=df.groupby("CustomerName")["OrderDate"].max()
# print(last)
# latest=df["OrderDate"].max()
# print(latest)
# gap=latest-last
# print(gap)
# inactive=gap[gap.dt.days >90]
# print(inactive)

latest_date = df["OrderDate"].max()

last_purchase = df.groupby("CustomerID")["OrderDate"].max()

for customer, date in last_purchase.items():
    if (latest_date - date).days > 90:
        print(customer, "is inactive")