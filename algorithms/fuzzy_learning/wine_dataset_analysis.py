import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

DATA_PATH = os.path.join(os.path.dirname( __file__ ), 'data')


def load_data(filename, data_path=DATA_PATH, separator=';'):
	csv_path = os.path.join(data_path, filename)
	return pd.read_csv(csv_path, sep=separator)

def save_data(data_frame, filename, data_path=DATA_PATH):
	csv_path = os.path.join(data_path, filename)
	return data_frame.to_csv(csv_path, float_format='%.3f', index=False)

def inspect_data(data):
	# print first 10 rows
	print(data.head())
	# print datatypes
	print(data.info())
	# print min, max, mean, std  dev and percentiles
	print(data.describe())
	# plot histogram
	data.hist(bins=50)
	plt.show()

def _split_train_test(data, test_ratio, random_seed=42):
	np.random.seed(random_seed)

	shuffled_indices = np.random.permutation(len(data))
	test_set_size = int(len(data) * test_ratio)
	test_indices = shuffled_indices[:test_set_size]
	train_indices = shuffled_indices[test_set_size:]
	return data.iloc[train_indices], data.iloc[test_indices]

def split_data(data):
	train_set, test_set = _split_train_test(data, 0.2)
	save_data(train_set, 'winequality-red_train.csv')
	save_data(test_set, 'winequality-red_test.csv')
	print(f'data count: {len(data)}')
	print(f'train set count: {len(train_set)}')
	print(f'test set count: {len(test_set)}')

def visualize(data):
	data.plot(kind='scatter', x='alcohol', y='citric acid', label='pH', figsize=(10,7), alpha=0.1, s=data['total sulfur dioxide'], c='quality',
	cmap=plt.get_cmap('jet'), colorbar=True)
	plt.show()

if __name__ == "__main__":
	from sklearn import preprocessing

	data = load_data('winequality-red.csv')

	# Get column names first
	names = data.columns
	# Create the Scaler object
	scaler = preprocessing.MinMaxScaler()
	# Fit your data on the scaler object
	scaled_df = scaler.fit_transform(data)
	scaled_df = pd.DataFrame(scaled_df, columns=names)

	inspect_data(scaled_df)
	# split_data(data)
	# visualize(dataNorm)