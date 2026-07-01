# Load the tips dataset and:
# Display the first 10 rows.
# Print the dataset shape.
# Display column names.

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
print(df.head(10))
print(df.shape)
print(df.columns)