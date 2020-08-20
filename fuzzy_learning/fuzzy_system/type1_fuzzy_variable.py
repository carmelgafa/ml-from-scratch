from fuzzy_system.type1_fuzzy_set import Type1FuzzySet
import matplotlib.pyplot as plt
import numpy as np
import fuzzy_system.system_settings

class Type1FuzzyVariable():
	'''
	A type-1 fuzzy variable that is mage up of a number of type-1 fuzzy sets
	'''

	def __init__(self, min_val, max_val, res, name=''):
		'''
		creates a new type-1 fuzzy variable (universe)

		Arguments:
		----------
			min_val -- number, minimum value of variable
			max_val -- number, maximum value of variable
			res -- int, resolution of variable
		'''
		self._sets={}
		self._max_val = max_val
		self._min_val = min_val
		self._res = res
		self._name = name
		self._delta = (self._max_val - self._min_val) / (self._res - 1)

		self._fuzzification_results = {}

	def __str__(self):
		return ', '.join(self._sets.keys())

	@property
	def set_count(self):
		return len(self._sets)


	@property
	def name(self):
		return self._name

	def _adjust_value(self, value):
		'''
		Adjusts a value so that it matches a bin value as this is a discrete system

		Arguments:
		----------
		value -- number, a value to map on the variable scale

		Returns
		-------
		value -- number, adjusted
		'''

		old_val = value
		
		if value < self._min_val:
			value = self._min_val
		elif value > self._max_val:
			value = self._max_val
		else:
			value = round((round((value - self._min_val) / self._delta) * self._delta) + self._min_val, fuzzy_system.system_settings.PRECISION)

		return value

	def _add_set(self, name, f_set):
		'''
		adds a fuzzy set to the variable

		Arguments:
		----------
			name -- string, name of the set
			f_set -- Type1FuzzySet, The set
		'''
		self._sets[name] = f_set
		self._fuzzification_results[name] = 0

	def get_set(self, name):
		'''
		returns a set given the name
		TODO ass checks
		Arguments:
		----------
		name -- str, set name

		Returns:
		--------
		set -- Type1FuzzySet, the set
		'''
		return self._sets[name]

	def get_sets_names(self):
		'''
		returns a list containing the set names of the variable
		'''	
		return list(self._sets.keys())

	def add_triangular(self, name, low, mid, high):
		'''
		creates a triangular set for this variable
		TODO add checks

		Arguments:
		----------
			name -- str, name of set
			low -- number, lowest value having a dom of 0
			mid -- number, mid value having a dom of 1
			high -- number, high value having a dom of 0

		Returns:
		--------
			set -- Type1FuzzySet, the created set
		'''

		low = self._adjust_value(low)
		mid = self._adjust_value(mid)
		high = self._adjust_value(high)

		new_set = Type1FuzzySet.create_triangular(self._min_val, 
					self._max_val, self._res, low, mid, high, name)

		self._add_set(name, new_set)

		return new_set


	def add_trapezoidal(self, name, low, mid, high):
		'''
		creates a triangular set for this variable
		TODO add checks

		Arguments:
		----------
			name -- str, name of set
			low -- number, lowest value having a dom of 0
			mid -- number, mid value having a dom of 1
			high -- number, high value having a dom of 0

		Returns:
		--------
			set -- Type1FuzzySet, the created set
		'''

		low = self._adjust_value(low)
		mid = self._adjust_value(mid)
		high = self._adjust_value(high)

		new_set = Type1FuzzySet. create_trapezoidal(self._min_val, 
					self._max_val, self._res, low, mid, high, name)


		self._add_set(name, new_set)

		return new_set


	def generate_sets_mean(self, n, mean):
		'''
		generates 2n+1 fuzzy sets in the variable

		Arguments:
		----------
			n -- int, the number of sets generated will be 2n+1
		'''
		no_sets = (2 * n) + 1
		
		set_half_support_pre = (mean - self._min_val) / (n)
		
		set_half_support_post = (self._max_val - mean) / (n)



		# set_count will ne used to name the sets
		set_count = 1
		set_name = str(set_count)


		# first set will be half triangle with both low and mid point at the min value
		s = Type1FuzzySet.create_trapezoidal(self._min_val, self._max_val, self._res, self._min_val, 
				self._min_val, set_half_support_pre + self._min_val, set_name)
		self._add_set(set_name, s)



		for i in range(0, n-1):
			set_count = set_count + 1
			set_name = str(set_count)

			s = Type1FuzzySet.create_trapezoidal(self._min_val, self._max_val, self._res,
			i*set_half_support_pre + self._min_val, 
			(i+1)*set_half_support_pre + self._min_val,
			(i+2)*set_half_support_pre + self._min_val, set_name)

			self._add_set(set_name, s)



		# first set will be half triangle with both low and mid point at the min value
		set_count = set_count + 1
		set_name = str(set_count)

		s = Type1FuzzySet.create_trapezoidal(self._min_val, self._max_val, self._res, mean - set_half_support_pre, 
				mean, mean + set_half_support_post, set_name)

		self._add_set(set_name, s)



		for i in range(0, n-1):
			set_count = set_count + 1
			set_name = str(set_count)

			s = Type1FuzzySet.create_trapezoidal(self._min_val, self._max_val, self._res,
					i*set_half_support_post + mean, 
					(i+1)*set_half_support_post + mean,
					(i+2)*set_half_support_post + mean, set_name)

			self._add_set(set_name, s)




		# last set will be half triangle with both mid and high point at the hight value

		set_count = set_count + 1
		set_name = str(set_count)

		s = Type1FuzzySet.create_trapezoidal(self._min_val, self._max_val, self._res, 
				self._max_val - set_half_support_post, self._max_val, self._max_val, set_name)
		self._add_set(set_name, s)



	def generate_sets(self, n):
		'''
		generates 2n+1 fuzzy sets in the variable

		Arguments:
		----------
			n -- int, the number of sets generated will be 2n+1
		'''
		
		names = ['s' + str(i) for i in range(n,0,-1)] + ['ce'] + ['b' + str(i) for i in range(1,n+1,1)]

		
		no_sets = (2 * n) + 1
		set_half_support = (self._max_val - self._min_val) / (2 * n)

		# set_count will ne used to name the sets


		# first set will be half triangle with both low and mid point at the min value
		s = Type1FuzzySet.create_triangular(self._min_val, self._max_val, self._res, self._min_val, 
				self._min_val, set_half_support + self._min_val, names[0])
		self._add_set(names[0], s)


		for i in range(0, no_sets-2):

			s = Type1FuzzySet.create_triangular(self._min_val, self._max_val, self._res,
					i*set_half_support + self._min_val, 
					(i+1)*set_half_support + self._min_val,
					(i+2)*set_half_support + self._min_val, names[i+1])

			self._add_set(names[i+1], s)


		# last set will be half triangle with both mid and high point at the hight value


		s = Type1FuzzySet.create_triangular(self._min_val, self._max_val, self._res, 
				self._max_val - set_half_support, self._max_val, self._max_val, names[len(names)-1])
		self._add_set(names[len(names)-1], s)

	def plot_variable(self, ax=None, show=True):
		'''
		plots a graphical representation of the fuzzy variable

		Reference:
		----------
			https://stackoverflow.com/questions/4700614/how-to-put-the-legend-out-of-the-plot
		'''
		if ax == None:
			ax = plt.subplot(111)

		for n ,s in self._sets.items():
			ax.plot(s.domain_elements(), s.dom_elements(), label=n)

		# Shrink current axis by 20%
		pos = ax.get_position()
		ax.set_position([pos.x0, pos.y0, pos.width * 0.8, pos.height])
		ax.grid(True, which='both', alpha=0.4)
		ax.set_title(self._name)
		ax.set(xlabel='x', ylabel='$\mu (x)$')


		# Put a legend to the right of the current axis
		ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

		if show:
			plt.show()


	def fuzzify_variable(self, value):
		'''
		performs fuzzification of the variable. used when the
		variable is an input one

		Arguments:
		-----------
		value -- number, input value for the variable

		'''
		# adjust the input value
		value = self._adjust_value(value)

		# get dom for each set and store it - it will be required for each rule
		for set_name, f_set in self._sets.items():
			# print(set_name, f_set[value])
			f_set.last_dom_value = f_set[value]

	def get_set_greater_dom(self, variable_value):

		variable_value = self._adjust_value(float(variable_value))

		res_f_set = None
		res_dom = -1

		for f_set_name, f_set in self._sets.items():

			dom = f_set[variable_value]
			if dom > res_dom:
				res_dom = dom
				res_f_set = f_set

		return res_f_set, res_dom


	def variable_state(self):
	
		res = []

		res.append('-----------------------------')
		res.append('\n')
		res.append(self._name)
		res.append('\n')

		for _, f_set in self._sets.items():
			res.append(f_set.name)
			res.append(str(f_set.last_dom_value))
			res.append('\n')

		res.append('-----------------------------')
		return ' '.join(res)
