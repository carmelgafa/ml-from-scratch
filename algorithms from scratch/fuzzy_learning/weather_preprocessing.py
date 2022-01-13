import pandas as pd
from pandas import DataFrame
import os
import matplotlib.pyplot as plt
import numpy as np
import math

DATA_PATH = os.path.join(os.path.dirname( __file__ ), 'data')

def load_data(filename, data_path=DATA_PATH, separator=','):
	csv_path = os.path.join(data_path, filename)
	return pd.read_csv(csv_path, sep=separator)

def save_data(data_frame, filename, data_path=DATA_PATH):
	csv_path = os.path.join(data_path, filename)
	return data_frame.to_csv(csv_path, float_format='%.3f', index=False)

def weather_dataset_preprocess():

    data_n = load_data ('weatherHistory.csv')

    # get month from date
    data_n.loc[:, 'DateTime'] = pd.to_datetime(data_n['Formatted Date'], utc=True)
    data_n['Month'] = data_n['DateTime'].dt.month

    data_n = data_n.drop(columns=[
    'Formatted Date',
    'DateTime',
    'Summary',
    'Precip Type',
    'Apparent Temperature (C)',
    'Loud Cover',
    'Daily Summary',
    "Wind Bearing (degrees)",
    "Visibility (km)",
    "Pressure (millibars)",
    "Wind Speed (km/h)",
    ])

    data_n = data_n.rename(columns={
        "Temperature (C)":"Temperature",
        # "Wind Speed (km/h)": "Wind Speed",
        # "Wind Bearing (degrees)":"Wind Bearing",
        # "Visibility (km)":"Visibility",
        # "Pressure (millibars)":"Pressure"
    })

    save_data(data_n,'weatherHistory_adj.csv')

def create_testing_sample():

    df = load_data('weatherHistory_adj.csv')
    df_ret = df.head(1000)
    save_data(df_ret,'weatherHistory_adj_test.csv')

if __name__ == "__main__":
    weather_dataset_preprocess()
    create_testing_sample()