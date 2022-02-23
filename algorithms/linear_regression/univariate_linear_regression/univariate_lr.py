import pandas as pd
import os

# import data from csv
full_filename = os.path.join(os.path.dirname(__file__), '..', 'data_generation', 'data_1f.csv')
data_set = pd.read_csv(full_filename)

data_set.columns=['x', 'y']

# add new columns required to solve the problem
data_set['x_sq'] = data_set['x']**2
data_set['xy'] = data_set['x']*data_set['y']


# calculate the sums of the data
sum_x = data_set['x'].sum()
sum_y = data_set['y'].sum()
sum_x_sq = data_set['x_sq'].sum()
sum_xy = data_set['xy'].sum()

n = len(data_set)
print(f'sum_x: {sum_x}, sum_y: {sum_y}, sum_x_sq: {sum_x_sq}, sum_xy: {sum_xy}, n: {n}')

# calculate the slope and intercept
a_0 = (sum_x_sq*sum_y - sum_x*sum_xy)/(n*sum_x_sq - sum_x**2)

a_1 = (n*sum_xy - sum_x*sum_y)/(n*sum_x_sq - sum_x**2)

print(f'a_0: {a_0}, a_1: {a_1}')