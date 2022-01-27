
import os
import matplotlib
from torch import rand
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np
from random import seed
from random import random

def LinearRegression(a, cd):

    file = 'data.csv'
    
    alpha = a
    threshold_iterations = 90000
    costdifference_threshold = cd

    # load the training data
    full_filename = os.path.join(os.path.dirname(__file__), file)
    training_data = pd.read_csv(full_filename, delimiter=',', header=0, index_col=False)

    # training_data = training_data.sample(frac=1).reset_index(drop=True)

    # divide the data into features and labels
    X = training_data.drop(['y'], axis=1).to_numpy()
    # add a column of ones to the features matrix to account for the intercept, a0
    X = np.insert(X, 0, 1, axis=1)

    Y = training_data['y'].to_numpy()
    
    # length of the training data
    m = len(Y)

    # initialize the y_hat vector to 0
    y_hat = np.zeros(len(Y))
    
    # beta will hold the values of the coefficients, hence it will be  the size 
    # of a row of the X matrix
    # initialize beta to random values
    beta = np.random.random(len(X[0]))


    # initialize the number of epochs
    epochs = 0


    
    previous_cumulative_cost = sys.float_info.max
    
    # loop until exit condition is met
    while True:

        cumulative_cost = 0

        i = (int)(random()*m)


        # print(f'Minibatch: {i}')
        x = X[i]
        y = Y[i]

        # calculate the hypothesis function for all training data
        y_hat = np.dot(beta, x.T)

        #  calculate the residuals
        residuals = y_hat - y

        # calculate the new value of beta
        beta -= (alpha * residuals * x)

        # calculate the cost function
        cost = (residuals**2)/(2*m)

        cumulative_cost += cost

        epochs += 1


        # check if the cost function is close enough to 0, if so, break or if the number of 
        # iterations is greater than the threshold, break
        if epochs > threshold_iterations:
            break


    
    # calculate the cost for the training data and return the beta values and 
    # the number of iterations and the cost
    y_hat = np.dot(beta, X.T)
    residuals = y_hat - Y
    cost = np.dot(residuals, residuals) / ( 2 * m)
    
    return beta, epochs, cost
    

if __name__ == '__main__':

    from timeit import default_timer as timer

   
    start = timer()
    print(LinearRegression(0.0001, 0.0000000001))
    end = timer()
    print(f'Time: {end - start}')
