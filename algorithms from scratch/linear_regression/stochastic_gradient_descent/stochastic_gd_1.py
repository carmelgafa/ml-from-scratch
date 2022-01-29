
import os
import matplotlib
from torch import rand
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np


def stochastic_gradient_descent(file, alpha):
    '''
    Implementation of Stochastic Gradient Descent
    
    Exit condition: 250 epochs
    '''
    
    np.random.seed(42)

    # load the training data
    full_filename = os.path.join(os.path.dirname(__file__), file)
    data_set = pd.read_csv(full_filename, delimiter=',', header=0, index_col=False)

    # training_data = training_data.sample(frac=1).reset_index(drop=True)

    # divide the data into features and labels
    X = data_set.drop(['y'], axis=1).to_numpy()
    
    # add a column of ones to the features matrix to account for the intercept, a0
    X = np.insert(X, 0, 1, axis=1)

    Y = data_set['y'].to_numpy()
    
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

    # loop until exit condition is met
    while True:
        
        i = np.random.randint(0, m)

        # print(f'Minibatch: {i}')
        x = X[i]
        y = Y[i]

        # calculate the hypothesis function for all training data
        y_hat = np.dot(beta, x.T)

        #  calculate the residuals
        residuals = y_hat - y

        # calculate the new value of beta
        beta -= (alpha * residuals * x)

        epochs += 1
  
        # check if the cost function is close enough to 0, if so, break or if the number of 
        # iterations is greater than the threshold, break
        if epochs > (m*250):
            break
    
    # calculate the cost for the training data and return the beta values and 
    # the number of iterations and the cost
    y_hat = np.dot(beta, X.T)
    residuals = y_hat - Y
    cost = np.dot(residuals, residuals) / ( 2 * m)
    
    return beta, epochs, cost


if __name__ == '__main__':

    from timeit import default_timer as timer

    file = 'data.csv'
    alpha = 0.0001
    start = timer()
    beta, epochs, cost = stochastic_gradient_descent(file, alpha) 
    end = timer()
    print(f'Time: {end - start}, beta: {beta}, epochs: {epochs}, cost: {cost}')
