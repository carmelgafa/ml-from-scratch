from fuzzy_system.fuzzy_learning_helper import load_sensor_data
from fuzzy_system.fuzzy_learning_system import FuzzyLearningSystem
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

X, y = load_sensor_data()

clean_y = y.copy() 
clean_y['Y'] = 1.1**X['x']

X_train = X
X_test = X
y_train = y
y_test = y

learning_system = FuzzyLearningSystem(res=1000)

learning_system.fit(X_train, y_train, X_n=5, y_n=2)

score = learning_system.score(X_test, clean_y)
print(score)

df = pd.DataFrame()

for i in np.arange(0,50,1):

    y_hat = learning_system.get_result({'x':i})['Y']

    a_row = pd.Series([i, y_hat])
    row_df = pd.DataFrame([a_row])
    df = pd.concat([row_df, df])

plt.plot(X, y)
plt.plot(df[0], df[1])

print(learning_system)

