from operator import index
from typing_extensions import _AnnotatedAlias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm

def plot_univariate_gd_analysis(file:str, a0_range:tuple, a1_range:tuple, gd_points:list):
    '''
    '''

    data_set = pd.read_csv(file, delimiter=',', index_col=False)

    m = len(data_set)

    a0, a1  = np.meshgrid(
        np.arange(a0_range[0], a0_range[1], a0_range[2]),
        np.arange(a1_range[0], a1_range[1], a1_range[2]))

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

    fig = plt.figure()
    ax = plt.axes(projection='3d')

    xx = []
    yy = []
    zz = []

    for item in gd_points:
        xx.append(item[0])
        yy.append(item[1])
        zz.append(item[2])

    ax.plot_surface(a0, a1, np.array(y), rstride=1, cstride=1, cmap='cividis', edgecolor='none', alpha=0.5)
    ax.contour(a0, a1, np.array(y), zdir='z', offset=-0.5, cmap=cm.coolwarm)
    ax.plot(xx, yy, zz, 'r.--', alpha=1)

    plt.show()

# if __name__=='__main__':
#     plot_univariate_gd_analysis(
#         file='data.csv', 
#         a0_range=(125,175,0.2), 
#         a1_range=(18,22,0.2), 
#         gd_points= [(150, 20, 200), (140, 21, 200)])