# Challenge 1: The Random Matrix (Simulation)
# Goal: Generate random data instantly.
# Tasks:Use np.random.randint() to create a 2D matrix with 2 rows and 4 columns.
# The random integers must be between 1 and 100.Print the generated matrix.

import numpy as np
x = np.random.randint(1,101,(2,4))
print(x)