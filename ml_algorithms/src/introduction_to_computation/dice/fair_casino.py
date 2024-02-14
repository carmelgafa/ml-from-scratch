import matplotlib.pyplot as plt
from fair_die import FairDie
from numpy import mean
from numpy import arange
import numpy as np

class FairCasino():

    def __init__(self) -> None:
        self.die = FairDie()

    def play(self, number_of_tosses:int=2):
        return self.die.roll_multiple(number_of_tosses)


    def simulate(self, t):
        mean_res = mean(self.play(t))
        print(mean_res)
        return mean_res

    def test(self)->None:

        avg_results = []

        number_of_plays = 5000
        for i in range(0, number_of_plays):
            # append the average opf the tosses
            play = self.play()
            mean_play = mean(play)
            avg_results.append(mean_play)

        # possible averages from 1 to 6 in steps of 0.5
        # ie 11 possible outcomes
        avg_frequencies = []
        for i in arange(1,6.5, 0.5):
            avg_frequencies.append(avg_results.count(i) / number_of_plays)

        print(avg_frequencies)

        plt.bar(arange(1,6.5, 0.5), avg_frequencies, color='g', edgecolor='blue', width=0.5)
        plt.show()


if __name__=='__main__':
    casino = FairCasino()
    casino.test()
