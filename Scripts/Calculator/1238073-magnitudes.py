# -*- coding: utf-8 -*-
"""
Date created: 03 August 2016
@author      : Aldy Rasyid Abe
@description : Velocity magnitudes calculator
"""

import numpy as np
import csv

# 1
xyz = np.zeros([0,3]) # Replace '3' with the number of columns in your csv file

# 2
with open ('hemeLB-csv-file-name') as csvfile:
    file = csv.reader(csvfile)
    
    # 3
    for row in file:
        xyz = np.vstack([xyz,[float(row[0]), float(row[1]), float(row[2])]])
        
    """
        For more than 1 column:
        x = np.vstack([x,[float(row[0]), float(row[1]), ...(..)]])
        
        ! The number inside [float(row[number])] indicates the index number of columns.
        ! Remember that index number in computer start from 0
    """

#4
magnitudes = np.sqrt(xyz[:,0]*xyz[:,0] + xyz[:,1]*xyz[:,1] + xyz[:,2]*xyz[:,2])
print(magnitudes)
