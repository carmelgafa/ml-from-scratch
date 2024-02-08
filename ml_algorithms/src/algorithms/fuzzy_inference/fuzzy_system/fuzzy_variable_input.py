from .fuzzy_variable import FuzzyVariable

class FuzzyInputVariable(FuzzyVariable):

	def __init__(self, name, min_val, max_val, res):
		super().__init__(name, min_val, max_val, res)

	def fuzzify(self, value):
		'''
		performs fuzzification of the variable. used when the
		variable is an input one

		Arguments:
		-----------
		value -- number, input value for the variable

		'''
		# get dom for each set and store it - it will be required for each rule
		for set_name, f_set in self._sets.items():
			f_set.last_dom_value = f_set[value]

	def fuzzify_info(self, value):
		'''
		performs fuzzification of the variable. used when the
		variable is an input one

		Arguments:
		-----------
		value -- number, input value for the variable

		'''
		# get dom for each set and store it - it will be required for each rule
		for set_name, f_set in self._sets.items():
			f_set.last_dom_value = f_set[value]

		res = []

		res.append(self._name)
		res.append('\n')

		for _, f_set in self._sets.items():
			res.append(f_set.name)
			res.append(str(f_set.last_dom_value))
			res.append('\n')

		return ' '.join(res)


if __name__ == "__main__":
	pass