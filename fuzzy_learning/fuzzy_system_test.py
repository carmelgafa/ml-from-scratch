from fuzzy_system.type1_fuzzy_variable import Type1FuzzyVariable
from fuzzy_system.fuzzy_system import FuzzySystem
from fuzzy_system.fuzzy_clause import FuzzyClause

x1 = Type1FuzzyVariable(0, 100, 100, 'x1')
x1.add_triangular('S', 0, 25, 50)
x1.add_triangular('M', 25, 50, 75)
x1.add_triangular('L', 50, 75, 100)

x2 = Type1FuzzyVariable(0, 100, 100, 'x2')
x2.add_triangular('S', 0, 25, 50)
x2.add_triangular('M', 25, 50, 75)
x2.add_triangular('L', 50, 75, 100)

y = Type1FuzzyVariable(0, 100, 100, 'y')
y.add_triangular('S', 0, 25, 50)
y.add_triangular('M', 25, 50, 75)
y.add_triangular('L', 50, 75, 100)

z = Type1FuzzyVariable(0, 100, 100, 'z')
z.add_triangular('S', 0, 25, 50)
z.add_triangular('M', 25, 50, 75)
z.add_triangular('L', 50, 75, 100)

system = FuzzySystem()
system.add_input_variable(x1)
system.add_input_variable(x2)
system.add_output_variable(y)
system.add_output_variable(z)

system.add_rule(
		{ 'x1':'S',
			'x2':'S' },
		{ 'y':'S',
			'z':'L' })

system.add_rule(
		{ 'x1':'M',
			'x2':'M' },
		{ 'y':'M',
			'z':'M' })

system.add_rule(
		{ 'x1':'L',
			'x2':'L' },
		{ 'y':'L',
			'z':'S' })

system.add_rule(
		{ 'x1':'S',
			'x2':'M' },
		{ 'y':'S',
			'z':'L' })

system.add_rule(
		{ 'x1':'M',
			'x2':'S' },
		{ 'y':'S',
			'z':'L' })

system.add_rule(
		{ 'x1':'L',
			'x2':'M' },
		{ 'y':'L',
			'z':'S' })

system.add_rule(
		{ 'x1':'M',
			'x2':'L' },
		{ 'y':'L',
			'z':'S' })

system.add_rule(
		{ 'x1':'L',
			'x2':'S' },
		{ 'y':'M',
			'z':'M' })

system.add_rule(
		{ 'x1':'S',
			'x2':'L' },
		{ 'y':'M',
			'z':'M' })

output = system.evaluate_output({
				'x1':35,
				'x2':75
		})

fam = system.create_fam('y')

print(fam)

print(output)
