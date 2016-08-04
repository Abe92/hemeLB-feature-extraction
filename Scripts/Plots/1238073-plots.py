# -*- coding: utf-8 -*-
"""
Date created : 03 August 2016

@author      : Aldy Rasyid Abe

@description : Plots maker
"""

import matplotlib.pyplot as plt
import numpy as np
import csv

#1
xy = np.zeros([0,2]) # Replace '2' with the number of columns in your csv file

#2
with open ('your-csv-file-name') as csvfile:
    file = csv.reader(csvfile)
    
    #3
    for row in file:
        xy = np.vstack([xy, [float(row[0]), float(row[1])]])
        
#4 Scatter plot maker
plt.scatter(xy[:,0], xy[:,1], label='label') 
plt.xlabel('x-axes_label')
plt.ylabel('y-axes_label')
plt.title('title')
plt.legend()
plt.show()
