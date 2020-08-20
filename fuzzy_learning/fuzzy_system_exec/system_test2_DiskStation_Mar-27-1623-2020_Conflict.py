import sys
sys.path.append("..")

from .type1_fuzzy_variable import Type1FuzzyVariable

from fuzzy_system import FuzzySystem
from fuzzy_clause import FuzzyClause

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

system = FuzzySystem()
system.add_input_variable(x1)
system.add_input_variable(x2)
system.add_output_variable(y)

system.add_rule(
    {
        'x1':'S',
        'x2':'M'
    },
    {
        'y':'S'
    }
)

system.add_rule(
    {
        'x1':'M',
        'x2':'L'
    },
    {
        'y':'M'
    }
)
output = system.evaluate_output({
        'x1':44,
        'x2':61
    })

# print(output)