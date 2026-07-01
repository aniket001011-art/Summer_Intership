import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Marks": [80, 85, 90, 95, 100, 78, 88]
}

df = pd.DataFrame(data)

df.plot(kind="box")

plt.show()