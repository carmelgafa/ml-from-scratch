# We generate a random dataset of points in a plane, and then add some noise to the y-values. We then
# save the data to a csv file.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

def generate_data(a0, a1, a2, noise_sigma, plot=False):

    x1_lower = -10
    x1_higher = 10
    x1_step = (x1_higher - x1_lower) / 1000
    x1 = np.arange(x1_lower, x1_higher, x1_step)

    x2_lower = 0
    x2_higher = 50
    x2_step = (x2_higher - x2_lower) / 1000
    x2= np.arange(x2_lower, x2_higher, x2_step)

    # generate the plane
    xx1, xx2 = np.meshgrid(x1, x2)
    y = a0 + (a1 * xx1) + (a2 * xx2)

    # add random_multiplier to y
    np.random
    random_multiplier = noise_sigma
    e = np.random.randn(len(xx1), len(xx2) )*random_multiplier
    yy = y + e

    df = pd.DataFrame(data=[xx1.ravel(), xx2.ravel(), yy.ravel()]).T
    df = df.sample(frac=0.01)
    df.columns = ['x1', 'x2', 'y']

    full_filename = os.path.join(os.path.dirname(__file__), "data_2f.csv")
    df.to_csv(full_filename, header=True, index=False)

    if plot:
        # plot the data
        fig = plt.figure(figsize=(12, 12))
        ax = fig.add_subplot(projection='3d')
        y = df.iloc[:,1]
        x = df.iloc[:,0]
        z = df.iloc[:,2]
        ax.scatter(x,y,z, cmap='coolwarm')
        plt.show()

if __name__=='__main__':
    generate_data(a0=12, a1=5, a2=-3, noise_sigma=5, plot=True)