import random

class Drunk():
    '''
    base class for drunkard walk algorithms
    '''
    def __init__(self, name='Anonymous'):
        self._name = name

    def __str__(self):
        return self._name

class UsualDrunk(Drunk):
    def take_step(self):
        step_choices = [(0,1), (1,0), (0,-1), (-1,0)]
        return random.choice(step_choices)

class BiasedDrunk(Drunk):
    '''
    implements biased random walk
    '''
    def take_step(self):
        step_choices = [(0,0.9), (1.1,0), (0,-1), (-1,0)]
        return random.choice(step_choices)

if __name__ == "__main__":
    d1=Drunk('Joe')
    print(d1)

    d2 = Drunk()
    print(d2)

