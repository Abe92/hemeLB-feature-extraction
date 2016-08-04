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
xy = np.zeros([0,2])

#2
with open ('D:/Python/In/time_steps-and-pressure/time_steps-in_seconds-and-pressures.txt') as csvfile:
    file = csv.reader(csvfile)
    
    #3
    for row in file:
        xy = np.vstack([xy, [float(row[0]), float(row[1])]])
        
#4
plt.scatter(xy[:,0], xy[:,1], label='something')
plt.xlabel('timesteps (s)')
plt.ylabel('mean pressure (Pa)')
plt.title('hemeLB raw file \n 300 timesteps and mean pressure of the example file')
plt.legend()
plt.show()