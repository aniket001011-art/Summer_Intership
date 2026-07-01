import pandas as pd
data = {
    "Joining_Date":["2026-06-20","2026-06-21","2026-06-22"]
}
df = pd.DataFrame(data)
df["Joingin_Date"] = pd.to_datetime(df["Joining_Date"])
print(df)
print(df.dtypes)