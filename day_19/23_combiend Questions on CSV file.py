import pandas as pd
df = pd.read_csv("C:\\Users\\anike\\Downloads\\student_submission_status.csv")
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())