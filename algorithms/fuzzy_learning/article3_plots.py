from fuzzy_system.type1_fuzzy_variable import Type1FuzzyVariable
from fuzzy_system.fuzzy_system import FuzzySystem
from fuzzy_system.fuzzy_clause import FuzzyClause


def plot_system():
    x1 = Type1FuzzyVariable(0, 100, 100, 'x1')
    x1.generate_sets(2)

    x2 = Type1FuzzyVariable(0, 100, 100, 'x2')
    x2.generate_sets(3)

    y = Type1FuzzyVariable(0, 100, 100, 'y')
    y.generate_sets(2)

    system = FuzzySystem()
    system.add_input_variable(x1)
    system.add_input_variable(x2)
    system.add_output_variable(y)

    system.plot_system()



if __name__ == "__main__":
    plot_system()