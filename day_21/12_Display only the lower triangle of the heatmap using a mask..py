# Display only the lower triangle of the heatmap using a mask.
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
 
# Load dataset
df = sns.load_dataset("tips")
corr = df.corr(numeric_only=True)
mask = np.tril(np.ones_like(corr, dtype=bool))
print(df)
 
# Heatmap
sns.heatmap(
    df.corr(numeric_only=True),
    cmap="coolwarm",
    annot=True,
    mask=mask
)
 
plt.show()