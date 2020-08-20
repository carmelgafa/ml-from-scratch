#from fuzzy_learning._implementation.fuzzy_system import *
from fuzzy_system.fuzzy_system import FuzzySystem
from fuzzy_system.fuzzy_clause import FuzzyClause


# adding an age linguistic variable1
input_var = Type1FuzzyVariable(0, 100, 100, 'Temperature')
input_var.add_triangular('S2', 0, 0, 25)
input_var.add_triangular('S1', 0, 25, 50)
input_var.add_triangular('CE', 25, 50, 75)
input_var.add_triangular('B1', 50, 75, 100)
input_var.add_triangular('B2', 75, 100, 100)


# adding an age linguistic variable
input2_var = Type1FuzzyVariable(0, 100, 100, 'Humidity')
input2_var.add_triangular('S2', 0, 0, 25)
input2_var.add_triangular('S1', 0, 25, 50)
input2_var.add_triangular('CE', 25, 50, 75)
input2_var.add_triangular('B1', 50, 75, 100)
input2_var.add_triangular('B2', 75, 100, 100)

output_var = Type1FuzzyVariable(0, 100, 100, 'Speed')
output_var.add_triangular('L2', 0, 0, 25)
output_var.add_triangular('L1', 0, 25, 50)
output_var.add_triangular('M', 25, 50, 75)
output_var.add_triangular('H1', 50, 75, 100)
output_var.add_triangular('H2', 75, 100, 100)

system = FuzzySystem()
system.add_input_variable(input_var)
system.add_input_variable(input2_var)
system.add_output_variable(output_var)

ante={
    'Temperature' : 'S2',
    'Humidity' : 'S2'
}
cons ={
    'Speed' : 'H2'
}

system.add_rule(ante, cons)

print(system)
