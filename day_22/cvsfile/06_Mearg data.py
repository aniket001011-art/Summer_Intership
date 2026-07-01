import pandas as pd 
df = pd.read_csv("day_22/cvsfile/orders.csv")
df1 = pd.read_csv("day_22/cvsfile/customers.csv")
df2 = pd.read_csv("day_22/cvsfile/products.csv")


df = pd.merge(df1, df4, on="CustomerID")
df = pd.merge(df, df2, on="ProductID")