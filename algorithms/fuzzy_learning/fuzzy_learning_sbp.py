from fuzzy_system.fuzzy_learning_helper import load_winequality_red
from fuzzy_system.fuzzy_learning_helper import load_linear_model
from fuzzy_system.fuzzy_learning_helper import split_train_test
from fuzzy_system.fuzzy_learning_helper import load_sbp
from fuzzy_system.fuzzy_learning_system import FuzzyLearningSystem
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
import pandas as pd

X, y = load_sbp()
# # X, y = load_linear_model()

# min_max_scaler = preprocessing.StandardScaler()

# x = X.values #returns a numpy array
# x_scaled = min_max_scaler.fit_transform(x)
# X = pd.DataFrame(x_scaled)

# print(X.min(), X.max())


# X_train, X_test, y_train, y_test = split_train_test(X, y, test_size = 0.10)
X_train = X
X_test = X
y_train = y
y_test = y

learning_system = FuzzyLearningSystem(res=1000)

learning_system.fit(X_train, y_train, X_n=3, y_n=4)

# learning_system.plot_variables()


print(learning_system)

score = learning_system.score(X_test, y_test)
print(score)

df = pd.DataFrame()

for i in np.arange(54,79,0.5):

    y_hat = learning_system.get_result({'Age':i})['SBP']

    a_row = pd.Series([i, y_hat])
    row_df = pd.DataFrame([a_row])
    df = pd.concat([row_df, df])


plt.scatter(X, y)
plt.scatter(df[0], df[1])
plt.show()

