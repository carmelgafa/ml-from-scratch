from fuzzy_system.fuzzy_learning_helper import load_weather
from fuzzy_system.fuzzy_learning_helper import load_linear_model
from fuzzy_system.fuzzy_learning_helper import split_train_test
from fuzzy_system.fuzzy_learning_system import FuzzyLearningSystem
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing
import os


DATA_PATH = os.path.join(os.path.dirname( __file__ ), 'data')

def load_data(filename, data_path=DATA_PATH, separator=','):
	csv_path = os.path.join(data_path, filename)
	return pd.read_csv(csv_path, sep=separator)


if __name__ == "__main__":

    df = load_data ('weatherHistory_adj.csv')


    # param = 'Temperature'
    param = 'Humidity'

    res = df.groupby(pd.Grouper(key='Month'))[param].agg([np.min, np.mean, np.max])
    res = res.sort_values(by=['Month'])
    print(res)


    error = [(res['amax']-res['mean']), (res['mean']-res['amin'])]

    res.plot(kind = "barh", y = "mean", legend = False, title = param, xerr=error)
    plt.show()





