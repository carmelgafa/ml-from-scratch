'''
Fuzzy Clause class. Used in Fuzzy rule
'''
class FuzzyClause():
	'''
	A fuzzy clause of the type 'variable is set'
	used in fuzzy IF ... THEN ... rules
	clauses can be antecedent (if part) or consequent 
	(then part)
	'''

	def __init__(self, variable, f_set, degree=1):
		'''
		initialization of the fuzzy clause

		Arguments:
		----------
		variable -- the clause variable in 'variable is set'
		set -- the clause set in 'variable is set'
		'''

		if f_set is None:
			raise Exception('set none')

		if f_set.name == '':
			raise Exception(str(f_set), 'no set name')


		self._variable = variable
		self._set = f_set

	def __str__(self):
		'''
		string representation of the clause.

		Returns:
		--------
		str: str, string representation of the clause in the form
					A is x
		'''
		return f'{self._variable.name} is {self._set.name}'

	@property
	def variable_name(self):
		'''
		returns the name of the clause variable

		Returns:
		--------
		variable_name: str, name of variable
		'''
		return self._variable.name

	@property
	def set_name(self):
		'''
		returns the name of the clause variable

		Returns:
		--------
		variable_name: str, name of variable
		'''
		return self._set.name

	def evaluate_antecedent(self):
		'''
		Used when set is antecedent.
		returns the set degree of membership.

		Returns:
		--------
		dom -- number, the set degree of membership given a value for
				that variable. This value is determined at an earlier stage
				and stored in the set
		'''
		return self._set.last_dom_value

	def evaluate_consequent(self, dom):
		'''
		Used when clause is consequent.

		Arguments:
		-----------
		dom -- number, scalar value from the antecedent clauses

		Returns:
		--------
		set -- Type1FuzzySet, a set resulting from min operation with
				the scalar value
		'''
		self._variable.add_rule_contribution(self._set.min_scalar(dom))