# Create a heatmap of the correlation matrix for the tips dataset with:
# Annotation
# coolwarm color map
# Square cells


import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
sns.heatmap(df.corr(numeric_only =True), cmap="coolwarm",annot=True)
plt.show()