import os
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
import pandas as pd
import sys

def two_feature_gradient_descent(filename, alpha=0.0023, epochs_threshold=100000, costdifference_threshold=0.00001, plot=False):
    '''
    Batched gradient descent for a two feature linear regression problem.
    This algorithm does not use any vectorization
    '''

    # initialize the coefficients
    a0 = 5
    a1 = 3
    a2 = 1

    data_set = None
    data_set = pd.read_csv(filename, delimiter=',', header=0, index_col=False)
    m = len(data_set)
    epoch = 0

    previous_cost = sys.float_info.max

    while True:
        # calculate the hypothesis function for all training data
        data_set['y_hat'] = a0 + (a1 * data_set['x1']) + (a2 * data_set['x2'])

        # calculate the difference between the hypothesis function and the
        # actual y value for all training data
        data_set['y_hat-y'] = data_set['y_hat'] - data_set['y']

        # multiply the difference by the x value for all training data
        data_set['y-hat-y.x1'] = data_set['y_hat-y'] * data_set['x1']
        data_set['y-hat-y.x2'] = data_set['y_hat-y'] * data_set['x2']

        # square the difference for all training data
        data_set['y-hat-y_sq'] = data_set['y_hat-y'] ** 2

        # update the a0 and a1 values
        a0 -= (alpha * (1/m) * sum(data_set['y_hat-y']))
        a1 -= (alpha * (1/m) * sum(data_set['y-hat-y.x1']))
        a2 -= (alpha * (1/m) * sum(data_set['y-hat-y.x2']))

        # calculate the cost function
        cost = sum(data_set['y-hat-y_sq']) / (2 * m)
        epoch += 1

        # check if the cost function has converged
        cost_difference = previous_cost - cost
        # print(f'Epoch: {epoch}, cost: {cost:.3f}, difference: {cost_difference:.6f}')
        previous_cost = cost

        # check if the cost function is diverging, if so, break
        if cost_difference < 0:
            print(f'Cost function is diverging. Stopping training.')
            break

        # check if the cost function is close enough to 0, if so, break or if the number of 
        # iterations is greater than the threshold, break
        if abs(cost_difference) < costdifference_threshold or epoch > epochs_threshold:
            break

    return a0, a1, a2, epoch, cost

if __name__ == '__main__':

    from timeit import default_timer as timer

    filename = os.path.join(os.path.dirname(__file__), '..', 'data_generation', 'data_2f.csv')
    alpha = 0.0023
    epochs_threshold = 100000
    costdifference_threshold = 0.00001
    plot = False

    start = timer()
    a0, a1, a2, epochs, cost = two_feature_gradient_descent(filename, alpha, epochs_threshold, costdifference_threshold, plot)
    end = timer()
    print(f'Time: {end - start}, a0: {a0}, a1: {a1}, a2: {a2} epochs: {epochs}, cost: {cost}')
