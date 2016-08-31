# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 19:58:38 2016
@author      : Aldy Rasyid Abe
@description : The manual Feature Extraction grouped by the difference of column(s)
"""

import pandas as pd

## Source file
df = pd.read_csv('path/to/file.csv')

## List of the column names from the flat file
step = df['step']
gridx = df['grid_x']
gridy = df['grid_y']
gridz = df['grid_z']
velocity0 = df['velocity(0)']
velocity1 = df['velocity(1)']
velocity2 = df['velocity(2)']
magnitudes = df['magnitudes']
pressure = df['pressure']

"""
                Find magnitudes difference
"""
## Create a dictionary
#
# List all of the columns including its values
raw_data1 = {'step':step,
            'grid_x':gridx,
            'grid_y':gridy,
            'grid_z':gridz,
            'magnitudes':magnitudes}

## Create a new dataframe from the dictionary            
df1 = pd.DataFrame(raw_data1, columns=['step','grid_x','grid_y','grid_z','magnitudes'])

## Create new column and calculate the difference
#
# The new column will be use to store the results of the difference
df1['dMagnitudes'] = df.magnitudes.diff(-1)     # (-1) means 'put this column after the last column'
                                              
"""
                Find velocity vectors difference
"""
## Create a dictionary
#
# List all of the columns including its values
raw_data2 = {'step':step,
            'grid_x':gridx,
            'grid_y':gridy,
            'grid_z':gridz,
            'velocity(0)':velocity0,
            'velocity(1)':velocity1,
            'velocity(2)':velocity2,
            'pressure':pressure}
            
## Create a new dataframe from the dictionary
df2 = pd.DataFrame(raw_data2,columns=['step','grid_x','grid_y','grid_z',
                                      'velocity(0)','velocity(1)','velocity(2)',
                                      'pressure'])
                                      
## Create new column and calculate the difference
#
# The new column will be use to store the results of the difference
df2['dVelocity'] = df2['velocity(0)'] - df2['velocity(1)'] - df2['velocity(2)'].shift(-1) # (-1) means 'put this column 
                                                                                          # after the last column'

"""
                Save into flat file
"""
## Magnitudes difference - save into a file 
df1.to_csv(r'path/to/file.csv', header=True, index=None, sep=',', mode='a')

## Velocity vectors - save into a file 
df2.to_csv(r'path/to/file.csv', header=True, index=None, sep=',', mode='a')

"""
                Descriptive Statistics
"""
## Magnitudes
mag_desc_stats = df1.describe()
print(mag_desc_stats)                   # Quartiles will return NaN

## Velocity vectors
vel_desc_stats = df2.describe()
print(vel_desc_stats)                   # Quartiles will return NaN
