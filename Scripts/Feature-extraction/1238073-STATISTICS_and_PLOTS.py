# -*- coding: utf-8 -*-
"""
Date created : 27 August 2016
@author      : Aldy Rasyid Abe
@description : Descriptive statistics and plots
"""

import pandas as pd
import matplotlib.pyplot as plt

## Source file
df = pd.read_csv('path/to/file.csv')      # df = pd.read_csv('path/to/file.txt')

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
                STATISTICS RELATED CODES
"""
## Dimensions of data
def dimension(data):
    dimensions_of_data = data.shape
    print(dimensions_of_data)          # Output ('number_of_rows', 'number_of_columns')

## Each attribute/column data type
def datatypes(data):
    datatype = df.dtypes
    print(datatype)                    # Output: (column_name      datatype)

## Descriptive statistics
def desc_statistics(data):
    desc_stats = data.describe(percentiles=[.05, .25, .75, .95])
    print(desc_stats)

# Correlation between attributes
def pearson_correlation(data):
    correlation = data.corr(method='pearson')
    print(correlation)

# Skewness
def skewness(data):
    skewness = data.skew()
    print(skewness)

"""
                PLOT CODES to make FIGURES
"""
## Simple plots
plt.plot(column_1, column_2, label='simple-plot-label', color='#0066cc')
plt.xlabel('x-axes-label')
plt.ylabel('y-axes-label')
plt.title('simple-plot-title')
plt.grid(True)
plt.legend()
plt.show()
#plt.savefig('path/to/figure.png')

## Scatter plot
plt.scatter(column_1, column_2, label='scatter-plot-label', color='#0066cc')
plt.xlabel('x-axes-label')
plt.ylabel('y-axes-label')
plt.title('scatter-plot-title')
plt.grid(True)
plt.legend()
plt.show()
#plt.savefig('path/to/figure.png')
