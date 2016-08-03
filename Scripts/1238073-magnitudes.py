# -*- coding: utf-8 -*-
"""
Date created: 03 August 2016

@author      : Aldy Rasyid Abe

@description : (1) Initialize an array with N columns.
               
               (2) Read a CSV file from a specific directory.
                   Store it on a variable.
               
               (3) Using for loops, read and store the contents of the file then
                   put it into a array then stack it in vertical sequence.
               
               (4) Calculate the velocity magnitudes
"""

import numpy as np
import csv

# 1
xyz = np.zeros([0,3])

# 2
with open ('D:/Python/In/ID-678528/678528-velocity-vector.txt') as csvfile:
    file = csv.reader(csvfile)
    
    # 3
    for row in file:
        xyz = np.vstack([xyz,[float(row[0]), float(row[1]), float(row[2])]])

#4
magnitudes = np.sqrt(xyz[:,0]*xyz[:,0] + xyz[:,1]*xyz[:,1] + xyz[:,2]*xyz[:,2])
print(magnitudes)