from type2fuzzy import Type1FuzzyVariable

# adding an age linguistic variable
var = Type1FuzzyVariable(0, 100, 100)

var.add_triangular('very young', 0, 0, 20)
var.add_triangular('young', 10, 20, 30)
var.add_triangular('adult', 20, 40, 60)
var.add_triangular('old', 50, 70, 90)
var.add_triangular('very old', 70, 100, 100)

var.plot_variable()