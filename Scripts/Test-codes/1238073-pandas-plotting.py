# -*- coding: utf-8 -*-
"""
Date created : 11 August 2016
@author      : Aldy Rasyid Abe
@description : Plotting with pandas
"""

import pandas as pd
import matplotlib.pyplot as plt

## Pandas configuration - optional
#pd.set_option('display.height', 46000)
#pd.set_option('display.max_rows', 46000)

## Source file
df = pd.read_csv('csv-file-name')

## Column names
column_name1 = df['column_name']

column_name2 = df['column_name']
column_name3 = df['column_name']
column_name4 = df['column_name']

column_name5 = df['column_name']

column_name6 = df['column_name']

## Plotting
#
# Regular plots
plt.plot(column_name1, column_name2, label='plot-label', color='#0066cc')
plt.xlabel('x_axes-label')
plt.ylabel('y_axes-label')
plt.title('plot-title')
plt.legend()
plt.show()

# Scatter plot
plt.scatter(column_name3, column_name4, label='plot-label', color='#0066cc')
plt.xlabel('x_axes-label')
plt.ylabel('y_axes-label')
plt.title('plot-title')
plt.legend()
plt.show()
