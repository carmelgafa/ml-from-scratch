
import os
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
import pandas as pd
import sys

def gradient_descent(file, alpha=0.0023, maximum_epochs=100000, costdifference_threshold=0.00001, plot=False):

    
    a0 = 5
    a1 = 3
    
    full_filename = os.path.join(os.path.dirname(__file__), file)
    data_set = pd.read_csv(full_filename, delimiter=',', names=['x', 'y'], index_col=False)

    m = len(data_set)
    epoch = 0

    previous_cost = sys.float_info.max
    
    costs = []
    a_1s = []
    
    while True:
        # calculate the hypothesis function for all training data
        data_set['y_hat'] = a0 + (a1 * data_set['x'])
        
        # calculate the difference between the hypothesis function and the
        # actual y value for all training data
        data_set['y_hat-y'] = data_set['y_hat'] - data_set['y']
        
        # multiply the difference by the x value for all training data
        data_set['y-hat-y.x'] = data_set['y_hat-y'] * data_set['x']
        
        # square the difference for all training data
        data_set['y-hat-y_sq'] = data_set['y_hat-y'] ** 2
        
        # update the a0 and a1 values
        a0 -= (alpha * (1/m) * sum(data_set['y_hat-y']))
        a1 -= (alpha * (1/m) * sum(data_set['y-hat-y.x']))
        
        # calculate the cost function
        cost = sum(data_set['y-hat-y_sq']) / (2 * m)
        epoch += 1

        # record the cost and a1 values for plotting
        costs.append(cost)
        a_1s.append(a1)
        
        cost_difference = previous_cost - cost
        print(f'Epoch: {epoch}, cost: {cost:.3f}, difference: {cost_difference:.6f}')
        previous_cost = cost

        # check if the cost function is diverging, if so, break
        if cost_difference < 0:
            print(f'Cost function is diverging. Stopping training.')
            break
        
        # check if the cost function is close enough to 0, if so, break or if the number of 
        # iterations is greater than the threshold, break
        if abs(cost_difference) < 0.00001 or epoch > maximum_epochs:
            break
    
    if plot:
        # plot the cost function and a1 values
        plt.plot(a_1s[:], costs[:], '--bx', color='lightblue', mec='red')
        plt.xlabel('a1')
        plt.ylabel('cost')
        plt.title(r'Cost Function vs. a1, with $\alpha$ =' + str(alpha))
        plt.show()

    return a0, a1

if __name__ == '__main__':

    file = 'data.csv'
    alpha = 0.0005
    threshold_iterations = 100000
    costdifference_threshold = 0.00001
    plot = False
    
    a0, a1 = gradient_descent(file, alpha, threshold_iterations, costdifference_threshold, plot)
    print(f'a0: {a0:.3f}, a1: {a1:.3f}')