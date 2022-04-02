from operator import index
from typing_extensions import _AnnotatedAlias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import cm

def plot_univariate_gd_analysis(file:str, a0_range:tuple, a1_range:tuple, gd_points:list, plot_slices=False):
    '''
    '''

    # read the data set
    data_set = pd.read_csv(file, delimiter=',', index_col=False)
    m = len(data_set)

    # plot the costs surface
    a0, a1  = np.meshgrid(
        np.arange(a0_range[0], a0_range[1], a0_range[2]),
        np.arange(a1_range[0], a1_range[1], a1_range[2]))
    ii, jj = np.shape(a0)


    costs = []
    for i in range(ii):
        cost_row = []
        for j in range(jj):
            y_hat = a0[i,j] + (a1[i,j] * data_set['x'])
            y_diff = y_hat - data_set['y']
            y_diff_sq = y_diff ** 2
            cost = sum(y_diff_sq) / (2 * m)
            cost_row.append(cost)
        costs.append(cost_row)


    if plot_slices:

        a0_mincost_idx = np.where(np.round(a0[0,:], 1)==150)
        a1_mincost =  a1[:, a0_mincost_idx].squeeze()
        ncosts = np.array(costs)
        costs_mincosts = ncosts[:,a0_mincost_idx[0].squeeze()]

        plt.rcParams['text.usetex'] = True
        plt.plot(a1_mincost, costs_mincosts)
        plt.xlabel(r'$a_1$')
        plt.ylabel(r'$J(150,a_1$)')
        
        plt.show()


        a1_mincost_idx = np.where(np.round(a1[:,0], 1)==20)
        a0_mincost =  a0[a1_mincost_idx, :].squeeze()
        ncosts = np.array(costs)
        costs_mincosts = ncosts[a1_mincost_idx[0].squeeze(), :]

        plt.rcParams['text.usetex'] = True
        plt.plot(a0_mincost, costs_mincosts)
        plt.xlabel(r'$a_1$')
        plt.ylabel(r'$J(a_0, 20$)')

        plt.show()

    # plot the gradient descent points
    xx = []
    yy = []
    zz = []
    for item in gd_points:
        xx.append(item[0])
        yy.append(item[1])
        zz.append(item[2])

    plt.rcParams['text.usetex'] = True
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.plot_surface(a0, a1, np.array(costs), rstride=1, cstride=1, cmap='cividis', edgecolor='none', alpha=0.5)
    ax.contour(a0, a1, np.array(costs), zdir='z', offset=-0.5, cmap=cm.coolwarm)
    ax.plot(xx, yy, zz, 'r.--', alpha=1)
    ax.set_xlabel(r'$a_0$')
    ax.set_ylabel(r'$a_1$')
    ax.set_zlabel(r'$J(a_0, a_1)$')
    plt.show()

if __name__=='__main__':
    import os

    plot_univariate_gd_analysis(
        file=os.path.join(os.path.dirname(__file__), 'data_generation', 'data_1f.csv'),
        a0_range=(125,175,0.2), 
        a1_range=(18,22,0.2), 
        gd_points= [],
        plot_slices=True)
