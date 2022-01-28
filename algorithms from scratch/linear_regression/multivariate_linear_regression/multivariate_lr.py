import pandas as pd
import os

# import data from csv
full_filename = os.path.join(os.path.dirname(__file__), "data.csv")

data = pd.read_csv(full_filename)

data['x1_sq'] = data['x1']**2
data['x2_sq'] = data['x2']**2
data['x1y'] = data['x1']*data['y']
data['x2y'] = data['x2']*data['y']
data['x1x2'] = data['x1']*data['x2']

n = len(data)

sum_X1_sq = data['x1_sq'].sum() - (data['x1'].sum()**2)/n
print(f'sum_X1_sq: {sum_X1_sq}')

sum_X2_sq = data['x2_sq'].sum() - (data['x2'].sum()**2)/n
print(f'sum_x2_sq: {sum_X2_sq}')

sum_X1y = data['x1y'].sum() - (data['x1'].sum()*data['y'].sum())/n
print(f'sum_X1y: {sum_X1y}')

sum_X2y = data['x2y'].sum() - (data['x2'].sum()*data['y'].sum())/n
print(f'sum_X2y: {sum_X2y}')

sum_X1X2 = data['x1x2'].sum() - (data['x1'].sum()*data['x2'].sum())/n
print(f'sum_X1X2: {sum_X1X2}')

mean_y = data['y'].mean()
mean_x1 = data['x1'].mean()
mean_x2 = data['x2'].mean()

n = len(data)

a1 = (sum_X2_sq*sum_X1y - sum_X1X2*sum_X2y)/(sum_X1_sq*sum_X2_sq - sum_X1X2**2)

a2 = (sum_X1_sq*sum_X2y - sum_X1X2*sum_X1y)/(sum_X1_sq*sum_X2_sq - sum_X1X2**2)

a0 = mean_y - a1*mean_x1 - a2*mean_x2

print(f'a0: {a0}, a1: {a1}, a2: {a2}')


import numpy as np

y_hat = a0 + a1*data['x1'] + a2*data['x2']

residuals = y_hat - data['y']

cost = np.dot(residuals, residuals)/(2*n)

print(f'cost: {cost}')