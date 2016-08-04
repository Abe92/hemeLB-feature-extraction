# -*- coding: utf-8 -*-
"""
Date created : 04 August 2016

@author      : Aldy Rasyid Abe

@description : Time steps conversion
"""

import numpy as np
import csv

#1
x = np.zeros([0,1])  # Replace '1' with the number of columns in your csv file

#2
with open ('your-csv-file-name') as csvfile:
    file = csv.reader(csvfile)
    
    #3
    for row in file:
        x = np.vstack([x,[float(row[0])]])
        
        """
        For more than 1 column:
        x = np.vstack([x,[float(row[0]), float(row[1]), ...(..)]])
        
        ! The number inside [float(row[number])] indicates the index number of columns.
        ! Remember that index number in computer start from 0
        """
      
#4
seconds = ((x[:,0])/1000) % 60
print(seconds)
