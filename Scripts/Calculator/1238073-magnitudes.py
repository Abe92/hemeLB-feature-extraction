# -*- coding: utf-8 -*-
"""
Date created: 03 August 2016

@author      : Aldy Rasyid Abe

@description : Velocity magnitudes calculator
"""

import numpy as np
import csv

# 1
xyz = np.zeros([0,3])

# 2
with open ('csv_file-name') as csvfile:
    file = csv.reader(csvfile)
    
    # 3
    for row in file:
        xyz = np.vstack([xyz,[float(row[0]), float(row[1]), float(row[2])]])

#4
magnitudes = np.sqrt(xyz[:,0]*xyz[:,0] + xyz[:,1]*xyz[:,1] + xyz[:,2]*xyz[:,2])
print(magnitudes)
