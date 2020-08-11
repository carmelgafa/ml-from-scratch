from .fuzzy_clause import FuzzyClause

class FuzzyRule():
	'''
	A fuzzy rule of the type
	IF [antecedent clauses] THEN [consequent clauses]
	'''

	def __init__(self):
		'''
		initializes the rule. Two data structures are necessary:
			Antecedent clauses list
			consequent clauses list
		'''
		self._antecedent = []
		self._consequent = []

	def __str__(self):
		'''
		string representation of the rule.

		Returns:
		--------
		str: str, string representation of the rule in the form
					IF [antecedent clauses] THEN [consequent clauses]
		'''
		ante = ' and '.join(map(str, self._antecedent))
		cons = ' and '.join(map(str, self._consequent))
		return f'If {ante} then {cons}'

	def add_antecedent_clause(self, var, f_set):
		'''
		adds an antecedent clause to the rule

		Arguments:
		-----------
			clause -- FuzzyClause, the antecedent clause
		'''
		self._antecedent.append(FuzzyClause(var, f_set))

	def add_consequent_clause(self, var, f_set):
		'''
		adds an consequent clause to the rule

		Arguments:
		-----------
			clause -- FuzzyClause, the consequent clause
		'''
		self._consequent.append(FuzzyClause(var, f_set))

	def evaluate(self):
		'''
		evaluation of the rule.
		the antecedent clauses are executed and the minimum degree of
		membership is retained.
		This is used in teh consequent clauses to min with the consequent
		set
		The values are returned in a dict of the form {variable_name: scalar min set, ...}

		Returns:
		--------
		rule_consequence -- dict, the resulting sets in the form
							{variable_name: scalar min set, ...}
		'''
		# rule dom initialize to 1 as min operator will be performed
		rule_strength = 1

		# execute all antecedent clauses, keeping the minimum of the
		# returned doms to determine the rule strength
		for ante_clause in self._antecedent:
			rule_strength = min(ante_clause.evaluate_antecedent(), rule_strength)

		# execute consequent clauses, each output variable will update its output_distribution set
		for consequent_clause in self._consequent:
			consequent_clause.evaluate_consequent(rule_strength)

	def evaluate_info(self):
		'''
		evaluation of the rule.
		the antecedent clauses are executed and the minimum degree of
		membership is retained.
		This is used in teh consequent clauses to min with the consequent
		set
		The values are returned in a dict of the form {variable_name: scalar min set, ...}

		Returns:
		--------
		rule_consequence -- dict, the resulting sets in the form
							{variable_name: scalar min set, ...}
		'''
		# rule dom initialize to 1 as min operator will be performed
		rule_strength = 1

		
		# execute all antecedent clauses, keeping the minimum of the
		# returned doms to determine the rule strength
		for ante_clause in self._antecedent:
			rule_strength = min(ante_clause.evaluate_antecedent(), rule_strength)

		# execute consequent clauses, each output variable will update its output_distribution set
		for consequent_clause in self._consequent:
			consequent_clause.evaluate_consequent(rule_strength)

		return f'{rule_strength} : {self}'