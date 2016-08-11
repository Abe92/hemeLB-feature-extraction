# -*- coding: utf-8 -*-
"""
Date created : 11 August 2016
@author      : Aldy Rasyid Abe
@description : Multi-purpose script with pandas
"""

import pandas as pd
import numpy as np

# Pandas configuration
pd.set_option('display.height', 'height_value')
pd.set_option('display.max_rows', 'rows_value') 

# Source file
df = pd.read_csv('csv-file-name')

# Column names
column_name1 = df['column_name1']

column_name2 = df['column_name2']
column_name3 = df['column_name3']
column_name4 = df['column_name4']

# Converting raw time-step into seconds
seconds = (column_name1*4.00E-06)
seconds = str(seconds)          # optional, but useful if you want to save the output to text file

# Calculating magnitudes
magnitudes = np.sqrt(column_name2*column_name2+column_name3*column_name3+column_name4*column_name4)
magnitudes = str(magnitudes)    # optional, but useful if you want to save the output to text file

# Print the results
print(seconds)
print(magnitudes)

# Seconds
#with open("D:\\Python\\In\\csv\\time-steps.txt", 'w') as time:    
#        for item in seconds:
#            time.write(seconds)
#
# Magnitudes
#with open("D:\\Python\\In\\csv\\magnitudes.txt", 'w') as magnitude:    
#        for item in magnitudes:
#            magnitude.write(magnitudes)
