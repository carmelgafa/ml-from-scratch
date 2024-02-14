import random
import numpy as np
import matplotlib.pyplot as plt

class FairDice:

    def __init__(self) -> None:
        ...

    def roll(self)->int:
        return random.randint(1,6)

    def roll_multiple(self, number_of_tosses):
        x = np.random.random((number_of_tosses, 1)).squeeze()
        return np.ceil(x*6)

    def test_die(self)->None:
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
    die = FairDice()
    die.roll_multiple(10)
