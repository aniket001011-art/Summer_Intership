import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Year": [2022, 2023, 2024, 2025],
    "Profit": [50, 70, 90, 120]
}

df = pd.DataFrame(data)

df.plot(x="Year", y="Profit", kind="area")

plt.show()