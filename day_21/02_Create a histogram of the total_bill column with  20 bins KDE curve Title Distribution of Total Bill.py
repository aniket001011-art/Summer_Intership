# Create a histogram of the total_bill column with:
# 20 bins
# KDE curve
# Title: "Distribution of Total Bill"
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
sns.histplot(df,x="total_bill",bins=20)
plt.hist(df,x="total_bill",bins=20)
plt.show()