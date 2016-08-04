# -*- coding: utf-8 -*-
"""
Date created : 04 August 2016

@author      : Aldy Rasyid Abe

@description : Time steps conversion
"""

import numpy as np
import csv

#1
x = np.zeros([0,1])

#2
with open ('D:/Python/In/time_steps-and-pressure/hemeLB-time_steps.txt') as csvfile:
    file = csv.reader(csvfile)
    
    #3
    for row in file:
        x = np.vstack([x,[float(row[0])]])
      
#4
seconds = ((x[:,0])/1000) % 60
print(seconds)