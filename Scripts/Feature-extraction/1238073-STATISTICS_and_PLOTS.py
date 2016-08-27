# -*- coding: utf-8 -*-
"""
Date created : 27 August 2016
@author      : Aldy Rasyid Abe
@description : Descriptive statistics and plots
"""

import pandas as pd
import matplotlib.pyplot as plt

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
pressure = df['pressure']
magnitudes = df['magnitudes']

"""
                      STATISTICS
"""
## Dimensions of data
dimensions_of_data = df.shape
print(dimensions_of_data)          # Output ('number_of_rows', 'number_of_columns')

## Each attribute/column data type
datatype = df.dtypes
print(datatype)                    # Output: (column_name      datatype)

## Descriptive statistics
desc_stats = df.describe(percentiles=[.05, .25, .75, .95])
desc_stats.csv(r'path/to/file.csv', sep=' ', mode='a')

# Correlation between attributes
pearson_correlation = df.corr(method='pearson')
pearson_correlation.to_csv(r'path/to/file.csv', sep=' ', mode='a')

# Skewness
skewness = df.skew()
skewness.to_csv(r'path/to/file.csv', sep=' ', mode='a')

"""
                    PLOTS
"""
## Simple plots
plt.plot('column_name1', 'column_name2', label='simple-plot-label', color='#0066cc')
plt.xlabel('x-axes-label')
plt.ylabel('y-axes-label')
plt.title('simple-plot-title')
plt.grid(True)
plt.legend()
plt.savefig('path/to/figure.png')

## Scatter plot
plt.scatter('column_name1', 'column_name2', label='scatter-plot-label', color='#0066cc')
plt.xlabel('x-axes-label')
plt.ylabel('y-label-label')
plt.title('scatter-plot-title')
plt.grid(True)
plt.legend()
plt.savefig('path/to/figure.png')
