from .fuzzy_variable import FuzzyVariable

class FuzzyOutputVariable(FuzzyVariable):

    def __init__(self, name, min_val, max_val, res):
        super().__init__(name, min_val, max_val, res)

if __name__ == "__main__":
    pass