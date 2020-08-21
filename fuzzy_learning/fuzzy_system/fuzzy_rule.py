class FuzzyRule():
	'''
	A fuzzy rule of the type
	IF [antecedent clauses] THEN [consequent clauses]
	'''

	# def __init__(self, antecedent_clauses, consequent_clauses):
	def __init__(self):
		'''
		initializes the rule. Two data structures are necessary:
			Antecedent clauses list
			consequent clauses list
		'''
		self._antecedent = []
		self._consequent= []
		self._degree = 1

	@property
	def degree(self):
		return self._degree

	def evaluate_score(self):

		output_control = 1

		center_values={}

		for ante in self._antecedent:
			output_control= output_control * ante.evaluate_antecedent()
		
		for cons in self._consequent:
			center_values[cons.variable_name] = cons.get_consequent_center_val()

		return output_control, center_values


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

	def get_antecedent_str(self):
		ante = ' and '.join(map(str, self._antecedent))
		return ante

	def add_antecedent_clause(self, clause):
		'''
		adds an antecedent clause to the rule

		Arguments:
		-----------
			clause -- FuzzyClause, the antecedent clause
		'''
		self._antecedent.append(clause)
		self._degree = self._degree * clause.degree

	def add_consequent_clause(self, clause):
		'''
		adds an consequent clause to the rule

		Arguments:
		-----------
			clause -- FuzzyClause, the consequent clause
		'''
		self._consequent.append(clause)
		self._degree = self._degree * clause.degree

	def evaluate(self):
		'''
		evaluation of the rule.
		the antecedent clauses are executed and the minimum degree of
		membership is retained.
		This is used in teh consequent clauses to alpha cut the consequent
		set
		The values are returned in a dict of the form {variable_name: alpha-cut set, ...}

		Returns:
		--------
		rule_consequence -- dict, the resulting sets in the form
							{variable_name: alpha-cut set, ...}
		'''
		# rule dom initialize to 1 as min operator will be performed
		rule_strength = 1

		# execute all antecedent clauses, keeping the minimum of the
		# returned doms to determine the rule strength
		for ante_clause in self._antecedent:
			rule_strength = min(ante_clause.evaluate_antecedent(), rule_strength)

		# initialize the results dict
		rule_consequence = {}

		# execute consequent clauses, adding each result to the results dict using the
		# variable name as key
		for consequent_clause in self._consequent:
			rule_consequence[consequent_clause.variable_name] = consequent_clause.evaluate_consequent(rule_strength)

		# return results
		return rule_consequence

	def get_antecedent_list(self):
		
		ret = []

		for ante_clause in self._antecedent:
			ret.append(ante_clause.set_name)

		return ret

	def get_consequent_list(self):
		
		ret = []

		for cons_clause in self._consequent:
			ret.append(cons_clause.set_name)

		return ret


	def get_csv_line(self, header):
		
		row = [None] * len(header)

		for ante in self._antecedent:
			idx = header.index(ante.variable_name)
			row[idx] = ante.set_name

		for cons in self._consequent:
			idx = header.index(cons.variable_name)
			row[idx] = cons.set_name

		return row