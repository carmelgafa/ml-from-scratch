'''Loaded dice implementation'''

import random
import numpy as np
import matplotlib.pyplot as plt

class LoadedDice:
    '''A loaded dice. probabilities for each number defined in __init_'''

    def __init__(self) -> None:
        '''Initializes new dice'''
        self.probabilities = np.array([0.5, 0.1, 0.1, 0.1, 0.1, 0.1])
        self.cumul_array = np.cumsum(self.probabilities)

    def roll(self)->int:
        '''rolls dice'''
        precision = 3
        random_number = random.randint(0, 10 ** precision) / float(10 ** precision)
        mapped_cumul = self.cumul_array - random_number
        rolled_number = np.where(mapped_cumul > 0, mapped_cumul, np.inf).argmin()
        return rolled_number + 1

    def roll_multiple(self, number_of_tosses):
        '''rolls dice multiple times'''
        x = np.random.random((number_of_tosses, 1)).squeeze()
        x = np.ceil(x*10)-4
        x[x<=0] = 1
        return x


    def test_die(self)->None:
        '''executes a test for the dice'''
        outcomes = []

        number_of_trials = 5000
        for i in range(number_of_trials):
            outcomes.append(self.roll())

        results = []
        for i in np.arange(1,7):
            results.append(outcomes.count(i) / number_of_trials)

        plt.bar(np.arange(1,7), results, color='g', edgecolor='blue', width=1)
        plt.show()

if __name__ == '__main__':
    die = LoadedDice()
    print(die.roll_multiple(100000))
    die.test_die()
