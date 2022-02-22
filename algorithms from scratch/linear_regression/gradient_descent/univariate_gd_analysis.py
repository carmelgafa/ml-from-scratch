from operator import index
from typing_extensions import _AnnotatedAlias
import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd

# load training data
full_filename = os.path.join(os.path.dirname(__file__), 'data.csv')
data_set = pd.read_csv(full_filename, delimiter=',', names=['x', 'y'], index_col=False)

m = len(data_set)

a0, a1  = np.meshgrid(np.arange(125,175,0.5), np.arange(18,22,0.5))

ii, jj = np.shape(a0)

y = []
for i in range(ii):
    y_row = []
    for j in range(jj):
        y_hat = a0[i,j] + (a1[i,j] * data_set['x'])
        y_diff = y_hat - data_set['y']
        y_diff_sq = y_diff ** 2
        cost = sum(y_diff_sq) / (2 * m)
        y_row.append(cost)
    y.append(y_row)

min_idx = np.unravel_index(np.argmin(y), np.shape(y))

print(min_idx)

print(a0[min_idx])
print(a1[min_idx])

fig = plt.figure()
ax = plt.axes(projection='3d')



xx = a0[min_idx]
yy = a1[min_idx]
zz = y[min_idx[0]][min_idx[1]]


ax.plot_surface(a0, a1, np.array(y), rstride=1, cstride=1, cmap='cividis', edgecolor='none', alpha=0.5)

ax.plot(xx, yy, zz, 'ro', alpha=1)






plt.show()
