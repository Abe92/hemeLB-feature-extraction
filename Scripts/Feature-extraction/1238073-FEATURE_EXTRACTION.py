# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 23:13:47 2016
@author      : Aldy Rasyid Abe
@description : Feature Extraction
"""

# Feature Extraction with Filter Methods

import pandas as pd

# Load the data
file = "path/to/file.txt" # "path/to/file.csv"
names = ['step','grid_x','grid_y','grid_z',
        'velocity(0)','velocity(1)','velocity(2)',
        'magnitudes','pressure']
df = pd.read_csv(file, names=names)

"""
(1) Describing the data
"""
# Dimensions of data
dimensions = df.shape
print(dimensions)

# Attributes/Columns datatype
data_types = df.dtypes
print(data_types)

# Descriptive statistics
desc_stats = df.describe()
print(desc_stats)
#desc_stats.to_csv(r'path/to/file.csv', sep=',', mode='a') # Uncomment this line to save the output to flat file

"""
(2) Experimentation
"""
# Candidate 1 - find the difference between velocity vectors (0,1 and 2)
df['dVelocities'] = df['velocity(0)'] - df['velocity(1)'] - df['velocity(2)'].shift(-1)
df['dVelocities'].fillna(0, inplace=True)

# Candidate 2 - find the difference of magnitudes
df['dMagnitudes'] = df['magnitudes'].diff(-1)
df['dMagnitudes'].fillna(0, inplace=True)

# Print the result
#print(df)

# Correlation coefficient scores
pearson_correlation = df.corr(method='pearson')
print(pearson_correlation)
#pearson_correlation.to_csv(r'path/to/file.csv', sep=',', mode='a') # Uncomment this line to save the output to flat file

"""
(3) Feature extraction - dimensionality reduction
"""
data = {'grid_x':df['grid_x'],
        'grid_y':df['grid_y'],
        'grid_z':df['grid_z'],
        'pressure':df['pressure'],
        'dVelocities':df['dVelocities'],
        'dMagnitudes':df['dMagnitudes']}
        
new_df = pd.DataFrame(data, columns=['grid_x','grid_y','grid_z',
                                     'pressure','dVelocities',
                                     'dMagnitudes'])                                     
#print (new_df.to_string(index=False))
#new_df.to_csv(r'path/to/file.csv', header=True, index=None, sep=',', mode='a')

"""
(4) Feature extraction - experimentation
    (4.1) 'filter by the size of velocity differences
           between adjacent lattice sites'
"""
## 4.1
# Dimensions of data
new_dimensions = new_df.shape
print(new_dimensions)

# Attributes/Columns datatype
new_data_types = new_df.dtypes
print(new_data_types)

# Descriptive statistics
desc_stats_new_df = new_df.describe()
print(desc_stats_new_df)

# Sort the velocities difference by the highest
sort_df = new_df.sort_values(by=['dVelocities'], ascending=False)
#print(sort_df.to_string(index=False))

# Filter the size of velocity difference
filter_greater_df = new_df[new_df['dVelocities'] >= 0]
print(filter_greater_df.to_string(index=False))

filter_less_df = new_df[new_df['dVelocities'] <= 0]
print(filter_less_df.to_string(index=False))
