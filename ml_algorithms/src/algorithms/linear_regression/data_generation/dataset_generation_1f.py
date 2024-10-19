'''
single feature data generation
'''
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def generate_data(a0, a1, noise_sigma, file_name, plot=False):
    '''
    Generates 100 points with m slope and c intercept 
    and adds noise with sigma
    '''

    # x between 0 and 100 in steps of 1
    x = np.arange(0, 101, 1)

    # generate a noisy line
    np.random.seed(42)
    l = (a1*x) + a0
    e = np.random.randn(len(x))*noise_sigma
    y = l + e

    file_path = os.path.join(os.path.dirname(__file__), file_name)
    # save the data to a csv file
    df = pd.DataFrame(data=[x, y]).T
    df.columns = ['x', 'y']
    df.to_csv(file_path, header=True, index=False)

    # plot the data
    if plot:
        plt.plot(x, y)
        plt.plot(x, l, '--')
        plt.xlim([min(x), max(x)])
        plt.ylim([min(y), max(y)])
        plt.show()

if __name__=='__main__':
    generate_data(a0=150, a1=20, noise_sigma=20, file_name="data_1f.csv", plot=True)
