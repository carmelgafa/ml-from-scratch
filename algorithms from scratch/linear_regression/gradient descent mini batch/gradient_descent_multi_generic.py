
import os
import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
import pandas as pd
import sys
import numpy as np

class MultivariateGradientDescent:
    '''
    Generic Gradient Descent Univariate utilizing pandas
    Assumption that the name of the label is 'y'
    '''

    def __init__(self, alpha=0.0003, threshold_iterations=100000, costdifference_threshold=0.000000001):
        '''
        Initializes the class
        '''
        self.__alpha = alpha
        self.__threshold_iterations = threshold_iterations
        self.__costdifference_threshold = costdifference_threshold
        self.__X = None
        self.__Y = None
        self.__beta = None

    def __load_training_data(self, file):
        full_filename = os.path.join(os.path.dirname(__file__), file)
        training_data = pd.read_csv(full_filename, delimiter=',', header=0, index_col=False)

        training_data = training_data.sample(frac=1).reset_index(drop=True)


        self.__Y = training_data['y'].to_numpy()
        
        self.__m = len(self.__Y)

        self.__X = training_data.drop(['y'], axis=1).to_numpy()
        
        # add a column of ones to the X matrix to account for the intercept, a0
        self.__X = np.insert(self.__X, 0, 1, axis=1)
        print(self.__X)
        
        self.y_hat = np.zeros(len(self.__Y))
        
        # beta will hold the values of the coefficients, hence it will be  the size 
        # of a row of the X matrix
        self.__beta = np.random.random(len(self.__X[0]))

        self.__minibatches_number = 2
        
        self.__minibatch_size = int(self.__m/self.__minibatches_number)

    def train(self, file):
        '''
        starts the training procedure
        '''
        self.__load_training_data(file)

        iterations = 0

        # initialize the previous cost function value to a large number
        # previous_cost = sys.float_info.max
        
        # store the cost function and a2 values for plotting
        costs = []
        a_2s = []
        
        previous_cumulative_cost = sys.float_info.max
        
        while True:
            
            # print(f'Epoch: {iterations}')

            cumulative_cost = 0

            for i in range(self.__minibatches_number):

                # print(f'Minibatch: {i}')
                
                minibatch_X = self.__X[i*self.__minibatch_size:(i+1)*self.__minibatch_size]
                minibatch_Y = self.__Y[i*self.__minibatch_size:(i+1)*self.__minibatch_size]

                # print(f'Minibatch X: {minibatch_X.shape}, minimatch Y: {minibatch_Y.shape}, minibatch beta: {minibatch_beta.shape}')


                # calculate the hypothesis function for all training data
                y_hat = np.dot( self.__beta, minibatch_X.T)

                #  calculate the residuals
                residuals = y_hat - minibatch_Y
                
                # calculate the new value of beta
                self.__beta -= (
                    self.__alpha / self.__minibatch_size)  * np.dot(
                        residuals, minibatch_X)

                # calculate the cost function
                cost = np.dot(residuals, residuals) / ( 2 * self.__minibatch_size)

                cumulative_cost += cost

            # increase the number of iterations
            iterations += 1


            # record the cost and a1 values for plotting
            #     costs.append(cost)
            #     a_2s.append(self.__beta[2])

            cost_difference = previous_cumulative_cost - cumulative_cost
            print(f'Epoch: {iterations}, average cost: {(cumulative_cost/self.__minibatches_number):.3f}, beta: {self.__beta}')
            previous_cumulative_cost = cumulative_cost

            # check if the cost function is diverging, if so, break
            if cost_difference < 0:
                print(f'Cost function is diverging. Stopping training.')
                break
                
            # check if the cost function is close enough to 0, if so, break or if the number of 
            # iterations is greater than the threshold, break
            if abs(cost_difference) < self.__costdifference_threshold or iterations > self.__threshold_iterations:
                break

        # # plot the cost function and a1 values
        # plt.plot(a_2s[3:], costs[3:], '--bx', color='lightblue', mec='red')
        # plt.xlabel('a2')
        # plt.ylabel('cost')
        # plt.title(r'Cost Function vs. a1, with $\alpha$ =' + str(self.__alpha))
        # plt.show()

if __name__ == '__main__':
    gradient_descent = MultivariateGradientDescent()
    gradient_descent.train('data.csv')
