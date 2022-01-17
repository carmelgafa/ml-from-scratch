
import os
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np

class MultivariateGradientDescent:
    '''
    Gradient Descent Univariate utilizing pandas
    '''

    def __init__(self, alpha):
        self.__X = None
        self.__y = None
        self.__Beta = None
        
        self.__alpha = alpha
        self.__threshold_iterations = 100000


    def __load_training_data(self, file):
        full_filename = os.path.join(os.path.dirname(__file__), file)
        training_data = pd.read_csv(full_filename, delimiter=',', header=0, index_col=False)

        self.__y = training_data['y'].to_numpy()
        
        self.__m = len(self.__y)

        self.__X = training_data.drop(['y'], axis=1).to_numpy()
        
        # add a column of ones to the X matrix to account for the intercept, a0
        self.__X = np.insert(self.__X, 0, 1, axis=1)
        print(self.__X)
        
        self.y_hat = np.zeros(len(self.__y))
        
        # beta will hold the values of the coefficients, hence it will be  the size 
        # of a row of the X matrix
        # self.__Beta = np.random.random(len(self.__X[0]))
        self.__Beta = np.array([5.0, 3.0, 1.0])

        self.__deltas = np.zeros(len(self.__X[0]))


        # self.__diffyx = self.__X.copy()
        # self.__Beta = np.random.rand(self.__X.shape[1]+1)
        
        # print(self.__X)
        # print(self.__y)
        # print(self.__Beta)




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
        # m = len(self.__training_data)
        iterations = 0

        previous_cost = sys.float_info.max
        
        costs = []
        a_2s = []
        
        while True:
            # calculate the hypothesis function for all training data
            self.__y_hat = np.dot(self.__Beta, self.__X.T)

            #  calculate the difference between the hypothesis and the actual y values
            diff = self.__y_hat - self.__y

            # calculate the value of (y_hat - y).x, call it deltas
            self.__deltas = np.dot(diff, self.__X)
            
            # calculate the new value of beta
            self.__Beta -= (self.__alpha/self.__m) * self.__deltas

            # calculate the cost function
            cost = np.dot(diff, diff)/(2 * self.__m)

            # increase the number of iterations
            iterations += 1

        #     # record the cost and a1 values for plotting
            costs.append(cost)
            a_2s.append(self.__Beta[2])
            
            cost_difference = previous_cost - cost
            print(f'Iteration: {iterations}, cost: {cost:.3f}, beta: {self.__Beta}')
            previous_cost = cost

            # check if the cost function is diverging, if so, break
            if cost_difference < 0:
                print(f'Cost function is diverging. Stopping training.')
                break
            
            # check if the cost function is close enough to 0, if so, break or if the number of 
            # iterations is greater than the threshold, break
            if abs(cost_difference) < 0.0001 or iterations > self.__threshold_iterations:
                break

        # plot the cost function and a1 values
        plt.plot(a_2s[:], costs[:], '--bx', color='lightblue', mec='red')
        plt.xlabel('a2')
        plt.ylabel('cost')
        plt.title(r'Cost Function vs. a1, with $\alpha$ =' + str(self.__alpha))
        plt.show()



if __name__ == '__main__':
    gradient_descent = MultivariateGradientDescent(0.0001)
    gradient_descent.train('data.csv')
