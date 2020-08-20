import pandas as pd
from pandas import DataFrame
import os
import matplotlib.pyplot as plt

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'data\winequality-red.csv')

df = pd.read_csv(filename, sep=';')
# print(df.head())

df2 = df['chlorides']
# print(df2.head())

df3 = df[['free sulfur dioxide', 'total sulfur dioxide']]
# print(df3.head())


to_rename = {'fixed acidity':'fixed_acidity',
          'volatile acidity':'volatile_acidity',
          'citric acid':'citric_acid',
          'residual sugar':'residual_sugar',
          'free sulfur dioxide':'free_sulfur_dioxide',
          'total sulfur dioxide':'total_sulfur_dioxide'
          }

df.rename(columns=to_rename, inplace=True)
# print(df.head())

df4 = df[(df['residual_sugar'] > 10)]
# print(df4)

df['sulphur_dioxide_difference'] = df['total_sulfur_dioxide'] - df['free_sulfur_dioxide']
# print(df.head())

df[['total_sulfur_dioxide','free_sulfur_dioxide','sulphur_dioxide_difference']][200:300].plot()
# plt.show()


