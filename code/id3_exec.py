'''
id3_exe.py
execution of ID3 example
'''
import os
import pandas as pd
import numpy as np
from id3 import ID3Classifier

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DF = pd.read_csv(DIR_PATH + '\\weather.csv')
df_copy = DF.copy()

#
# preprocessing
#

# discretize the TEMP attriibute
df_copy.loc[(DF['TEMP'] <= 69), 'TEMP'] = 'Cold'
df_copy.loc[(DF['TEMP'] > 69), 'TEMP'] = 'Medium'
df_copy.loc[(DF['TEMP'] >= 79), 'TEMP'] = 'Hot'

# discretize the HUMIDITY attriibute
df_copy.loc[(DF['HUMIDITY'] <= 80), 'HUMIDITY'] = 'Normal'
df_copy.loc[(DF['HUMIDITY'] > 80), 'HUMIDITY'] = 'High'

# remove the DAY column
df_copy.drop(columns=['DAY'], axis=1, inplace=True)

RESULTS = np.array(df_copy['PLAY'])
df_copy.drop('PLAY', axis=1, inplace=True)

NODE_NAMES = list(df_copy.columns.values)
NODE = np.array(df_copy[NODE_NAMES])


classifier = ID3Classifier()
classifier.id3_compute(NODE_NAMES, NODE, RESULTS)
classifier.display_tree()

case = {'WEATHER': 'Sunny','TEMP':'Cold','HUMIDITY':'High','WIND':'Weak'}
result = classifier.infer(case)
print('Result with', case, 'is: ', result)