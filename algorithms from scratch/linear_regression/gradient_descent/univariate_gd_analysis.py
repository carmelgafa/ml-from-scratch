from typing_extensions import _AnnotatedAlias
import numpy as np
import os
import matplotlib.pyplot as plt
import pandas as pd

# load training data
full_filename = os.path.join(os.path.dirname(__file__), 'data.csv')
data_set = pd.read_csv(full_filename, delimiter=',', names=['x', 'y'], index_col=False)

m = len(data_set)

#
# normalize data_set


a0, a1  = np.meshgrid(np.arange(-1000,1000,100), np.arange(-3,5,1))

ii, jj = np.shape(a0)

y = []

for i in range(ii):
    y_row = []
    for j in range(jj):
        y_hat = a0[i,j] + (a1[i,j] * data_set['x'])
        y_diff = y_hat - data_set['y']
        y_diff_sq = y_diff ** 2
        cost = sum(y_diff_sq) / (2 * m)
        # print(f'a0: {a0[i,j]:.2f}, a1: {a1[i,j]:.2f}, cost: {cost:.2f}')
        y_row.append(cost)
    y.append(y_row)
    
print(y)

fig = plt.figure()
ax = plt.axes(projection='3d')
# ax.contour3D(a0, a1, np.array(y), 50, cmap='binary')
# ax.plot_wireframe(a0, a1, np.array(y), color='black')
ax.plot_surface(a0, a1, np.array(y), rstride=1, cstride=1, cmap='viridis', edgecolor='none')
plt.show()


# df = pd.DataFrame(data=[a0.ravel(), a1.ravel(), cost.ravel()]).T
# df = df.sample(frac=0.1)
# df.columns = ['a0', 'a1', 'J']

# # plot the data
# y = df.iloc[:,1]
# x = df.iloc[:,0]
# z = df.iloc[:,2]


# fig = plt.figure(figsize=(12, 12))
# ax = fig.add_subplot(projection='3d')
# ax.scatter(x,y,z, cmap='coolwarm')
# plt.show()