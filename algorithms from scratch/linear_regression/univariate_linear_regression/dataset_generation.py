import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# x between 0 and 100 in steps of 1
x = np.arange(0, 101, 1)

# generate a noisy line

np.random.seed(42)

l = (2*x) + 15
random_multiplier = 5
e = np.random.randn(len(x))*random_multiplier
y = l + e

# plot the data
plt.plot(x, y)
plt.plot(x, l, '--')
plt.xlim([0, 101])
plt.ylim([0, 200])
plt.show()

# save the data to a csv file
pd.DataFrame(y).to_csv("data.csv", header=False, index=True)
