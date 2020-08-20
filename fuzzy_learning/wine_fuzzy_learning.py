from fuzzy_system.fuzzy_learning_helper import load_winequality_red
from fuzzy_system.fuzzy_learning_helper import load_linear_model
from fuzzy_system.fuzzy_learning_helper import split_train_test
from fuzzy_system.fuzzy_learning_system import FuzzyLearningSystem
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing


def execute_test(resolution, x_n, y_n):

    X, y = load_winequality_red()

    s = 'chlorides'
    c = X[s]
    c_log = np.log(c)
    c_log[c_log < -3.5] = -3.5
    c_log[c_log > -1.5] = -1.5
    X[s] = c_log

    s='residual sugar'
    c = X[s]
    c_log = np.log(c)
    c_log[c_log > 2] = 2
    X[s] = c_log

    s = 'sulphates'
    c = X[s]
    c[c > 1.25] = 1.25
    X[s] = c

    s = 'total sulfur dioxide'
    c = X[s]
    c_log = np.log(c)
    X[s] = c_log



    X_train, X_test, y_train, y_test = split_train_test(X, y, test_size = 0.05)
    # X_train = X
    # X_test = X
    # y_train = y
    # y_test = y

    learning_system = FuzzyLearningSystem(res=resolution)

    learning_system.fit(X_train, y_train, X_n=x_n, y_n=y_n)

    score = learning_system.score(X_test, y_test)

    return score


size = 10
results = np.zeros((size,size))
init_val = 11
for x in range (init_val,init_val+size):
    for y in range (init_val,init_val+size):

      results [x-init_val,y-init_val] =  execute_test(1000, x, y)

#results.tofile('results.standardscaler.csv', sep=',')
print(results)