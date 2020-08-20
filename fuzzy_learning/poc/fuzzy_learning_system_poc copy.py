import pandas as pd
from pandas import DataFrame
import os
import matplotlib.pyplot as plt
import numpy as np

from fuzzy_system.fuzzy_system import FuzzySystem
from fuzzy_system.type1_fuzzy_variable import Type1FuzzyVariable
from fuzzy_system.fuzzy_rule import FuzzyRule
from fuzzy_system.fuzzy_clause import FuzzyClause


DATA_PATH = os.path.join(os.path.dirname( __file__ ), 'data')

def load_data(filename, data_path=DATA_PATH, separator=';'):
	csv_path = os.path.join(data_path, filename)
	return pd.read_csv(csv_path, sep=separator)

def save_data(data_frame, filename, data_path=DATA_PATH):
	csv_path = os.path.join(data_path, filename)
	return data_frame.to_csv(csv_path, float_format='%.3f', index=False)

def _split_train_test(X, y, test_ratio, random_seed=42):
	np.random.seed(random_seed)
	shuffled_indices = np.random.permutation(len(X))
	test_set_size = int(len(data) * test_ratio)

	test_indices = shuffled_indices[:test_set_size]
	train_indices = shuffled_indices[test_set_size:]

	return X.iloc[train_indices], y.iloc[train_indices], X.iloc[test_indices], y.iloc[test_indices]

def split_data(X, y):
	X_train, y_train, X_test, y_test = _split_train_test(X, y, 0.2)
	return X_train, y_train, X_test, y_test

def create_input_output_datasets(data, output_attributes_names):
	'''
	Arguments:
	----------
	data -- original dataset
	output_attributes_names -- list, contains the names of the output attributes
	'''
	input_data = data.loc[:, data.columns != output_attributes_names]
	output_data = data.loc[:, data.columns == output_attributes_names]

	# print(input_data.head())
	# print(output_data.head())

	return input_data, output_data

def create_fuzzy_system(input_data_info, output_data_info, res=100):

	f_system = FuzzySystem()

	for idx, row in input_data_info.iterrows():

		var = Type1FuzzyVariable(row['min_value'],
									row['max_value'],
									res,
									row['variable_name'])
		var.generate_sets(5)
		f_system.add_input_variable(var)

	for idx, row in output_data_info.iterrows():
		var = Type1FuzzyVariable(row['min_value'],
									row['max_value'],
									res,
									row['variable_name'])
		var.generate_sets(5)
		
		f_system.add_output_variable(var)

	return f_system


learned_rules = {}

def build_rule(f_system, input_data_row, output_data_row):
	new_rule = FuzzyRule()
	
	for (input_variable_name, input_variable_value) in input_data_row.iteritems():
		
		input_variable = f_system.get_input_variable(input_variable_name)
		
		f_set, dom = input_variable.get_set_greater_dom(input_variable_value)

		clause = FuzzyClause(input_variable, f_set, dom)
		
		new_rule.add_antecedent_clause(clause)

		# print(clause)

	for (output_variable_name, output_variable_value) in output_data_row.iteritems():
		
		output_variable = f_system.get_output_variable(output_variable_name)
		
		f_set, dom = output_variable.get_set_greater_dom(output_variable_value)

		clause = FuzzyClause(output_variable, f_set, dom)
		
		new_rule.add_consequent_clause(clause)

	if str(new_rule) in learned_rules:
		# print(f'clash in {str(new_rule)}')
		# print(f'{new_rule.degree} vs {learned_rules[str(new_rule)].degree}')

		if new_rule.degree > learned_rules[str(new_rule)].degree:
			learned_rules[str(new_rule)] = new_rule
	else:
		learned_rules[str(new_rule)] = new_rule

if __name__ == "__main__":
	data = load_data('winequality-red.csv')
	
	X, y = create_input_output_datasets(data, 'quality')
	# print(X.shape)


	X_train, y_train, X_test, y_test = split_data(X, y)
	# print(X_train.shape)

	train_input_info = DataFrame({'variable_name':X_train.columns.values,
									'min_value':X_train.min(),
									'max_value':X_train.max()})

	train_output_info = DataFrame({'variable_name':y_train.columns.values,
									'min_value':y_train.min(),
									'max_value':y_train.max()})

	f_system = create_fuzzy_system(train_input_info, train_output_info)

	for idx in X_train.index:
		build_rule(f_system, X_train.loc[idx, :], y_train.loc[idx, :])


	# print(len(learned_rules))

	# test_input, test_output =create_input_output_datasets(test, 'quality')

	# print(test_input.head())

	# for idx in test_input.index:
	# 	build_rule(f_system, train_input.loc[idx, :], train_output.loc[idx, :])
