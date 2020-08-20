'''
Generates the dataset for a noisy sensor having an exponential response
'''
from random import uniform, seed
from matplotlib import pyplot as plt
from pandas import DataFrame
from fuzzy_system.fuzzy_learning_helper import save_data

# generate functions
seed(42)
factor = 0.3
x = range(0,50,1)

y_clean = [(1.1**i) for i in x]
y = [(1.1**i) +  ( i * factor * uniform(-1,1))  for i in x]

# plot
fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(y_clean)
axes[1].plot(y)
axes[0].set_title('ideal sensor response')
axes[1].set_title('noisy sensor response')
plt.show()

# write in file
data = {
    'x': x,
    'Y': y
}
df = DataFrame(data)
save_data(df, "sensor_data.csv")

