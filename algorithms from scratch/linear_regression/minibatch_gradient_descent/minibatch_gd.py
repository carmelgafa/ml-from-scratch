
import os
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np

def minibatch_gradient_descent(file:str, alpha:float=0.0023, batch_size:int=100, epochs_threshold:int=100000, costdifference_threshold:float=0.00001, plot:bool=False):
    '''
    The function calculates the beta values for the linear regression model using the gradient descent
    algorithm
    
    :param file: the name of the file that contains the training data
    :type file: str
    :param alpha: the learning rate
    :type alpha: float
    :param batch_size: the number of rows in the training data that will be used to calculate the
    gradient, defaults to 100
    :type batch_size: int (optional)
    :param epochs_threshold: the number of epochs to run before stopping, defaults to 100000
    :type epochs_threshold: int (optional)
    :param costdifference_threshold: The threshold for the difference in the cost function between the
    current and previous iterations. If the difference is less than this threshold, the training will
    stop
    :type costdifference_threshold: float
    :param plot: If you want to plot the cost function vs. the number of iterations, defaults to False
    :type plot: bool (optional)
    :return: the beta values, the number of iterations and the cost.
    '''

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
    minibatch_size = int(m/batch_size)

    # initialize the number of epochs
    epoch_count = 0

    # initialize the previous cost function value to a large number
    # previous_cost = sys.float_info.max
    
    # store the cost function and a2 values for plotting
    costs = []
    a_2s = []
    
    previous_cumulative_cost = sys.float_info.max
    
    # loop until exit condition is met
    while True:

        cumulative_cost = 0

        for i in range(batch_size):

            # print(f'Minibatch: {i}')
            minibatch_X = X[i*minibatch_size:(i+1)*minibatch_size]
            minibatch_Y = Y[i*minibatch_size:(i+1)*minibatch_size]

            # calculate the hypothesis function for all training data
            y_hat = np.dot(beta, minibatch_X.T)
            #  calculate the residuals
            residuals = y_hat - minibatch_Y
            
            
            # calculate the new value of beta
            beta -= ( alpha / minibatch_size)  * np.dot(residuals, minibatch_X)

            # calculate the cost function
            cost = np.dot(residuals, residuals) / ( 2 * minibatch_size)

            cumulative_cost += cost

        # increase the number of iterations
        epoch_count += 1

        # record the cost and a1 values for plotting
        #     costs.append(cost)
        #     a_2s.append(__beta[2])

        cost_difference = previous_cumulative_cost - cumulative_cost
        # print(f'Epoch: {epochs}, average cost: {(cumulative_cost/minibatches_number):.3f}, beta: {beta}')
        previous_cumulative_cost = cumulative_cost

        # check if the cost function is diverging, if so, break
        # if cost_difference < 0:
        #     print(f'Cost function is diverging. Stopping training.')
        #     break
            
        # check if the cost function is close enough to 0, if so, break or if the number of 
        # iterations is greater than the threshold, break
        if abs(cost_difference) < costdifference_threshold or epoch_count > epochs_threshold:
            break

    # # plot the cost function and a1 values
    # plt.plot(a_2s[3:], costs[3:], '--bx', color='lightblue', mec='red')
    # plt.xlabel('a2')
    # plt.ylabel('cost')
    # plt.title(r'Cost Function vs. a1, with $\alpha$ =' + str(__alpha))
    # plt.show()
    
    # calculate the cost for the training data and return the beta values and 
    # the number of iterations and the cost
    y_hat = np.dot(beta, X.T)
    residuals = y_hat - Y
    cost = np.dot(residuals, residuals) / ( 2 * m)
    
    return beta, epoch_count, cost
    

if __name__ == '__main__':

    from timeit import default_timer as timer

    file = 'data.csv'
    alpha = 0.00023
    epochs_threshold = 1000
    costdifference_threshold = 0.00001
    plot = False
    batch_size = 100


    start = timer()
    beta, epoch_count, cost = minibatch_gradient_descent(file, alpha, batch_size, epochs_threshold, costdifference_threshold, plot)
    end = timer()
    print(f'Time: {end - start} beta: {beta}, epoch_count: {epoch_count}, cost: {cost}')
    