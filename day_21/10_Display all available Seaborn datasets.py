# Display all available Seaborn datasets.

import seaborn as sns
import matplotlib.pyplot as plt

df = sns.get_dataset_names()
print(df)