# -*- coding: utf-8 -*-
"""
Date created : 15 August 2016
@author      : Aldy Rasyid Abe
@description : HemeLB-feature-extraction-manual_approach
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
- Requirements: 
(1) The latest Python (2.7 or 3.x)
(2) hemeLB xtr file
(3) hemeXtract --------------------------> You need this to convert the xtr file into flat file

-The program utilising the Pandas library.

-File types supported by the Pandas
(1) Flat files (CSV and delimited),
(2) Excel files,
(3) Databases and
(4) HDF5.

-The program primarily focused on the flat files type.

-Please consult to {http://pandas.pydata.org/pandas-docs/stable/io.html}
for more details of using other file types.
"""

## Load your file here
df = pd.read_csv('hemeLB-flat_file-name') # Flat files (CSV and delimited)

## List your column of the flat files here
time_step = df['step']

grid_X = df['X']
grid_Y = df['Y']
grid_Z = df['Z']

velocity0 = df['velocity(0)']
velocity1 = df['velocity(1)']
velocity2 = df['velocity(2)']

magnitude = df['magnitudes']  # I added this column manually after converted
                              # the file into CSV from text file
pressure = df['pressure']

# Dimensions of data
dimensions_of_data = df.shape
print(dimensions_of_data)          # Output ('number_of_rows', 'number_of_columns')

# Each attribute/column data type
datatype = df.dtypes
print(datatype)                    # Output: (column_name      datatype)

## Calculator
# (1) Converting the value of time from column step into seconds
seconds = (time_step*4.00E-06)
seconds.to_csv(r'file-output-name', header=None, index=None, sep=',', mode='a')    # save the conversion of time to file

# (2) Finding the magnitudes of the velocity vectors
magnitudes = np.sqrt(velocity0*velocity0 + velocity1*velocity1 + velocity2*velocity2)
magnitudes.to_csv(r'file-output-name', header=None, index=None, sep=',', mode='a') # save the calculation of magnitudes to file

## Descriptive statistics
all_columns = df.describe(percentiles=[.05, .25, .75, .95])
all_columns.to_csv(r'file-output-name', sep=' ', mode='a')
"""
Don't forget to add some comments here to describe the output of the file! --- 16th August 2016 @ 12:32 pm BST
"""

## Plotting
# (1) Regular plot
plt.plot('column-name1', 'column-name2', label='regular-plot-label', color='#0066cc')
plt.xlabel('x_axes-label')
plt.ylabel('y_axes-label')
plt.title('regular-plot-title')
plt.grid(True)
plt.legend()
plt.show()

# (2) Scatter plot
plt.scatter('column-name1', 'column-name2', label='regular-plot-label', color='#0066cc')
plt.xlabel('x_axes-label')
plt.ylabel('y_axes-label')
plt.title('regular-plot-title')
plt.grid(True)
plt.legend()
plt.show()

#  Correlation between attributes
pearson_correlation = df.corr(method='pearson')
pearson_correlation.to_csv(r'file-output-name', sep=' ', mode='a')
