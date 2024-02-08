# The above code is a simple linear regression model. 
# 
# The model is: 
# 
# y = a0 + a1*x1 + a2*x2 
# 
# The model is fit using the least squares method. 
# 
# The model is tested by computing the cost of the model. 
# 
# The cost is the sum of the squared residuals. 
# 
# The cost is a measure of how good the model is. 
# 
# The lower the cost, the better the model. 

import pandas as pd
import os

# import data from csv
filename = os.path.join(os.path.dirname(__file__), '..', 'data_generation', 'data_2f.csv')
data_set = pd.read_csv(filename)

data_set['x1_sq'] = data_set['x1']**2
data_set['x2_sq'] = data_set['x2']**2
data_set['x1y'] = data_set['x1']*data_set['y']
data_set['x2y'] = data_set['x2']*data_set['y']
data_set['x1x2'] = data_set['x1']*data_set['x2']

n = len(data_set)

sum_X1_sq = data_set['x1_sq'].sum() - (data_set['x1'].sum()**2)/n
print(f'sum_X1_sq: {sum_X1_sq}')

sum_X2_sq = data_set['x2_sq'].sum() - (data_set['x2'].sum()**2)/n
print(f'sum_x2_sq: {sum_X2_sq}')

sum_X1y = data_set['x1y'].sum() - (data_set['x1'].sum()*data_set['y'].sum())/n
print(f'sum_X1y: {sum_X1y}')

sum_X2y = data_set['x2y'].sum() - (data_set['x2'].sum()*data_set['y'].sum())/n
print(f'sum_X2y: {sum_X2y}')

sum_X1X2 = data_set['x1x2'].sum() - (data_set['x1'].sum()*data_set['x2'].sum())/n
print(f'sum_X1X2: {sum_X1X2}')

mean_y = data_set['y'].mean()
mean_x1 = data_set['x1'].mean()
mean_x2 = data_set['x2'].mean()

n = len(data_set)

a1 = (sum_X2_sq*sum_X1y - sum_X1X2*sum_X2y)/(sum_X1_sq*sum_X2_sq - sum_X1X2**2)

a2 = (sum_X1_sq*sum_X2y - sum_X1X2*sum_X1y)/(sum_X1_sq*sum_X2_sq - sum_X1X2**2)

a0 = mean_y - a1*mean_x1 - a2*mean_x2

print(f'a0: {a0}, a1: {a1}, a2: {a2}')


import numpy as np

y_hat = a0 + a1*data_set['x1'] + a2*data_set['x2']

residuals = y_hat - data_set['y']

cost = np.dot(residuals, residuals)/(2*n)

print(f'cost: {cost}')