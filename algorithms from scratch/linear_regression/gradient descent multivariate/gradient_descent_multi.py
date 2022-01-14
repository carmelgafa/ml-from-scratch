
import os
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
import pandas as pd
import sys

class MultivariateGradientDescent:
    '''
    Gradient Descent Univariate utilizing pandas
    '''

    def __init__(self, alpha):
        self.__a0 = 5
        self.__a1 = 3
        self.__a2 = 1
        self.__training_data = None
        
        self.__alpha = alpha
        self.__threshold_iterations = 100000


    def __load_training_data(self, file):
        full_filename = os.path.join(os.path.dirname(__file__), file)
        self.__training_data = pd.read_csv(full_filename, delimiter=',', header=0, index_col=False)
        print(self.__training_data)

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
        m = len(self.__training_data)
        iterations = 0

        previous_cost = sys.float_info.max
        
        costs = []
        a_1s = []
        
        while True:
            # calculate the hypothesis function for all training data
            self.__training_data['y_hat'] = self.__a0 + (self.__a1 * self.__training_data['x1']) + (self.__a2 * self.__training_data['x2'])
                        
            # calculate the difference between the hypothesis function and the
            # actual y value for all training data
            self.__training_data['y_hat-y'] = self.__training_data['y_hat'] - self.__training_data['y']
            
            # multiply the difference by the x value for all training data
            self.__training_data['y-hat-y.x1'] = self.__training_data['y_hat-y'] * self.__training_data['x1']
            self.__training_data['y-hat-y.x2'] = self.__training_data['y_hat-y'] * self.__training_data['x2']
            
            # square the difference for all training data
            self.__training_data['y-hat-y_sq'] = self.__training_data['y_hat-y'] ** 2
            
            # update the a0 and a1 values
            self.__a0 -= (self.__alpha * (1/m) * sum(self.__training_data['y_hat-y']))
            self.__a1 -= (self.__alpha * (1/m) * sum(self.__training_data['y-hat-y.x1']))
            self.__a2 -= (self.__alpha * (1/m) * sum(self.__training_data['y-hat-y.x2']))
            
            # calculate the cost function
            cost = sum(self.__training_data['y-hat-y_sq']) / (2 * m)
            iterations += 1

            # record the cost and a1 values for plotting
            costs.append(cost)
            a_1s.append(self.__a1)
            
            cost_difference = previous_cost - cost
            print(f'Iteration: {iterations}, cost: {cost:.3f}, difference: {cost_difference:.6f}')
            previous_cost = cost

            # check if the cost function is diverging, if so, break
            if cost_difference < 0:
                print(f'Cost function is diverging. Stopping training.')
                break
            
            # check if the cost function is close enough to 0, if so, break or if the number of 
            # iterations is greater than the threshold, break
            if abs(cost_difference) < 0.0001 or iterations > self.__threshold_iterations:
                break

        # # plot the cost function and a1 values
        # plt.plot(a_1s[:], costs[:], '--bx', color='lightblue', mec='red')
        # plt.xlabel('a1')
        # plt.ylabel('cost')
        # plt.title(r'Cost Function vs. a1, with $\alpha$ =' + str(self.__alpha))
        # plt.show()

    def print_hypothesis(self):
        '''
        prints the hypothesis equation
        '''
        print(f'y = {self.__a0} + {self.__a1}x1 + {self.__a2}x2')


if __name__ == '__main__':
    gradient_descent = MultivariateGradientDescent(0.001)
    gradient_descent.train('data.csv')
    gradient_descent.print_hypothesis()