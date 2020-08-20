from fuzzy_system.fuzzy_rule import FuzzyRule
from fuzzy_system.fuzzy_clause import FuzzyClause
from fuzzy_system.type1_fuzzy_variable import Type1FuzzyVariable
from fuzzy_system.type1_fuzzy_set import Type1FuzzySet
from fuzzy_system.fuzzy_associative_memory import FuzzyAssociativeMemory

import matplotlib.pyplot as plt
from matplotlib import rc
from type2fuzzy import cog_defuzzify
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
								{variable_name: Type1FuzzySet, ...}
		'''
		self._input_variables = {}
		self._output_variables = {}
		self._rules = []
		self._output_distributions = {}

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
		variable -- Type1FuzzyVariable, the input variable
		'''
		self._input_variables[variable.name] = variable

	def add_output_variable(self, variable):
		'''
		adds an output variable to the system.
		note that outputs will also have an entry in the output
		distributions dict

		Arguments:
		----------
		variable -- Type1FuzzyVariable, the output variable
		'''
		self._output_variables[variable.name] = variable
		self._output_distributions[variable.name] = Type1FuzzySet()

	def get_input_variable(self, name):
		'''
		get an input variable given the name

		Arguments:
		-----------
		name -- str, name of variable

		Returns:
		--------
		variable -- Type1FuzzyVariable, the input variable
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
		variable -- Type1FuzzyVariable, the output variable
		'''

		return self._output_variables[name]

	def _clear_output_distributions(self):
		'''
		used for each iteration. The fuzzy result is cleared
		'''
		for variable_name , output_distribution in self._output_distributions.items():
			output_distribution.clear_set()

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
			new_rule.add_antecedent_clause(FuzzyClause(var, f_set))

		for var_name, set_name in consequent_clauses.items():
			var = self.get_output_variable(var_name)
			f_set = var.get_set(set_name)
			new_rule.add_consequent_clause(FuzzyClause(var, f_set))

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
			self._input_variables[input_name].fuzzify_variable(input_value)

		# evaluate rules
		# each rule will return a set of consequences, for each
		# output variable
		for rule in self._rules:
			rule_consequences = rule.evaluate()

			# combine each consequence to obtain an output distribution for each
			# output variable
			for output_var_name, rule_consequence in rule_consequences.items():
				self._output_distributions[output_var_name] = self._output_distributions[output_var_name].union(rule_consequence)

		# finally, defuzzify all output distributions to get the crisp outputs
		output = {}
		for output_var_name, output_distribution in self._output_distributions.items():
			
			fig, ax = plt.subplots(1,1)

			output_distribution.plot_set(ax)

			plt.show()

			output[output_var_name] = output_distribution.cog_defuzzify()

		return output

	def create_fam(self, output):
		'''
		creates a fuzzy associative memory for a given output
		variable.
		'''

		variable_info = {}
		fam_shape = []

		for variable_name, variable in self._input_variables.items():

			sets_names = variable.get_sets_names()
			variable_info[variable_name] = sets_names
			fam_shape.append(len(sets_names))

		fam = FuzzyAssociativeMemory(variable_info, fam_shape)

		for rule in self._rules:
			# ante = rule.antecedent_clauses
			# cons = rule.consequent_clauses[output]

			# fam.set_entity(ante, cons)
			pass

		return fam


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