# -*- coding: utf-8 -*-
"""
Date created : 27 August 2016
@author      : Aldy Rasyid Abe
@description : Manual feature extraction with its building blocks
"""

import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

## Source file
df = pd.read_csv('hemeLB-flat-file_name')

## List of the original column names from the flat file
step = df['step']
gridx = df['grid_x']
gridy = df['grid_y']
gridz = df['grid_z']
velocity0 = df['velocity(0)']
velocity1 = df['velocity(1)']
velocity2 = df['velocity(2)']
pressure = df['pressure']

"""
                            Calculator
"""
# (1) Converting the dimensionless step value into step value with unit of seconds
time_step = (step * 4.00E-06)

#(2) Finding the magnitudes of the velocity vectors
magnitude = np.sqrt(velocity0*velocity0 + velocity1*velocity1 + velocity2*velocity2)

"""
                    Creating new data frame 
"""
# (1) Create a dictionary
# List all of the columns including its values
raw_data = {'step': time_step,
          'grid_x':gridx,
          'grid_y':gridy,
          'grid_z':gridz,
          'velocity(0)':velocity0,
          'velocity(1)':velocity1,
          'velocity(2)':velocity2,
          'pressure':pressure,
          'magnitudes':magnitude}

# (2) Create the new dataframe from the dictionary
new_df = pd.DataFrame(raw_data,columns = ['step','grid_x','grid_y','grid_z','velocity(0)','velocity(1)','velocity(2)','pressure','magnitudes'])

"""
            Transform the new dataframe into flat file (CSV)
"""
new_df.to_csv(r'new-flat-file-name', header=True, index=None, sep=',', mode='a')
