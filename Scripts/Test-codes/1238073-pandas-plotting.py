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
column_name0 = df['column_name']

column_name1 = df['column_name']
column_name2 = df['column_name']
column_name3 = df['column_name']

column_name4 = df['column_name']

column_name5 = df['column_name']

## Plotting
#
# Regular plots
plt.plot(column_name0, column_name1, label='plot-label', color='#0066cc')
plt.xlabel('x_axes-label')
plt.ylabel('y_axes-label')
plt.title('plot-title')
plt.grid(True)
plt.legend()
plt.show()

# Scatter plot
plt.scatter(column_name2, column_name3, label='plot-label', color='#0066cc')
plt.xlabel('x_axes-label')
plt.ylabel('y_axes-label')
plt.title('plot-title')
plt.grid(True)
plt.legend()
plt.show()

# Historgram
plt.hist(column_name4,  color='#0066cc')
plt.xlabel('x_axes-label')
plt.ylabel('y_axes-label')
plt.title('')
plt.grid(True)
plt.show()

# Boxplot
data = [column_name5, column_name0]
plt.boxplot(data)
plt.xticks([1,2], ['x1-label', 'x2-label'])
plt.grid(True)
plt.show()
