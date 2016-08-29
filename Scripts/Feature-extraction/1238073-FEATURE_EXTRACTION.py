# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 19:58:38 2016
@author      : Aldy Rasyid Abe
@description : The manual Feature Extraction by differences
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

## Create the new dataframe from the dictionary            
df1 = pd.DataFrame(raw_data1, columns=['step','grid_x','grid_y','grid_z','magnitudes'])
#print (df1.to_string(index=False))

## Create new column and calculate the difference
#
# The new column will be use to store the results of the difference
df1['dMagnitudes'] = df.magnitudes.diff(-1) 
print(df1)                                  
                                              # The (-1) value within the diff function                      
                                              # is used to specify the location of new column.
                                              # (-1) means 'put this column after the last colum'
