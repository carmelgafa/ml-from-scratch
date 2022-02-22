
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
    The function calculates the beta values for the linear regression model using the mini batch gradient descent
    algorithm.
    contains a validation set to detect convergence
    This variation contains learning rate decay
    '''
    alpha_0 = alpha

    # load the training data
    full_filename = os.path.join(os.path.dirname(__file__), file)
    data_set = pd.read_csv(full_filename, delimiter=',', header=0, index_col=False)

    # create train and test sets
    mask = np.random.rand(len(data_set)) < 0.8
    training_data = data_set[mask]
    validation_data = data_set[~mask]

    # divide the data into features and labels
    X_train = training_data.drop(['y'], axis=1).to_numpy()
    # add a column of ones to the features matrix to account for the intercept, a0
    X_train = np.insert(X_train, 0, 1, axis=1)
    Y_train = training_data['y'].to_numpy()

    X_validation = validation_data.drop(['y'], axis=1).to_numpy()
    X_validation = np.insert(X_validation, 0, 1, axis=1)
    Y_validation = validation_data['y'].to_numpy()

    # length of the training data
    m = len(Y_train)
    print(f'Length of the training data: {m}')

    # initialize the y_hat vector to 0
    y_hat = np.zeros(len(Y_train))
    
    # beta will hold the values of the coefficients, hence it will be  the size 
    # of a row of the X matrix
    # initialize beta to random values
    beta = np.random.random(len(X_train[0]))

    # minibatches setting
    # number of minibatches = m => stochastic gradient descent
    # number of minibatches = 1 => batch gradient descent
    minibatch_size = int(m/batch_size)

    # initialize the number of epochs
    epoch_count = 0

    # initialize the previous cost function value to a large number
    # previous_cost = sys.float_info.max

    previous_validation_cost = sys.float_info.max
    
    # loop until exit condition is met
    while True:

        for i in range(batch_size):

            # print(f'Minibatch: {i}')
            minibatch_X = X_train[i*minibatch_size:(i+1)*minibatch_size]
            minibatch_Y = Y_train[i*minibatch_size:(i+1)*minibatch_size]

            # calculate the hypothesis function for all training data
            y_hat = np.dot(beta, minibatch_X.T)
            #  calculate the residuals
            residuals = y_hat - minibatch_Y
            
            
            # calculate the new value of beta
            beta -= ( alpha / minibatch_size)  * np.dot(residuals, minibatch_X)

            # calculate the cost function
            cost = np.dot(residuals, residuals) / ( 2 * minibatch_size)

        # increase the number of iterations
        epoch_count += 1

        alpha = alpha_0 / (1 + (epoch_count / 100))

        if epoch_count % 10 == 0:
            y_hat_validation = np.dot(beta, X_validation.T)
            residuals_validation = y_hat_validation - Y_validation
            cost_validation = np.dot(residuals_validation, residuals_validation) / ( 2 * len(Y_validation))
            
            if abs(previous_validation_cost - cost_validation) < costdifference_threshold:
                print(f'Cost difference is {cost_validation} less than {costdifference_threshold} in epoch {epoch_count}')
                break
            else:
                previous_validation_cost = cost_validation

            
        # check if the cost function is close enough to 0, if so, break or if the number of 
        # iterations is greater than the threshold, break
        if epoch_count > epochs_threshold:
            print(f'Number of iterations exceeded {epochs_threshold}')
            break

    # calculate the cost for the training data and return the beta values and 
    # the number of iterations and the cost
    y_hat = np.dot(beta, X_train.T)
    residuals = y_hat - Y_train
    cost = np.dot(residuals, residuals) / ( 2 * m)
    
    return beta, epoch_count, cost
    

if __name__ == '__main__':

    from timeit import default_timer as timer

    file = 'data.csv'
    alpha = 0.0023
    epochs_threshold = 10000
    costdifference_threshold = 0.0001
    plot = False
    batch_size = 64


    start = timer()
    beta, epoch_count, cost = minibatch_gradient_descent(file, alpha, batch_size, epochs_threshold, costdifference_threshold, plot)
    end = timer()
    print(f'Time: {end - start} beta: {beta}, epoch_count: {epoch_count}, cost: {cost}')
    