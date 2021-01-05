from field import Field
from drunk import UsualDrunk
from drunk import BiasedDrunk
from location import Location
import numpy as np
import matplotlib.pylab as plt


def walk(f, d, num_steps):
    start = f.get_location(d)
    for s in range(num_steps):
        f.move_drunk(d)
        # print(f.get_location(d))
    return start.dist(f.get_location(d))

def sim_walks(num_steps, num_trials, dClass):
    drunkard = dClass()
    origin = Location(0, 0)
    distances = []
    for t in range(num_trials):
        f = Field()
        f.add_drunk(drunkard, origin)
        distances.append(round(walk(f, drunkard, num_steps) ,1))

    return distances

def drunk_test(walk_lengths, num_trials,dClass):
    for num_steps in walk_lengths:
        distances = sim_walks(num_steps, num_trials, dClass)
        print(f'{dClass.__name__} random walk of {num_steps} steps')
        print(f'Mean = {round(sum(distances)/len(distances), 4)}')
        print(f'Max={max(distances)}')
        print(f'Min={min(distances)}')

if __name__ == "__main__":
    drunk_test((0,1,2), 100, UsualDrunk)