# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 23:13:47 2016
@author      : Aldy Rasyid Abe
@description : 'Manual' Feature Extraction
"""

import pandas as pd

# Load the data
file = "D:/Python/In/csv/m_l.txt"
names = ['step','grid_x','grid_y','grid_z',
        'velocity(0)','velocity(1)','velocity(2)',
        'magnitudes','pressure']
df = pd.read_csv(file, names=names)

"""
(1) List of functions to describe data
"""
# Dimensions of data
def dimension(data):
    dimensions = data.shape
    print(dimensions)

# Attributes/Columns datatype
def data_types(data):
    data_types = data.dtypes
    print(data_types)

# Descriptive statistics
def desc_stats(data):
    desc_stats = data.describe()
    print(desc_stats)
    #desc_stats.to_csv(r'D:/Python/In/csv/featureXtraction_stats.csv', sep=',', mode='a') # Uncomment this line to save the output to flat file

# Correlation coefficient scores
def pearson_correlation(data):
    pearson_correlation = data.corr(method='pearson')
    print(pearson_correlation)
    #pearson_correlation.to_csv(r'D:/Python/In/csv/featureXtraction_corr', sep=',', mode='a') # Uncomment this line to save the output to flat file

"""
(2) Feature extraction - create a new variable from existing variables
"""
# Candidate 1 - find the difference between velocity vectors (2,1 and 0)
df['dVelocities'] = df['velocity(2)'] - df['velocity(1)'] - df['velocity(0)'].shift(-1)
df['dVelocities'].fillna(0, inplace=True)

# Candidate 2 - find the difference of magnitudes
df['dMagnitudes'] = df['magnitudes'].diff(-1)
df['dMagnitudes'].fillna(0, inplace=True)

# Print the result
#print(df)

"""
(3) Feature extraction - new dataset
"""
data = {'step':df['step'],
        'grid_x':df['grid_x'],
        'grid_y':df['grid_y'],
        'grid_z':df['grid_z'],
        'dVelocities':df['dVelocities'],
        'dMagnitudes':df['dMagnitudes'],
        'pressure':df['pressure']}
        
new_df = pd.DataFrame(data, columns=['step',
                                     'grid_x',
                                     'grid_y',
                                     'grid_z',
                                     'dVelocities',
                                     'dMagnitudes',
                                     'pressure'])

desc_stats(new_df)
pearson_correlation(new_df)

#print(new_df.head(5))
#print (new_df.to_string(index=False))
#new_df.to_csv(r'D:/Python/In/csv/featureXtraction.csv', header=True, index=None, sep=',', mode='a')

"""
(4) Feature extraction - experimentation
    (4.1) 'filter by the size of velocity differences
           between adjacent lattice sites'
"""
## 4.1
## Sort the velocities difference by the highest
sort_df = new_df.sort_values(by=['dVelocities'], ascending=False)
#print(sort_df.to_string(index=False))

## Filter by the size of velocity difference
filter_greater_vel = new_df[new_df['dVelocities'] >= 0.005]
filter_less_vel = new_df[new_df['dVelocities'] <= 0.005]
#print(filter_greater_vel.head(5))
#print(filter_less_vel.head(5))

## Filter by the size of magnitude difference
filter_greater_mag = new_df[new_df['dMagnitudes'] >= 0.005]
filter_less_mag = new_df[new_df['dMagnitudes'] <= 0.005]
#print(filter_greater_mag.head(5))
#print(filter_less_mag.head(5))
