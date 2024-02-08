import random

def roll_die():
    # chose from uniform distribution
    return random.choice([1,2,3,4,5,6])


def test_roll(n=10):
    result = ''
    for i in range(n):
        result = result + str(roll_die())
    print(result)


def run_sim(goal, num_trials):
    total = 0

    for i in range(num_trials):
        result=''
        for j in range(len(goal)):
            result += str(roll_die())
        if result == goal:
            total += 1
    
    print(f'actual prob of {goal} = ', round(1/(6**len(goal)), 8))
    est_prob = round(total/num_trials, 8)
    print(f'estimated prob of {goal} = ', est_prob)

if __name__ == "__main__":
    # test_roll()
    run_sim('11111', 1000000)