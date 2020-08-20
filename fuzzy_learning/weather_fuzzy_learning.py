from fuzzy_system.fuzzy_learning_helper import load_weather
from fuzzy_system.fuzzy_learning_helper import load_linear_model
from fuzzy_system.fuzzy_learning_helper import split_train_test
from fuzzy_system.fuzzy_learning_system import FuzzyLearningSystem
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing


def execute_test(resolution, x_n, y_n):

    X, y = load_weather()

    X_train, X_test, y_train, y_test = split_train_test(X, y, test_size = 0.2)
    # X_train = X
    # X_test = X
    # y_train = y
    # y_test = y

    learning_system = FuzzyLearningSystem(res=resolution)

    learning_system.fit(X_train, y_train, X_n=x_n, y_n=y_n)

    score = learning_system.score(X_test, y_test)

    print(learning_system)

    return score



result = execute_test(1000,4,16)
print(result)


# size = 5
# # results = np.zeros((size,size))
# init_val = 1
# for x in range (init_val,init_val+size):
#     for y in range (init_val,init_val+size):

#         # results [x-init_val,y-init_val] =  execute_test(1000, x, y)
#         result =  execute_test(1000, x, y)

#         print(f'{x-init_val}, {y-init_val} - {result}')

# #results.tofile('results.standardscaler.csv', sep=',')
# print(results)