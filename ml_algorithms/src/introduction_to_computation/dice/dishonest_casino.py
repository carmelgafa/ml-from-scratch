import matplotlib.pyplot as plt
from fair_die import FairDie
from loaded_die import LoadedDie
from numpy import mean
from numpy import arange
import random
import enum



class DiceThrow(enum.Enum):
    FAIR = enum.auto()
    LOADED = enum.auto()
class DishonestCasino():

    def __init__(self, p1:float, p2:float) -> None:
        self.fair_die = FairDie()
        self.biased_die = LoadedDie()
        self.p_1 = p1
        self.p_2 = p2



    def play(self, number_of_tosses:int)->float:

        results = []
        next_toss = DiceThrow.FAIR
        prob_first_toss = random.uniform(0,1)
        if prob_first_toss > 0.5:
            next_toss = DiceThrow.LOADED

        fair_toss_counter = 0
        loaded_toss_counter = 0


        for i in range(number_of_tosses):

            if next_toss == DiceThrow.FAIR:
                fair_toss_counter += 1
                prob_next_toss = random.uniform(0,1)
                if prob_next_toss > self.p_1:
                    next_toss = DiceThrow.LOADED
            else:
                loaded_toss_counter += 1
                prob_next_toss = random.uniform(0,1)
                if prob_next_toss > self.p_2:
                    next_toss = DiceThrow.FAIR
        
        # print(fair_toss_counter)
        # print(loaded_toss_counter)
        
        fair_tosses = self.fair_die.roll_multiple(fair_toss_counter)
        loaded_tosses = self.biased_die.roll_multiple(loaded_toss_counter)
        
        mean_all_tosses = (sum(fair_tosses)+sum(loaded_tosses))/(fair_toss_counter+loaded_toss_counter)
        
        return mean_all_tosses



    def play_old(self, number_of_tosses:int)->list:

        results = []

        next_toss = DiceThrow.FAIR
        prob_first_toss = random.uniform(0,1)
        if prob_first_toss > 0.5:
            next_toss = DiceThrow.LOADED

        for i in range(number_of_tosses):

            if next_toss == DiceThrow.FAIR:
                results.append(self.fair_die.roll())
                prob_next_toss = random.uniform(0,1)
                if prob_next_toss > self.p_1:
                    next_toss = DiceThrow.LOADED
            else:
                results.append(self.biased_die.roll())
                prob_next_toss = random.uniform(0,1)
                if prob_next_toss > self.p_2:
                    next_toss = DiceThrow.FAIR
        return results

    def simulate(self, t:int):
        '''Simulate Method'''
        simulation_mean = self.play(t)
        return mean(simulation_mean)


    def test(self)->None:

        avg_results = []
        number_tosses_per_play = 100
        number_of_plays = 10
        for i in range(0, number_of_plays):
            # append the average opf the tosses
            play = self.play(number_tosses_per_play)
            mean_play = mean(play)
            print(mean_play)
            avg_results.append(mean_play)

        # possible averages from 1 to 6 in steps of 0.5
        # ie 11 possible outcomes
        avg_frequencies = []
        for i in arange(1,6.5, 0.5):
            avg_frequencies.append(avg_results.count(i) / number_of_plays)

        print(avg_frequencies)
        plt.bar(arange(1,6.5, 0.5).tolist(), avg_frequencies, color='g', edgecolor='blue', width=0.5)
        plt.show()

if __name__=='__main__':
    casino = DishonestCasino(0.99, 0.1)
    print(casino.play(100000))