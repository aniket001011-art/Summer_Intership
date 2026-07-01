# Create a KDE plot of the tip column with:
# Filled area
# Grid enabled

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
sns.kdeplot(df,x="tip")
plt.show()