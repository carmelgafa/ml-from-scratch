import numpy as np
# from crisp_set import CrispSet
import copy
from collections import OrderedDict
import fuzzy_system.system_settings


class Type1FuzzySet:
	'''
	taken from type2fuzzy library

	Reference:
	----------
	Zadeh, Lotfi Asker. "The concept of a linguistic variable and its 
	application to approximate reasoning—I." Information sciences 8.3 (1975): 199-249.

	'''
	def __init__(self, name=''):
		self._elements = {}
		self._empty = True
		self._precision = fuzzy_system.system_settings.PRECISION
		self._name = name
		self._last_dom_value = 0
		self._center = float('inf')

	def __getitem__(self, x_val):
		'''
		For a given value of x, return the degree of membership

		Reference:
		----------
		Zadeh, Lotfi Asker. "The concept of a linguistic variable and its 
		application to approximate reasoning—I." Information sciences 8.3 (1975): 199-249.

		Arguments:
		----------
		x_val -- value of x 

		Returns:
		--------
		degree of membership -- float

		'''

		dom = 0

		if x_val in self._elements:
			dom = self._elements[x_val]

		return dom

	def __setitem__(self, x_val, dom):
		
		if x_val in self._elements:
			self._elements[x_val] = dom

	def __str__(self):

		set_elements = []
		dec_places_formatter = '''%0.{}f'''.format(self._precision)

		for domain_val, dom_val in self._elements.items():
			set_elements.append(f'{dec_places_formatter % dom_val}/{dec_places_formatter % domain_val}')

		set_representation = ' + '.join(set_elements)

		return set_representation

	# def __repr__(self):
	# 	return f'{self.__class__.__name__}({str(self)})'

	@property
	def center_value(self):
		return self._center

	@property
	def name(self):
		return self._name


	@classmethod
	def create_trapezoidal(cls, univ_low, univ_hi, univ_res, set_low, set_mid, set_hi, name=''):

		if univ_hi <= univ_low:
			raise Exception('Error in universe definition')
		if (set_hi < set_mid) or (set_mid < set_low):
			raise Exception('Error in triangular set definition')

		factor = 0.9

		t1fs = cls()

		precision = fuzzy_system.system_settings.PRECISION # len(str(univ_res))
		domain_elements =  np.round(np.linspace(univ_low, univ_hi, univ_res), precision)

		idx_low = (np.abs(domain_elements - set_low)).argmin()
		set_low = domain_elements[idx_low]

		idx_hi = (np.abs(domain_elements - set_hi)).argmin()
		set_hi = domain_elements[idx_hi]

		# set_mid_1 = (set_low + set_mid) / 2 
		idx_mid_1 = (np.abs(domain_elements - set_mid_1)).argmin()
		set_mid_1 = domain_elements[idx_mid_1]

		set_mid_2 = (set_hi + set_mid) / 2
		idx_mid_2 = (np.abs(domain_elements - set_mid_2)).argmin()
		set_mid_2 = domain_elements[idx_mid_2]


		# print(set_low, set_mid_1, set_mid_2, set_hi)

		if idx_hi == idx_mid_2:
			for domain_val in domain_elements[idx_low:idx_mid_1+1]:
				dom = (domain_val-set_low)/(set_mid_1-set_low)
				t1fs.add_element(domain_val, round(dom, precision))	

			for  domain_val in domain_elements[idx_mid_1:idx_mid_2+1]:
				t1fs.add_element(domain_val, 1)	


		elif idx_low == idx_mid_1:

			for  domain_val in domain_elements[idx_mid_1:idx_mid_2+1]:
				t1fs.add_element(domain_val, 1)	

			for domain_val in domain_elements[idx_mid_2:idx_hi+1]:
				dom = (set_hi-domain_val)/(set_hi-set_mid_2)
				t1fs.add_element(domain_val, round(dom, precision))
		
		else:
			for domain_val in domain_elements[idx_low:idx_mid_1]:
				dom = (domain_val-set_low)/(set_mid_1-set_low)
				t1fs.add_element(domain_val, round(dom, precision))	

			for  domain_val in domain_elements[idx_mid_1:idx_mid_2+1]:
				t1fs.add_element(domain_val, 1)	

			for domain_val in domain_elements[idx_mid_2+1 :idx_hi+1]:
				dom = (set_hi-domain_val)/(set_hi-set_mid_2)
				t1fs.add_element(domain_val, round(dom, precision))

		t1fs._name = name

		return t1fs





	@classmethod
	def create_triangular(cls, univ_low, univ_hi, univ_res, set_low, set_mid, set_hi, name=''):

		'''
		Creates a triangular type 1 fuzzy set in a defined universe of discourse
		The triangle is mage of three points; the low where the dom is 0, the mid where the
		dom is 1 and the high where the dom is 0

		References
		----------
		Pedrycz, Witold, and Fernando Gomide. 
		An introduction to fuzzy sets: analysis and design. Mit Press, 1998.

		Arguments:
		----------
		univ_low -- lower value of the universe of discourse
		univ_hi -- higher value of the universe of discourse
		univ_res -- resolution of the universe of discourse
		set_low -- sel low point, where dom is 0
		set_mid -- sel mid point, where dom is 1
		set_hi -- sel high point, where dom is 0

		Returns:
		--------
		The new type1 triangular fuzzy set
		'''

		if univ_hi <= univ_low:
			raise Exception('Error in universe definition')
		if (set_hi < set_mid) or (set_mid < set_low):
			raise Exception('Error in triangular set definition')

		t1fs = cls()

		precision = fuzzy_system.system_settings.PRECISION # len(str(univ_res))
		domain_elements =  np.round(np.linspace(univ_low, univ_hi, univ_res), precision)

		idx_mid = (np.abs(domain_elements - set_mid)).argmin()
		set_mid = domain_elements[idx_mid]

		idx_low = (np.abs(domain_elements - set_low)).argmin()
		set_low = domain_elements[idx_low]

		idx_hi = (np.abs(domain_elements - set_hi)).argmin()
		set_hi = domain_elements[idx_hi]

		if idx_low > 0:
			for domain_val in domain_elements[0:idx_low]:
				t1fs.add_element(domain_val, 0)	

		if idx_hi == idx_mid:
			for domain_val in domain_elements[idx_low:idx_mid+1]:
				dom = (domain_val-set_low)/(set_mid-set_low)
				t1fs.add_element(domain_val, round(dom, precision))			
		elif idx_low == idx_mid:
			for domain_val in domain_elements[idx_mid:idx_hi+1]:
				dom = (set_hi-domain_val)/(set_hi-set_mid)
				t1fs.add_element(domain_val, round(dom, precision))
		else:
			for domain_val in domain_elements[idx_low:idx_hi+1]:
				dom = dom = max(min((domain_val - set_low)/(set_mid - set_low), (set_hi - domain_val)/(set_hi - set_mid)), 0)
				t1fs.add_element(domain_val, round(dom, precision))

		# print(idx_hi, univ_res)
		if idx_hi < univ_res:
			for domain_val in domain_elements[idx_hi:univ_res]:
				t1fs.add_element(domain_val, 0)	


		t1fs._name = name

		return t1fs

	def _sort_set(self):
		'''
		sorts a type-1 fuzzy set so that all somain values (keys) are 
		in ascending order
		'''
		self._elements = OrderedDict( sorted(self._elements.items()))

	def _get_last_dom_value(self):
		return self._last_dom_value

	def _set_last_dom_value(self, d):
		if d < 0:
			self._last_dom_value = 0
		elif d > 1:
			self._last_dom_value = 1
		else:
			self._last_dom_value = d

	last_dom_value = property(_get_last_dom_value, _set_last_dom_value)

	def add_element(self, domain_val, dom_val):
		'''
		Adds a new element to the t1fs. If there is already an element at the stated
		domain value the maximum degree of membership value is kept

		Arguments:
		----------
		domain_val -- float, the value of x
		degree_of_membership, float value between 0 and 1. The degree of membership
		'''
		if dom_val > 1:
			raise ValueError('degree of membership must not be greater than 1, {} : {}'.format(domain_val, dom_val))

		if domain_val in self._elements:
			self._elements[domain_val] = max(self._elements[domain_val], dom_val)
		else:
			self._elements[domain_val] = dom_val
			self._empty = False

		if dom_val == 1:
			self._center = min(self._center, domain_val)
		

	def clear_set(self):
		if not self._empty:
			self._elements = {}
			self._empty = True
			self._precision = 3
			self._name = name
			self._last_dom_value = 0

	def fuzzy_alpha_cut(self, val):
		
		res_set = Type1FuzzySet()

		for x, u in self._elements.items():
			
			if u > val:
				res_set.add_element(x, val)
			else:
				res_set.add_element(x, u)

		return res_set

	def union(self, f_set):

		result = copy.deepcopy(f_set)

		for x, u in self._elements.items():
			if x in result._elements:
				result[x] = max( result[x], u)
			else:
				result.add_element(x, u)

		result._sort_set()
		return result

	def intersection(self, f_set):

		result = copy.deepcopy(f_set)

		for x, u in self._elements.items():
			if x in result._elements:
				result[x] = min( result[x], u)
			else:
				result.add_element(x, u)

		result._sort_set()
		return result


	def complement(self):

		result = copy.deepcopy(self)

		for x, u in self._elements.items():
			result[x] = 1 - u

		result._sort_set()
		return result


	def cog_defuzzify(self):
		
		num = 0
		den = 0

		for x, u in self._elements.items():
			num = round(num + x * u, fuzzy_system.system_settings.PRECISION)
			den = round(den + u , fuzzy_system.system_settings.PRECISION)

		return(num/den)

	def domain_elements(self):
		return self._elements.keys()

	def dom_elements(self):
		return self._elements.values()

	def plot_set(self, ax, col=''):
		ax.plot(self.domain_elements(), self.dom_elements(), col)
		ax.set_ylim([-0.1,1.1])
		ax.set_title(self._name)
		ax.grid(True, which='both', alpha=0.4)
		ax.set(xlabel='x', ylabel='$\mu(x)$')