import pandas as pd

# import data from csv
data = pd.read_csv("data.csv")
data.columns=['x', 'y']

# add new columns required to solve the problem
data['x_sq'] = data['x']**2
data['xy'] = data['x']*data['y']


# calculate the sums of the data
sum_x = data['x'].sum()
sum_y = data['y'].sum()
sum_x_sq = data['x_sq'].sum()
sum_xy = data['xy'].sum()

n = len(data)
print(f'sum_x: {sum_x}, sum_y: {sum_y}, sum_x_sq: {sum_x_sq}, sum_xy: {sum_xy}, n: {n}')

# calculate the slope and intercept
a_0 = (sum_x_sq*sum_y - sum_x*sum_xy)/(n*sum_x_sq - sum_x**2)

a_1 = (n*sum_xy - sum_x*sum_y)/(n*sum_x_sq - sum_x**2)

print(f'a_0: {a_0}, a_1: {a_1}')