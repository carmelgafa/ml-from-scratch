import numpy as np


class FuzzyAssociativeMemory():

    def __init__(self, variables_info, fam_shape):
        '''
        '''
        self._variables_info = variables_info
        self._fam  = np.empty(fam_shape, dtype='object')

    def set_entity(self, location, value):
        '''
        '''
        entity_location = []

        for variable, f_sets in self._variables_info.items():
            f_set = location[variable]
            entity_location.append(f_sets.index(f_set))

        self._fam[tuple(entity_location)] = value


    def __str__(self):
        return str(self._fam)
