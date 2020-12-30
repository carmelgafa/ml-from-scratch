import random
import math 

def same_date_birthday(num_poeple, num_same):
    possibility_dates = range(366)
    birthdays = [0] * 366
    for p in range(num_poeple):
        birth_date = random.choice(possibility_dates)
        birthdays[birth_date] += 1
    return max(birthdays) >= num_same

def birthday_problem(num_poeple, num_same, num_trials):
    num_hits = 0
    for t in range(num_trials):
        if same_date_birthday(num_poeple, num_same):
            num_hits += 1

    return num_hits/num_trials



if __name__ == "__main__":
    for num_people in [10,20,40,100]:
        print(f'for {num_people} est prob of shared birthday is {birthday_problem(num_people, 2, 90000)}')

        num = math.factorial(366)
        den = (366**num_people)*math.factorial(366-num_people)

        print(f'actual prob for {num_people} is {1-(num/den)}')