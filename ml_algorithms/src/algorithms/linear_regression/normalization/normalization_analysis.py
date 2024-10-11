import os
import pandas as pd



data_path=os.path.join(os.path.dirname(__file__),'..', 'data_generation', 'data_1f.csv')

df_data = pd.read_csv(data_path, delimiter=',', index_col=False)

y_mean = df_data['y'].mean()
y_stddev = df_data['y'].std()


df_data['y'] = (df_data['y'] - y_mean) / y_stddev

print(df_data['y'].mean())
print(df_data['y'].std())


normalized_data_path = os.path.join(os.path.dirname(__file__),'..', 'data_generation', 'data_1f_norm.csv')

df_data.to_csv(normalized_data_path, header=True, index=False)
