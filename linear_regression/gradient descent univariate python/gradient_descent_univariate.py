
import os
import numpy
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt

class UnivariateGradientDescent:
    '''
    Gradient Descent Univariate utilizing numpy
    not very efficient but easier to follow
    '''

    def __init__(self, alpha):
        self.__a0 = -5
        self.__a1 = -3
        self.__training_data = []
        self.__alpha = alpha
        self.__threshold_iterations = 100000
        self.__threshold_cost = 12

    def __load_training_data(self, file):
        '''
        Loads the training data from a file
        '''
        current_directory = os.path.dirname(__file__)
        full_filename = os.path.join(current_directory, file)
        self.__training_data = numpy.loadtxt(full_filename, delimiter=',', skiprows=1)

    def get_y_value(self, x_value):
        '''
        return an estimated y value given an x value based on the training results
        '''
        return self.__calculate_hypothesis(x_value)

    def train(self, file):
        '''
        starts the training procedure
        '''
        self.__load_training_data(file)
        counter = 1
        cost = 0
        
        costs = []
        a_1s = []
        
        while True:
            cost = self.__calculate_cost_function()
            counter += 1
            
            costs.append(cost)
            a_1s.append(self.__a1)
            
            if cost < self.__threshold_cost or counter > self.__threshold_iterations:
                print(f'Cost Function: {cost}')
                print(f'Iterations: {counter}')
                break
        
        plt.plot(a_1s[:], costs[:], '--bx', color='lightblue', mec='red')
        plt.xlabel('a1')
        plt.ylabel('cost')
        plt.title(r'Cost Function vs. a1, with $\alpha$ =' + str(self.__alpha))
        plt.show()
  
    def __calculate_cost_function(self):
        '''
        returns the cost function
        '''
        training_count = len(self.__training_data)
        sum_a0 = 0.0
        sum_a1 = 0.0
        sum_cost = 0.0
        cost = 0.0

        for idx in range(0, training_count):
            y_value = self.__training_data[idx][1]
            x_value = self.__training_data[idx][0]

            y_hat = self.__calculate_hypothesis(x_value)

            sum_a0 += (y_hat - y_value)
            sum_a1 += ((y_hat - y_value) * x_value)
            sum_cost += pow((y_hat - y_value), 2)

        self.__a0 -= ((self.__alpha * sum_a0) / training_count)
        self.__a1 -= ((self.__alpha * sum_a1) / training_count)
        cost = ((1 / (2 * training_count)) * sum_cost)

        return cost

    def __calculate_hypothesis(self, x_value):
        '''
        calculates the hypothesis for a value of x
        '''
        hypothesis = self.__a0 + (self.__a1 * x_value)
        return hypothesis

    def print_hypothesis(self):
        '''
        prints the hypothesis equation
        '''
        print(f'y = {self.__a0} x + {self.__a1}')


if __name__ == '__main__':
    gradient_descent = UnivariateGradientDescent(0.00005)
    gradient_descent.train('data.csv')
    gradient_descent.print_hypothesis()