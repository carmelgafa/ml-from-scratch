from .fuzzy_rule import FuzzyRule
from fuzzy_system.fuzzy_variable_output import FuzzyOutputVariable
from fuzzy_system.fuzzy_variable_input import FuzzyInputVariable

import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np

class FuzzySystem:
	'''
	A type-1 fuzzy system based on Mamdani inference system

	Reference:
	----------
	Mamdani, Ebrahim H., and Sedrak Assilian. 
	"An experiment in linguistic synthesis with a 
	fuzzy logic controller." Readings in Fuzzy Sets 
	for Intelligent Systems. Morgan Kaufmann, 1993. 283-289.
	'''

	def __init__(self):
		'''
		initializes fuzzy system.
		data structures required:
			input variables -- dict, having format {variable_name: FuzzyVariable, ...}
			output variables -- dict, having format {variable_name: FuzzyVariable, ...}
			rules -- list of FuzzyRule
			output_distribution -- dict holding fuzzy output for each variable having format
								{variable_name: FuzzySet, ...}
		'''
		self._input_variables = {}
		self._output_variables = {}
		self._rules = []

	def __str__(self):
		'''
		string representation of the system.

		Returns:
		--------
		str: str, string representation of the system in the form
				Input:
				input_variable_name(set_names)...
				Output:
				output_variable_name(set_names)...
				Rules:
				IF [antecedent clauses] THEN [consequent clauses]
		'''

		ret_str = 'Input: \n'
		for n, s in self._input_variables.items():
			ret_str = ret_str + f'{n}: ({s})\n'

		ret_str = ret_str + 'Output: \n'
		for n, s in self._output_variables.items():
			ret_str = ret_str + f'{n}: ({s})\n'

		ret_str = ret_str + 'Rules: \n'
		for rule in self._rules:
			ret_str = ret_str + f'{rule}\n'

		return ret_str

	def add_input_variable(self, variable):
		'''
		adds an input variable to the system

		Arguments:
		----------
		variable -- FuzzyVariable, the input variable
		'''
		self._input_variables[variable.name] = variable

	def add_output_variable(self, variable):
		self._output_variables[variable.name] = variable


	def get_input_variable(self, name):
		'''
		get an input variable given the name

		Arguments:
		-----------
		name -- str, name of variable

		Returns:
		--------
		variable -- FuzzyVariable, the input variable
		'''
		return self._input_variables[name]

	def get_output_variable(self, name):
		'''
		get an output variable given the name

		Arguments:
		-----------
		name -- str, name of variable

		Returns:
		--------
		variable -- FuzzyVariable, the output variable
		'''

		return self._output_variables[name]

	def _clear_output_distributions(self):
		'''
		used for each iteration. The fuzzy result is cleared
		'''
		map(lambda output_var: output_var.clear_output_distribution(), self._output_variables.values())

	def add_rule(self, antecedent_clauses, consequent_clauses):
		'''
		adds a new rule to the system.
		TODO: add checks

		Arguments:
		-----------
		antecedent_clauses -- dict, having the form {variable_name:set_name, ...}
		consequent_clauses -- dict, having the form {variable_name:set_name, ...}
		'''
		# create a new rule
		# new_rule = FuzzyRule(antecedent_clauses, consequent_clauses)
		new_rule = FuzzyRule()

		for var_name, set_name in antecedent_clauses.items():
			# get variable by name
			var = self.get_input_variable(var_name)
			# get set by name
			f_set = var.get_set(set_name)
			# add clause
			new_rule.add_antecedent_clause(var, f_set)

		for var_name, set_name in consequent_clauses.items():
			var = self.get_output_variable(var_name)
			f_set = var.get_set(set_name)
			new_rule.add_consequent_clause(var, f_set)

		# add the new rule
		self._rules.append(new_rule)

	def evaluate_output(self, input_values):
		'''
		Executes the fuzzy inference system for a set of inputs

		Arguments:
		-----------
		input_values -- dict, containing the inputs to the systems in the form
							{input_variable_name: value, ...}

		Returns:
		--------
		output -- dict, containing the outputs from the systems in the form
					{output_variable_name: value, ...}
		'''
		# clear the fuzzy consequences as we are evaluating a new set of inputs.
		# can be optimized by comparing if the inputs have changes from the previous
		# iteration.
		self._clear_output_distributions()

		# Fuzzify the inputs. The degree of membership will be stored in
		# each set
		for input_name, input_value in input_values.items():
			self._input_variables[input_name].fuzzify(input_value)

		# evaluate rules
		for rule in self._rules:
			rule.evaluate()

		# finally, defuzzify all output distributions to get the crisp outputs
		output = {}
		for output_var_name, output_var in self._output_variables.items():
			output[output_var_name] = output_var.get_crisp_output()

		return output


	def evaluate_output_info(self, input_values):
		'''
		Executes the fuzzy inference system for a set of inputs

		Arguments:
		-----------
		input_values -- dict, containing the inputs to the systems in the form
							{input_variable_name: value, ...}

		Returns:
		--------
		output -- dict, containing the outputs from the systems in the form
					{output_variable_name: value, ...}
		'''
		info = {}
		# clear the fuzzy consequences as we are evaluating a new set of inputs.
		# can be optimized by comparing if the inputs have changes from the previous
		# iteration.
		self._clear_output_distributions()

		# Fuzzify the inputs. The degree of membership will be stored in
		# each set
		fuzzification_info = []
		for input_name, input_value in input_values.items():
			fuzzification_info.append(self._input_variables[input_name].fuzzify_info(input_value))

		info['fuzzification'] = '\n'.join(fuzzification_info)

		# evaluate rules
		rule_info = []
		for rule in self._rules:
			rule_info.append(rule.evaluate_info())

		info['rules'] = '\n'.join(rule_info)


		# finally, defuzzify all output distributions to get the crisp outputs
		output = {}
		for output_var_name, output_var in self._output_variables.items():
			output[output_var_name], info = output_var.get_crisp_output_info()
			# info[output_var_name] = info
		
		return output, info

	def plot_system(self):

		total_var_count = len(self._input_variables) + len(self._output_variables)
		if total_var_count <2:
			total_var_count = 2

		fig, axs = plt.subplots(total_var_count, 1)

		fig.tight_layout(pad=1.0)

		for idx, var_name in enumerate(self._input_variables):
			self._input_variables[var_name].plot_variable(ax=axs[idx], show=False)

		for idx, var_name in enumerate(self._output_variables):
			self._output_variables[var_name].plot_variable(ax=axs[len(self._input_variables)+idx], show=False)

		plt.show()

if __name__ == "__main__":
	pass