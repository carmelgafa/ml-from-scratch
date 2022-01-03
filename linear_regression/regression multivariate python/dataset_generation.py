import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(projection='3d')

x1_lower = -10
x1_higher = 10
x1_step = (x1_higher - x1_lower) / 100
x1 = np.arange(x1_lower, x1_higher, x1_step)

x2_lower = 0
x2_higher = 50
x2_step = (x2_higher - x2_lower) / 100
x2= np.arange(x2_lower, x2_higher, x2_step)

# generate the plane
xx1, xx2 = np.meshgrid(x1, x2)
y = 12 + (5 * xx1) + (-3 * xx2)

# add random_multiplier to y
random_multiplier = 5
e = np.random.randn(len(xx1), len(xx2) )*random_multiplier
yy = y + e


df = pd.DataFrame(data=[xx1.ravel(), xx2.ravel(), yy.ravel()]).T
df = df.sample(frac=0.01)
df.columns = ['x1', 'x2', 'y']
df.to_csv("data.csv", header=True, index=False)

# plot the data
y = df.iloc[:,1]
x = df.iloc[:,0]
z = df.iloc[:,2]
ax.scatter(x,y,z, cmap='coolwarm')
plt.show()


