import os
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np


def multifeature_gradient_descent(
    filename,
    alpha=0.0023,
    epochs_threshold=100000,
    costdifference_threshold=0.00001,
    plot=False):

    X = None
    Y = None
    beta = None

    training_data = pd.read_csv(filename, delimiter=',', header=0, index_col=False)

    Y = training_data['y'].to_numpy()
    
    m = len(Y)

    X = training_data.drop(['y'], axis=1).to_numpy()
    
    # add a column of ones to the X matrix to account for the intercept, a0
    X = np.insert(X, 0, 1, axis=1)
    
    y_hat = np.zeros(len(Y))
    
    # beta will hold the values of the coefficients, hence it will be  the size 
    # of a row of the X matrix
    # Initializing the beta values to random values.
    # beta = np.random.random(len(X[0]))

    beta = np.array([5.0, 3.0, 1.0])

    iterations = 0

    # initialize the previous cost function value to a large number
    previous_cost = sys.float_info.max
    
    # store the cost function and a2 values for plotting
    costs = []
    a_2s = []
    
    while True:
        # calculate the hypothesis function for all training data
        y_hat = np.dot(beta, X.T)

        #  calculate the residuals
        residuals = y_hat - Y
        
        # calculate the new value of beta
        beta -= (alpha/m) * np.dot(residuals, X)

        # calculate the cost function
        cost = np.dot(residuals, residuals)/(2 * m)

        # increase the number of iterations
        iterations += 1

        # record the cost and a1 values for plotting
        costs.append(cost)
        a_2s.append(beta[2])
        
        cost_difference = previous_cost - cost

        # undelete this line to see details
        # print(f'Epoch: {iterations}, cost: {cost:.3f}, beta: {beta}')
        previous_cost = cost

        # check if the cost function is diverging, if so, break
        if cost_difference < 0:
            print(f'Cost function is diverging. Stopping training.')
            break
        
        # check if the cost function is close enough to 0, if so, break or if the number of 
        # iterations is greater than the threshold, break
        if abs(cost_difference) < costdifference_threshold or iterations > epochs_threshold:
            break
    
    if plot:
        # plot the cost function and a1 values
        plt.plot(a_2s[3:], costs[3:], '--bx', color='lightblue', mec='red')
        plt.xlabel('a2')
        plt.ylabel('cost')
        plt.title(r'Cost Function vs. a1, with $\alpha$ =' + str(alpha))
        plt.show()

    return beta

if __name__ == '__main__':

    from timeit import default_timer as timer

    filename = os.path.join(os.path.dirname(__file__), '..', 'data_generation', 'data_2f.csv')
    alpha = 0.0023
    epochs_threshold = 100000
    costdifference_threshold = 0.00001
    plot = False

    start = timer()
    beta = multifeature_gradient_descent(filename, alpha, epochs_threshold, costdifference_threshold, plot)
    end = timer()
    print(f'Time: {end - start}, beta: {beta}')
