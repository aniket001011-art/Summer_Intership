# Create a count plot showing:

# Number of customers for each day


import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
print(df)
sns.countplot(df,x="day")
plt.show()