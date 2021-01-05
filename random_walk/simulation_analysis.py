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
    return f.get_location(d), start.dist(f.get_location(d))

def sim_walks(num_steps, num_trials, dClass):
    drunkard = dClass()
    origin = Location(0, 0)
    distances = []
    end_locations = []
    
    for t in range(num_trials):
        f = Field()
        f.add_drunk(drunkard, origin)
        end_location, distance =  walk(f, drunkard, num_steps)

        distances.append(round(distance,1))
        end_locations.append([end_location.x, end_location.y])

    return end_locations, distances


def drunk_test_dist_analysis(walk_lengths, num_trials):
    
    mean_dist_x = []
    mean_dist_y = []
    for num_steps in walk_lengths:
        _, distances = sim_walks(num_steps, num_trials, UsualDrunk)
        mean_dist_y.append(round(sum(distances)/len(distances), 4))
        mean_dist_x.append(num_steps)

    plt.plot(mean_dist_x, mean_dist_y)

    mean_dist_x.clear()
    mean_dist_y.clear()
    for num_steps in walk_lengths:
        _, distances = sim_walks(num_steps, num_trials, BiasedDrunk)
        mean_dist_y.append(round(sum(distances)/len(distances), 4))
        mean_dist_x.append(num_steps)

    plt.plot(mean_dist_x, mean_dist_y)
    plt.show()

def drunk_test_end_analysis(walk_lengths, num_trials):
    for num_steps in walk_lengths:
        end_locations, _ = sim_walks(num_steps, num_trials, UsualDrunk)
        end_locations = np.array(end_locations)
        plt.scatter(end_locations[:,0], end_locations[:,1])
    
    for num_steps in walk_lengths:
        end_locations, _ = sim_walks(num_steps, num_trials, BiasedDrunk)
        end_locations = np.array(end_locations)
        plt.scatter(end_locations[:,0], end_locations[:,1])
    
    plt.show()



def drunk_test(walk_lengths, num_trials,dClass):
    for num_steps in walk_lengths:
        end_locations, distances = sim_walks(num_steps, num_trials, dClass)
        end_locations = np.array(end_locations)
        print(f'{dClass.__name__} random walk of {num_steps} steps')
        print(f'Mean = {round(sum(distances)/len(distances), 4)}')
        print(f'Max={max(distances)}')
        print(f'Min={min(distances)}')
        plt.scatter(end_locations[:,0], end_locations[:,1])
        plt.show()

if __name__ == "__main__":
    # drunk_test((10,100,1000), 1000, BiasedDrunk)
    # drunk_test_dist_analysis((10,100,1000, 10000), 100)
    # xyz=np.array(np.random.random((100,3)))
    # print(xyz)
    drunk_test_end_analysis((0,1000), 100)
