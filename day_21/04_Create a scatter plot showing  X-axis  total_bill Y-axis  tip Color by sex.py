# Create a scatter plot showing:
# X-axis → total_bill
# Y-axis → tip
# Color by sex

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
sns.scatterplot(df,x="total_bill",y="tip",hue="sex")
plt.show()