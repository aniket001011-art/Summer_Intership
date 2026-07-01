import pandas as pd
df = pd.read_csv("day_22/cvsfile/MultiIndex_Challenge_Dataset.csv")
df = df.drop_duplicates()
df = df.dropna()
print(df)
# df1 = df.groupby("Country")["Sales"].agg(mean="mean",median="median",sum="sum",max="max",min="min")
# print(df1)

# # # use groupby to separate all countries and then extract the India group:
# df2 = df[df["Country"] == "India"]["City"]
# print(df2)
# #If you want to split your entire dataset into two groups (True for India, False for all other countries) and see the cities:
# # df2 = df.groupby(["Country"]=="India")["City"]
# # for is_india, cities in df2:
# #     print(is_india)
# #     print(cities)

# # select all cities in punjab
# df3 = df[df["State"] == "Punjab"]["City"]
# print(df3)

# # total slars by country
# df4 = df.groupby("Country")["Sales"].agg(Total_Sales="sum",)
# print(df4)

# # total slars by state
# df5 = df.groupby(["Country","State"])["Sales"].agg(Total_Sales="sum",)
# print(df5)

# #reset Indexing 
# df.reset_index(inplace=True)
# print(df)

# Calculate the percentage contribution of each city to its country's total sales.
df6 = df.groupby("Country")["Sales"].transform("sum")
print(df6)
Percentage_Contribution = (df["Sales"] / df6) * 100
print(Percentage_Contribution)

# Swap the index level

cols = list(df.columns)
cols[0],cols[1] = cols[1],cols[0]
df.columns = cols
df[["State","Country"]]=df[["Country","State"]]

print(df)

df7 = df[df["State"] == "California"]
print("\n",df7)

#Filter only those states where the average sales exceed 1500.
df8 = df.groupby("State")["Sales"].mean()>1500
print("\n",df8)

#Add a new column: Performance
# using the function 
def rate(Sales):
      if Sales>2000:
          return "Excellent"
      elif Sales >= 1500 and Sales <= 2000:
          return "Good"
      else:
          return "Average"

df["Performace"]=df["Sales"].apply(rate)
print(df)

# # using loc 
# df.loc[df["Sales"]>2000,"performance"]="excellent"
# df.loc[(df["Sales"] >= 1500) & (df["Sales"] <= 2000),"performance"] = "Good"
# df.loc[(df["Sales"]< 1500), "performance"] = "average"
# print(df)