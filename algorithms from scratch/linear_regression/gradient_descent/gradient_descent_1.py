
import os
import numpy
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

def gradient_descent(file, alpha=0.0023, threshold_iterations=100000, costdifference_threshold=0.00001, plot=False):

    a0 = -5
    a1 = -3
    threshold_cost = 12

    current_directory = os.path.dirname(__file__)
    full_filename = os.path.join(current_directory, file)
    data_set = numpy.loadtxt(full_filename, delimiter=',', skiprows=1)

    epoch = 1
    cost = 0
    
    costs = []
    a_1s = []
    

    data_count = len(data_set)


    while True:

        sum_a0 = 0.0
        sum_a1 = 0.0
        sum_cost = 0.0
        cost = 0.0

        for idx in range(0, data_count):
            y_value = data_set[idx][1]
            x_value = data_set[idx][0]

            y_hat = a0 + (a1 * x_value)

            sum_a0 += (y_hat - y_value)
            sum_a1 += ((y_hat - y_value) * x_value)
            sum_cost += pow((y_hat - y_value), 2)

        a0 -= ((alpha * sum_a0) / data_count)
        a1 -= ((alpha * sum_a1) / data_count)
        
        cost = ((1 / (2 * data_count)) * sum_cost)

        epoch += 1
        
        costs.append(cost)
        a_1s.append(a1)
        
        if cost < threshold_cost or epoch > threshold_iterations:
            print(f'Cost Function: {cost}')
            print(f'Iterations: {epoch}')
            break
    
    if plot:
        plt.plot(a_1s[:], costs[:], '--bx', color='lightblue', mec='red')
        plt.xlabel('a1')
        plt.ylabel('cost')
        plt.title(r'Cost Function vs. a1, with $\alpha$ =' + str(alpha))
        plt.show()
        
    return a0, a1



if __name__ == '__main__':
    file = 'data.csv'
    alpha = 0.00023
    threshold_iterations = 100000
    costdifference_threshold = 0.00001
    plot = False
    
    a0, a1 = gradient_descent(file, alpha, threshold_iterations, costdifference_threshold, plot)
    print(f'a0: {a0}, a1: {a1}')