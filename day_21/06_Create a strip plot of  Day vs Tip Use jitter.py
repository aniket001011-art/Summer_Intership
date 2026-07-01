# Create a strip plot of:
# Day vs Tip
# Use jitter


import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
print(df)
sns.stripplot(df,x="day",y="tip", jitter=True)
plt.show()