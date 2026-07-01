# Create a box plot showing:
# Day vs Total Bill
# Different colors for smokers and non-smokers

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
print(df)
sns.boxplot(df,x="day",y="total_bill", hue="smoker")
plt.show()