import pandas as pd
from pandas import DataFrame
import numpy as np

from fuzzy_system.fuzzy_system import FuzzySystem
from fuzzy_system.type1_fuzzy_variable import Type1FuzzyVariable
from fuzzy_system.fuzzy_rule import FuzzyRule
from fuzzy_system.fuzzy_clause import FuzzyClause


class FuzzyLearningSystem(FuzzySystem):

	def __init__(self, res=10):
		self._learned_rules = {}
		super().__init__()
		self._rule_result = {}
		self._cumulative_result = {}
		self._resolution = res

	def __str__(self):

		ret_str = 'Input: \n'
		for n, s in self._input_variables.items():
			ret_str = ret_str + f'{n}: ({s})\n'

		ret_str = ret_str + 'Output: \n'
		for n, s in self._output_variables.items():
			ret_str = ret_str + f'{n}: ({s})\n'

		ret_str = ret_str + 'Rules: \n'
		for _, rule in self._learned_rules.items():
			ret_str = ret_str + f'{rule}\n'

		return ret_str

	def _create_fuzzy_system(self, X_info, y_info, X_n, y_n):

		n_input = X_n
		n_output = y_n

		for idx, row in X_info.iterrows():
			# print(f"creating input variable {row['min_value']},	{row['max_value']},	{self._resolution},	{row['variable_name']}")

			var = Type1FuzzyVariable(row['min_value'],
										row['max_value'],
										self._resolution,
										row['variable_name'])
			
			# var.generate_sets_mean(n_input, row['mean_value'])
			var.generate_sets(n_input)

			self.add_input_variable(var)

		for idx, row in y_info.iterrows():
			var = Type1FuzzyVariable(row['min_value'],
										row['max_value'],
										self._resolution,
										row['variable_name'])
			
			# var.generate_sets_mean(n_output, row['mean_value'])
			var.generate_sets(n_output)

			self.add_output_variable(var)
			self._rule_result[row['variable_name']] = [0,0]
			self._cumulative_result[row['variable_name']] = [0,0]


	def _create_rule (self, X_row, y_row):
	
		new_rule = FuzzyRule()
		
		for (input_variable_name, input_variable_value) in X_row.iteritems():
			
			input_variable = self.get_input_variable(input_variable_name)

			f_set, dom = input_variable.get_set_greater_dom(input_variable_value)

			clause = FuzzyClause(input_variable, f_set, dom)
			
			new_rule.add_antecedent_clause(clause)


		for (output_variable_name, output_variable_value) in y_row.iteritems():
			
			output_variable = self.get_output_variable(output_variable_name)
			
			f_set, dom = output_variable.get_set_greater_dom(output_variable_value)

			clause = FuzzyClause(output_variable, f_set, dom)
			
			new_rule.add_consequent_clause(clause)

		if new_rule.get_antecedent_str() in self._learned_rules:
			if new_rule.degree > self._learned_rules[new_rule.get_antecedent_str()].degree:
				self._learned_rules[new_rule.get_antecedent_str()] = new_rule
		else:
			self._learned_rules[new_rule.get_antecedent_str()] = new_rule


	def fit(self, X_train, y_train, X_n=3, y_n=3):
		X_info = DataFrame({'variable_name':X_train.columns.values,
										'min_value':X_train.min(),
										'max_value':X_train.max(),
										'mean_value':X_train.mean()})

		y_info = DataFrame({'variable_name':y_train.columns.values,
										'min_value':y_train.min(),
										'max_value':y_train.max(),
										'mean_value':y_train.mean()})

		self._create_fuzzy_system(X_info, y_info, X_n, y_n)

		for idx in X_train.index:
			self._create_rule(X_train.loc[idx, :], y_train.loc[idx, :])
	

	def analyse_rules(self):
		
		antecedents = []
		consequents = []

		for rule_str, rule in self._learned_rules.items():
			antecedents.append(rule.get_antecedent_list())
			consequents.append(rule.get_consequent_list())
			
			# print(rule.get_antecedent_list(), rule.get_consequent_list())

		test_ante = antecedents[0]

		a = np.array(list(map(int, antecedents[0])))

		for i in range(1, len(antecedents)):
			# print(i, list(set(test_ante) - set(antecedents[i])))
			
			b = np.array(list(map(int, antecedents[i])))

			diff = np.abs(a - b)
			diff_count = np.count_nonzero(diff)
			


			if (diff_count < 5) :
				print(i, diff, consequents[0], consequents[i])
		# print(antecedents[1226])
		# print( list(set(list(map(int, antecedents[0]))) - set(list(map(int, antecedents[1226])))) )


		print(antecedents[0])
		print(antecedents[833])


	def get_result(self, X):

		for X_name, X_val in X.items():
			self._input_variables[X_name].fuzzify_variable(X_val)

		rules_result = {}

		for _, rule in self._learned_rules.items():

			degree_output_control, outputs_center = rule.evaluate_score()
			
			if degree_output_control > 0:

				for y_name, center_value in outputs_center.items():

					if y_name not in rules_result:
						rules_result[y_name] = [0, 0]

					rules_result[y_name][0] = rules_result[y_name][0] + (center_value * degree_output_control)
					rules_result[y_name][1] = rules_result[y_name][1] + (degree_output_control)

		# rules_result will be adapted to contain the result
		for y_name, result in rules_result.items():
			rules_result[y_name] = result[0] / result[1]

		return rules_result



	def score(self, X_test, y_test):
		'''

		Arguments:
		-----------

		Returns:
		--------
		'''

		y_hat = y_test.copy()
		y_hat.loc[:] = 0

		no_rules_fired = 0

		for idx in X_test.index:
			ret = self.get_result(X_test.loc[idx].to_dict())

			if len(ret) == 0:
				no_rules_fired = no_rules_fired + 1
				
				for name in y_test.columns.values:
					y_hat.loc[idx, name] = y_test[name].mean()
			else:
				for name, value in ret.items():
					y_hat.loc[idx, name] = value


		# print('no rules fired: ', no_rules_fired)

		for y_name in y_test.columns.values:

			y_mean = y_test[y_name].mean()

			sum_square_total = (pow(y_test[y_name] - y_mean, 2)).sum()
			# print(sum_square_total)


			sum_square_residual = (pow(y_test[y_name] - y_hat[y_name], 2)).sum()

			r_squared = 1 - (sum_square_residual / sum_square_total)

			# print(f'{y_name} : {r_squared}')

			return r_squared


	def plot_variables(self):
		
		for _, var in self._input_variables.items():
			var.plot_variable()

		for _, var in self._output_variables.items():
			var.plot_variable()


	def generate_rules_csv(self, file_path):


		
		input_variables = list(self._input_variables.keys())
		output_variables = list(self._output_variables.keys())

		header = input_variables + output_variables

		# drop all data, 1 row all none
		df = pd.DataFrame([[None]*len(header)], columns=header)
		df= df.iloc[0:0]


		for _, rule in self._learned_rules.items():

			line = rule.get_csv_line(header)
			row = pd.DataFrame([line], columns=header)

			df= df.append(row, ignore_index=True)
	
		df.to_csv(file_path)