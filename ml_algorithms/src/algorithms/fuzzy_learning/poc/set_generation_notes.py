from type2fuzzy import Type1FuzzyVariable

# adding an age linguistic variable
var = Type1FuzzyVariable(0, 100, 100)

var.add_triangular('S2', 0, 0, 25)
var.add_triangular('S1', 0, 25, 50)
var.add_triangular('CE', 25, 50, 75)
var.add_triangular('B1', 50, 75, 100)
var.add_triangular('B2', 75, 100, 100)

var.plot_variable()