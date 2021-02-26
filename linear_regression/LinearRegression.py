
"""week1 of andrew ng ml course"""
import os
import numpy

class UnivariateLinearRegression:
    """implementation of single variable linear regression"""

    def __init__(self, alpha):
        self.__theta0 = 0.0
        self.__theta1 = 0.0
        self.__training_data = []
        self.__alpha = alpha

    def __load_training_data(self, file):
        """loads training data from file"""
        current_directory = os.path.dirname(__file__)
        full_filename = os.path.join(current_directory, file)
        self.__training_data = numpy.loadtxt(full_filename, delimiter=' ')

    def get_y_value(self, x_value):
        """return an estimated y value given an x value based on the training results"""
        return self.__calculate_hypothesis(x_value)

    def train(self, file):
        """starts the training procedure"""
        self.__load_training_data(file)
        counter = 1
        cost_function = 0
        while True:
            cost_function = self.__calculate_cost_function()
            counter += 1
            if cost_function < 0.3 or counter > 1000:
                break

    def __calculate_cost_function(self):
        """returns the cost function"""
        training_count = len(self.__training_data)
        sum_theta0 = 0.0
        sum_theta1 = 0.0
        sum_costfunction = 0.0
        cost_function = 0.0

        for idx in range(0, training_count):
            y_value = self.__training_data[idx][1]
            x_value = self.__training_data[idx][0]

            h_value = self.__calculate_hypothesis(x_value)

            sum_theta0 += (h_value - y_value)
            sum_theta1 += ((h_value - y_value) * x_value)
            sum_costfunction += pow((h_value - y_value), 2)

        self.__theta0 -= ((self.__alpha * sum_theta0) / training_count)
        self.__theta1 -= ((self.__alpha * sum_theta1) / training_count)
        cost_function = ((1 / (2 * training_count)) * sum_costfunction)

        return cost_function

    def __calculate_hypothesis(self, x_value):
        """calculates the hypothesis for a value of x"""
        hypothesis = self.__theta0 + (self.__theta1 * x_value)
        return hypothesis

    def print_hypothesis(self):
        """prints the hypothesis equation"""
        print('y = {} x + {}'.format(self.__theta0, self.__theta1))
