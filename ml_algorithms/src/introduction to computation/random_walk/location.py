import math

class Location():
    def __init__(self, x:float, y:float):
        self._x = x
        self._y = y
    
    def move (self, delta_x:float, delta_y:float):
        return Location(self._x + delta_x, self._y + delta_y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    def dist(self, other):
        x_dist = self._x - other.x
        y_dist = self._y - other.y

        return (x_dist**2 + y_dist**2)**0.5

    def __str__(self):
        return f'<{self._x}, {self._y}>'

if __name__ == "__main__":
    loc = Location(1,1)
    print(loc)
    dist = loc.dist(Location(0,0))
    print(dist)