
import os
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np

def minibatch_gradient_descent(
    file:str, 
    alpha:float=0.0023, 
    batch_size:int=100, 
    epochs_threshold:int=100000, 
    costdifference_threshold:float=0.00001, 
    plot:bool=False):
    '''
    The function calculates the beta values for the linear regression model
    using the mini batch gradient descent algorithm
    '''

    # load the training data
    training_data = pd.read_csv(filename, delimiter=',', header=0, index_col=False)

    # divide the data into features and labels
    X = training_data.drop(['y'], axis=1).to_numpy()
    # add a column of ones to the features matrix to account for the intercept, a0
    X = np.insert(X, 0, 1, axis=1)
    Y = training_data['y'].to_numpy()
    
    # length of the training data
    m = len(Y)
    print(f'Length of the training data: {m}')

    # initialize the y_hat vector to 0
    y_hat = np.zeros(len(Y))
    
    # beta will hold the values of the coefficients, hence it will be  the size 
    # of a row of the X matrix
    # initialize beta to random values
    beta = np.random.random(len(X[0]))

    # minibatches setting
    # number of minibatches = m => stochastic gradient descent
    # number of minibatches = 1 => batch gradient descent
    minibatches = int(m/batch_size)

    # initialize the number of epochs
    minibatch_count = 0

    previous_cumulative_cost = sys.float_info.max

    # loop until exit condition is met
    while True:

        cumulative_cost = 0

        for i in range(batch_size):

            # print(f'Minibatch: {i}')
            minibatch_X = X[i*minibatches:(i+1)*minibatches]
            minibatch_Y = Y[i*minibatches:(i+1)*minibatches]

            # calculate the hypothesis function for all training data
            y_hat = np.dot(beta, minibatch_X.T)
            #  calculate the residuals
            residuals = y_hat - minibatch_Y

            # calculate the new value of beta
            beta -= ( alpha / minibatches)  * np.dot(residuals, minibatch_X)

            # calculate the cost function
            cost = np.dot(residuals, residuals) / ( 2 * minibatches)
            cumulative_cost += cost

        # increase the number of iterations
        minibatch_count += 1

        cost_difference = previous_cumulative_cost - cumulative_cost
        # print(f'Epoch: {epochs}, average cost: {(cumulative_cost/minibatches_number):.3f}, beta: {beta}')
        previous_cumulative_cost = cumulative_cost
            
        # check if the cost function is converged or
        # iterations is greater than the threshold, break
        if abs(cost_difference) < costdifference_threshold or minibatch_count > epochs_threshold:
            break
    
    # calculate the cost for the training data and return the beta values and 
    # the number of iterations and the cost
    y_hat = np.dot(beta, X.T)
    residuals = y_hat - Y
    cost = np.dot(residuals, residuals) / ( 2 * m)
    
    return beta, minibatch_count, cost
    

if __name__ == '__main__':

    from timeit import default_timer as timer

    filename = os.path.join(os.path.dirname(__file__), '..', 'data_generation', 'data_2f.csv')
    alpha = 0.00023
    epochs_threshold = 1000
    costdifference_threshold = 0.00001
    plot = False
    batch_size = 64


    start = timer()
    beta, minibatch_count, cost = minibatch_gradient_descent(filename, alpha, batch_size, epochs_threshold, costdifference_threshold, plot)
    end = timer()
    print(f'Time: {end - start} beta: {beta}, minibatch_count: {minibatch_count}, cost: {cost}')
    