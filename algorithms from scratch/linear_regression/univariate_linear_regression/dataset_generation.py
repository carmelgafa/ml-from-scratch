'''
single feature data generation
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

def generate_data(m, c, noise_sigma, plot=False):
    '''
    Generates 100 points with m slope and c intercept 
    and adds noise with sigma
    '''

    # x between 0 and 100 in steps of 1
    x = np.arange(0, 101, 1)

    # generate a noisy line
    np.random.seed(42)
    l = (m*x) + c
    e = np.random.randn(len(x))*noise_sigma
    y = l + e

    file_path = os.path.join(os.path.dirname(__file__), 'data.csv')
    # save the data to a csv file
    pd.DataFrame(y).to_csv(file_path, header=False, index=True)

    # plot the data
    if plot:
        plt.plot(x, y)
        plt.plot(x, l, '--')
        plt.xlim([min(x), max(x)])
        plt.ylim([min(y), max(y)])
        plt.show()

if __name__=='__main__':
    generate_data(m=20, c=150, noise_sigma=0, plot=True)