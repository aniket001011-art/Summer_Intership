# Create a line plot using the flights dataset showing:

# Year vs Passengers
# Separate line for each month

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="darkgrid")

df = sns.load_dataset("flights")
print(df)
sns.lineplot(df,x="year",y="passengers", hue="month")
plt.show()