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

# Correlation coefficient scores
pearson_correlation = df.corr(method='pearson')
print(pearson_correlation)
