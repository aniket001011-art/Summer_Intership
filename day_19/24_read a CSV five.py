import pandas as pd
df = pd.read_csv("C:\\Users\\anike\\Downloads\\student_submission_status.csv")
print(df.isnull().sum())

