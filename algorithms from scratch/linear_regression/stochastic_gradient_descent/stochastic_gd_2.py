
import os
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import pandas as pd
import sys
import numpy as np


def stochastic_gradient_descent(file, alpha=0.0023, epochs_threshold=100, costdifference_threshold=0.00001, plot=False):
    '''
    Implementation of Stochastic Gradient Descent
    
    '''

    np.random.seed(42)
    
    # load the training data
    full_filename = os.path.join(os.path.dirname(__file__), file)
    data_set = pd.read_csv(full_filename, delimiter=',', header=0, index_col=False)

    # create train and test sets
    mask = np.random.rand(len(data_set)) < 0.8
    training_data = data_set[mask]
    validation_data = data_set[~mask]

    # divide the data into features and labels
    X_train = data_set.drop(['y'], axis=1).to_numpy()
    # add a column of ones to the features matrix to account for the intercept, a0
    X_train = np.insert(X_train, 0, 1, axis=1)
    Y_train = data_set['y'].to_numpy()

    X_validation = validation_data.drop(['y'], axis=1).to_numpy()
    X_validation = np.insert(X_validation, 0, 1, axis=1)
    Y_validation = validation_data['y'].to_numpy()


    # length of the training data
    m = len(Y_train)

    # initialize the y_hat vector to 0
    y_hat = np.zeros(len(Y_train))
    
    # beta will hold the values of the coefficients, hence it will be  the size 
    # of a row of the X matrix
    # initialize beta to random values
    beta = np.random.random(len(X_train[0]))

    # initialize the number of epochs
    count = 0

    previous_validation_cost = sys.float_info.max

    # loop until exit condition is met
    while True:
        
        i = np.random.randint(0, m)

        # print(f'Minibatch: {i}')
        x = X_train[i]
        y = Y_train[i]

        # calculate the hypothesis function for all training data
        y_hat = np.dot(beta, x.T)

        #  calculate the residuals
        residuals = y_hat - y

        # calculate the new value of beta
        beta -= (alpha * residuals * x)

        count += 1

        if count % 1000 == 0:
            y_hat_validation = np.dot(beta, X_validation.T)
            residuals_validation = y_hat_validation - Y_validation
            cost_validation = np.dot(residuals_validation, residuals_validation) / ( 2 * len(Y_validation))
            
            if abs(previous_validation_cost - cost_validation) < costdifference_threshold:
                break
            else:
                previous_validation_cost = cost_validation
            
            # uncomment this line to see details
            # print(f'Epoch: {count/m} Cost: {cost_validation} beta: {beta}')
                    
        # check if the cost function is close enough to 0, if so, break or if the number of 
        # iterations is greater than the threshold, break
        if (count/m) > (epochs_threshold):
            break
    
    # calculate the cost for the training data and return the beta values and 
    # the number of iterations and the cost
    y_hat = np.dot(beta, X_train.T)
    residuals = y_hat - Y_train
    cost = np.dot(residuals, residuals) / ( 2 * m)
    
    return beta, count, cost


if __name__ == '__main__':

    from timeit import default_timer as timer

    file = 'data.csv'
    alpha = 0.00033
    epochs_threshold = 100
    costdifference_threshold = 0.005
    plot = False


    start = timer()
    beta, count, cost = stochastic_gradient_descent(file, alpha, epochs_threshold, costdifference_threshold, plot)
    end = timer()
    print(f'Time: {end - start}, beta: {beta}, count: {count}, cost: {cost}')
