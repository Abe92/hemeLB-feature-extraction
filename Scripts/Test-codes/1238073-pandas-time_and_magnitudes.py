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
pd.set_option('display.max_rows', 'rows_value')   # 'rows_value' should be adjusted to the number of rows from the csv file

# Source file
df = pd.read_csv('csv-file-name')

# Column names
column_name1 = df['column_name1']

column_name2 = df['column_name2']
column_name3 = df['column_name3']
column_name4 = df['column_name4']

# Converting raw time-step into seconds
seconds = (column_name1*4.00E-06)
seconds.to_csv(r'file-output-name', header=None, index=None, sep=',', mode='a')

# Calculating magnitudes
magnitudes = np.sqrt(column_name2*column_name2+column_name3*column_name3+column_name4*column_name4)
magnitudes.to_csv(r'file-output-name', header=None, index=None, sep=',', mode='a')
