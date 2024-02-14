from dishonest_casino import DishonestCasino
from fair_casino import FairCasino
import csv
import numpy as np

def fair_casino_simulation():
    casino = FairCasino()

    mean_results = []

    for _ in range(10000):
        mean_results.append(casino.simulate(100000))

    with open('fair_results.csv', 'w') as f:
        write = csv.writer(f)
        write.writerow(mean_results)

    mean = sum(mean_results)/len(mean_results)
    print('Mean for fair casino: ', mean)


def dishonest_casino_simulation_run(p1:float, p2:float):

    mean_results = []

    casino = DishonestCasino(p1, p2)

    for _ in range(10000):
        mean_results.append(casino.simulate(100000))

    with open(f'dishonest_results-{p1}-{p2}.csv', 'w', encoding='UTF-8') as f:
        write = csv.writer(f)
        write.writerow(mean_results)

    simulations_mean = sum(mean_results)/len(mean_results)
    print(f'Mean for dishonest casino with p1:{p1} and p2:{p2} is {simulations_mean}')


def dishonest_casino_simulation():

    dishonest_casino_simulation_run(0.99, 0.05)
    dishonest_casino_simulation_run(0.95, 0.1)
    dishonest_casino_simulation_run(0.9, 0.2)


def calculate_variance(simulation_data:np.array):#type:ignore
    simulation_mean = np.mean(simulation_data)

    variance = np.sum(np.square(simulation_data - simulation_mean))/(np.size(simulation_data)-1)
    standard_deviation = np.sqrt(variance)
    
    print(f'mean: {simulation_mean}, variance:{variance}, standard deviation:{standard_deviation}')


def dishonest_trial_variance_calculation():
    print('Dishonest simulation with p1 = 0.9 and p2 = 0.2')
    simulation_data = np.genfromtxt('dishonest_results-0.9-0.2.csv', delimiter=',')
    calculate_variance(simulation_data)


def fair_trial_variance_calculation():
    print('Fair Simulation')
    simulation_data = np.genfromtxt('fair_results.csv', delimiter=',')
    calculate_variance(simulation_data)

if __name__ == '__main__':
    # fair_casino_simulation()
    # dishonest_casino_simulation()
    dishonest_trial_variance_calculation()
    fair_trial_variance_calculation()
