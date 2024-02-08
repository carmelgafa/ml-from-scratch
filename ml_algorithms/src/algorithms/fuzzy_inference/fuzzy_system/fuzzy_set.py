import numpy as np
import copy
import matplotlib.pyplot as plt


class FuzzySet:

	_precision: int = 3

	def __init__(self, name, domain_min, domain_max, res):
		
		self._domain_min = domain_min
		self._domain_max = domain_max
		self._res = res

		self._domain = np.linspace(domain_min, domain_max, res)
		self._dom = np.zeros(self._domain.shape)
		self._name = name
		self._last_dom_value = 0

	def __getitem__(self, x_val):
		return self._dom[np.abs(self._domain-x_val).argmin()]

	def __setitem__(self, x_val, dom):
		self._dom[np.abs(self._domain-x_val).argmin()] = round(dom, self._precision)

	def __str__(self):
		return ' + '.join([str(a) + '/' + str(b) for a,b in zip(self._dom, self._domain)])

	def __get_last_dom_value(self):
		return self._last_dom_value

	def __set_last_dom_value(self, d):
		self._last_dom_value = d

	last_dom_value = property(__get_last_dom_value, __set_last_dom_value)

	@property
	def name(self):
		return self._name

	@property
	def empty(self):
		return np.all(self._dom == 0)

	@property
	def name(self):
		return self._name

	@classmethod
	def create_trapezoidal(cls, name, domain_min, domain_max, res, a, b, c, d):
		t1fs = cls(name, domain_min, domain_max, res)

		a = t1fs._adjust_domain_val(a)
		b = t1fs._adjust_domain_val(b)
		c = t1fs._adjust_domain_val(c)
		d = t1fs._adjust_domain_val(d)

		t1fs._dom = np.round(np.minimum(np.maximum(np.minimum((t1fs._domain-a)/(b-a), (d-t1fs._domain)/(d-c)), 0), 1), t1fs._precision)
		return t1fs

	@classmethod
	def create_triangular(cls, name, domain_min, domain_max, res, a, b, c):
		t1fs = cls(name, domain_min, domain_max, res)

		a = t1fs._adjust_domain_val(a)
		b = t1fs._adjust_domain_val(b)
		c = t1fs._adjust_domain_val(c)

		if b == a:
			t1fs._dom = np.round(np.maximum((c-t1fs._domain)/(c-b), 0), t1fs._precision)
		elif b == c:
			t1fs._dom = np.round(np.maximum((t1fs._domain-a)/(b-a), 0), t1fs._precision)
		else:
			t1fs._dom = np.round(np.maximum(np.minimum((t1fs._domain-a)/(b-a), (c-t1fs._domain)/(c-b)), 0), t1fs._precision)
		
		return t1fs

	def _adjust_domain_val(self, x_val):
		return self._domain[np.abs(self._domain-x_val).argmin()]

	def clear_set(self):
		self._dom.fill(0)

	def min_scalar(self, val):
		
		result = FuzzySet(f'({self._name}) min ({val})', self._domain_min, self._domain_max, self._res)
		result._dom = np.minimum(self._dom, val)

		return result

	def union(self, f_set):

		result = FuzzySet(f'({self._name}) union ({f_set._name})', self._domain_min, self._domain_max, self._res)
		result._dom = np.maximum(self._dom, f_set._dom)

		return result

	def intersection(self, f_set):

		result = FuzzySet(f'({self._name}) intersection ({f_set._name})', self._domain_min, self._domain_max, self._res)
		result._dom = np.minimum(self._dom, f_set._dom)

		return result

	def complement(self):

		result = FuzzySet(f'not ({self._name})', self._domain_min, self._domain_max, self._res)
		result._dom = 1 - self._dom

		return result

	def cog_defuzzify(self):
		
		num = np.sum(np.multiply(self._dom, self._domain))
		den = np.sum(self._dom)

		return num/den

	def domain_elements(self):
		return self._domain

	def dom_elements(self):
		return self._dom

	def plot_set(self, ax, col=''):
		ax.plot(self._domain, self._dom, col)
		ax.set_ylim([-0.1,1.1])
		ax.set_title(self._name)
		ax.grid(True, which='both', alpha=0.4)
		ax.set(xlabel='x', ylabel='$\mu(x)$')

if __name__ == "__main__":
	s = FuzzySet.create_trapezoidal('test', 1, 100, 100, 20, 30, 50, 80)

	print(s.empty)

	u = FuzzySet('u', 1, 100, 100)

	print(u.empty)

	t = FuzzySet.create_trapezoidal('test', 1, 100, 100, 30, 50, 90, 100)

	fig, axs = plt.subplots(1, 1)

	s.union(t).complement().intersection(s).min_scalar(0.2).plot_set(axs)

	plt.show()
	print(s.cog_defuzzify())
