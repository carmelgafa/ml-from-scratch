from drunk import UsualDrunk
from drunk import BiasedDrunk
from location import Location

class Field():
    def __init__(self):
        self._drunks = {}
    
    def add_drunk(self, drunk, loc):
        if drunk in self._drunks:
            raise ValueError('duplicate drunk')
        else:
            self._drunks[drunk] = loc

    def get_location(self, drunk):
        if drunk not in self._drunks:
            raise ValueError('drunk not in field')
        
        return self._drunks[drunk]

    def move_drunk(self, drunk):
        if drunk not in self._drunks:
            raise ValueError('drunk not in field')

        x_dist, y_dist = drunk.take_step()

        self._drunks[drunk] = self._drunks[drunk].move(x_dist, y_dist)

        