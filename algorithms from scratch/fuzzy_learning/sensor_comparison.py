from fuzzy_system.fuzzy_learning_helper import split_train_test
from fuzzy_system.fuzzy_learning_helper import load_sensor_data
from fuzzy_system.fuzzy_learning_system import FuzzyLearningSystem
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
import pandas as pd

X, y = load_sensor_data()


clean_y = y.copy() 
clean_y['Y'] = 1.1**X['x']


X_train = X
X_test = X
y_train = y
y_test = y



fig, axes = plt.subplots(nrows=3, ncols=3)

df = pd.DataFrame()


for x_range in range(3, 6):
    for y_range in range(2, 5):

        learning_system = FuzzyLearningSystem(res=1000)

        learning_system.fit(X_train, y_train, X_n=x_range, y_n=y_range)

        # learning_system.plot_variables()
        # print(learning_system)

        score = learning_system.score(X_test, clean_y)


        df = df[0:0]



        for i in np.arange(0,50,1):

            y_hat = learning_system.get_result({'x':i})['Y']

            a_row = pd.Series([i, y_hat])
            row_df = pd.DataFrame([a_row])
            df = pd.concat([row_df, df])

        axes[x_range-3, y_range-2].plot(X, clean_y)
        # axes[x_range-1, y_range-1].plot(X, y)
        axes[x_range-3, y_range-2].plot(df[0], df[1])
        axes[x_range-3, y_range-2].set_title(f'sets x: {1+(2*x_range)}, sets y:{1+(2*y_range)}, R-Squared:{score:1.3f}')
        axes[x_range-3, y_range-2].set_xlabel('')


plt.show()

