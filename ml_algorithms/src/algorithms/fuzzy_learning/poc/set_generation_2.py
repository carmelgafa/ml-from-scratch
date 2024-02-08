from fuzzy_system.type1_fuzzy_variable import Type1FuzzyVariable

# adding an age linguistic variable
var = Type1FuzzyVariable(0, 100, 100)

# generate (2*3)+1 = 7 sets
var.generate_sets_mean(3, 30)

var.plot_variable()