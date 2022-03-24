from fuzzy_system.fuzzy_learning_helper import load_sample_set
from fuzzy_system.fuzzy_learning_system import FuzzyLearningSystem
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

def generate_sample_data():
	random.seed(42)
	df = pd.DataFrame()
	r = random.uniform(-1,1)
	print(r)


def test_model():
	X, y = load_sample_set()

	# X_train, X_test, y_train, y_test = split_train_test(X, y, test_size = 0.10)
	X_train = X
	X_test = X
	y_train = y
	y_test = y

	learning_system = FuzzyLearningSystem(res=1000)

	learning_system.fit(X_train, y_train, X_n=4, y_n=2)
	print(learning_system)

	score = learning_system.score(X_test, y_test)
	print(score)

	df = pd.DataFrame()

	for i in np.arange(0,11,0.5):

		y_hat = learning_system.get_result({'X':i})['y']

		a_row = pd.Series([i, y_hat])
		row_df = pd.DataFrame([a_row])
		df = pd.concat([row_df, df])


	plt.scatter(X, y)
	plt.scatter(df[0], df[1])
	plt.show()

if __name__ == "__main__":
	generate_sample_data()