
import os
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np


def stochastic_gradient_descent(filename:str, alpha:float, max_epochs:int = 5):
    '''
    The stochastic gradient descent function takes a dataset, a learning rate, and a maximum number of
    epochs. 
    It returns the beta values and the cost.
    '''
    
    np.random.seed(42)

    # load the training data
    data_set = pd.read_csv(filename, delimiter=',', header=0, index_col=False)

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
        if epochs > (m*max_epochs):
            break
    
    # calculate the cost for the training data and return the beta values and 
    # the number of iterations and the cost
    y_hat = np.dot(beta, X.T)
    residuals = y_hat - Y
    cost = np.dot(residuals, residuals) / ( 2 * m)
    
    return beta, cost


if __name__ == '__main__':

    from timeit import default_timer as timer

    filename = os.path.join(os.path.dirname(__file__), '..', 'data_generation', 'data_1f.csv')
    alpha = 0.0004
    max_epochs = 4000
    start = timer()
    beta, cost = stochastic_gradient_descent(filename, alpha, max_epochs) 
    end = timer()
    print(f'Time: {end - start}, beta: {beta}, cost: {cost}')
