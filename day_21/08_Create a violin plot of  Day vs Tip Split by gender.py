# Create a violin plot of:
# Day vs Tip
# Split by gender

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
print(df)
sns.violinplot(df,x="day",y="tip", hue="sex")
plt.show()