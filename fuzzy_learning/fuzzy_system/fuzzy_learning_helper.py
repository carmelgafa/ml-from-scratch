import os
import pandas as pd
import numpy as np

DATA_PATH = os.path.join(os.path.dirname( __file__ ), '..\data')

def load_data(filename, data_path=DATA_PATH, separator=';'):
	csv_path = os.path.join(data_path, filename)
	return pd.read_csv(csv_path, sep=separator)

def save_data(data_frame, filename, data_path=DATA_PATH):
	csv_path = os.path.join(data_path, filename)
	return data_frame.to_csv(csv_path, float_format='%.3f', index=False)

def split_train_test(X, y, test_size=0.1, random_seed=21):
	np.random.seed(random_seed)
	shuffled_indices = np.random.permutation(len(X))
	set_size = int(len(X) * test_size)
	
	test_indices = shuffled_indices[:set_size]
	train_indices = shuffled_indices[set_size:]
	
	return X.iloc[train_indices], X.iloc[test_indices], y.iloc[train_indices], y.iloc[test_indices]

def format_dataset(data, output_attributes_names):
	'''
	Arguments:
	----------
	data -- original dataset
	output_attributes_names -- list, contains the names of the output attributes
	'''
	X = data.loc[:, data.columns != output_attributes_names]
	y = data.loc[:, data.columns == output_attributes_names]

	return X, y

def load_winequality_red():
	dataset = load_data('winequality-red.csv')
	# print(dataset.shape)

	return format_dataset(dataset, 'quality')


def load_weather():
	dataset = load_data('weatherHistory_adj.csv', separator=',')
	# print(dataset.shape)

	return format_dataset(dataset, 'Temperature')



def load_linear_model():
	dataset = load_data('linear_model.csv', separator=',')
	# print(dataset.shape)
	return format_dataset(dataset, 'y')

def load_sample_set():
	dataset = load_data('sample_set.csv', separator=',')
	# print(dataset.shape)
	return format_dataset(dataset, 'y')


def load_sbp():
	dataset = load_data('sbp_age.csv', separator=',')
	# print(dataset.shape)
	return format_dataset(dataset, 'SBP')


def load_sensor_data():
	dataset = load_data('sensor_data.csv', separator=',')
	# print(dataset.shape)

	return format_dataset(dataset, 'Y')



if __name__ == "__main__":
	pass