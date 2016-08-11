# -*- coding: utf-8 -*-
"""
Date created : 11 August 2016

@author      : Aldy Rasyid Abe

@description : Multi-purpose script with pandas
"""

import pandas as pd
import numpy as np

pd.set_option('display.height', 46198)
pd.set_option('display.max_rows', 46198) 

# Source file
df = pd.read_csv('D:/Dissertation for MSc 2016-17/hemeXtract - MSc/xtr to txt/planeOutTopFirst/planeOutTopFirst.csv')

# Column names
time_step = df['step']

gridx = df['grid_x']
gridy = df['grid_y']
gridz = df['grid_z']

velocity0 = df['velocity(0)']
velocity1 = df['velocity(1)']
velocity2 = df['velocity(2)']

magnitude = df['magnitudes']

pressure = df['pressure']

# Converting raw time-step into seconds
seconds = (time_step*4.00E-06)
seconds = str(seconds)

# Calculating magnitudes
magnitudes = np.sqrt(velocity0*velocity0+velocity1*velocity1+velocity2*velocity2)
magnitudes = str(magnitudes)

# Print the results
print(seconds)
print(magnitudes)

## Seconds
#with open("D:\\Python\\In\\csv\\time-steps.txt", 'w') as time:    
#        for item in seconds:
#            time.write(seconds)
#
## Magnitudes
#with open("D:\\Python\\In\\csv\\magnitudes.txt", 'w') as magnitude:    
#        for item in magnitudes:
#            magnitude.write(magnitudes)