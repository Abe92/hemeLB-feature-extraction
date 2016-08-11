# -*- coding: utf-8 -*-
"""
Date created : 11 August 2016
@author      : Aldy Rasyid Abe
@description : Plotting with pandas
"""

import pandas as pd
import matplotlib.pyplot as plt

## Pandas configuration - optional
#pd.set_option('display.height', 46198)
#pd.set_option('display.max_rows', 46198)

## Source file
df = pd.read_csv('D:/Dissertation for MSc 2016-17/1238073 - Final Report/Data/experiment/planeOutTopFirst.csv')

## Column names
time_step = df['step']

gridx = df['grid_x']
gridy = df['grid_y']
gridz = df['grid_z']

velocity0 = df['velocity(0)']
velocity1 = df['velocity(1)']
velocity2 = df['velocity(2)']

magnitude = df['magnitudes']

pressure = df['pressure']

## Plotting
#
# Regular plots - time_steps against magnitudes
plt.plot(time_step, pressure, label='lattice-Boltzmann simulation', color='#0066cc')
plt.xlabel('time-steps (s)')
plt.ylabel('pressure (Pa)')
plt.title('hemeLB \n source: planeOutTopFirst.xtr')
plt.legend()
plt.show()

# Scatter plot - time_steps against magnitudes
plt.scatter(magnitude, pressure, label='lattice-Boltzmann simulation', color='#0066cc')
plt.xlabel('magnitudes (m/s)')
plt.ylabel('pressure (Pa)')
plt.title('hemeLB \n source: planeOutTopFirst.xtr')
plt.legend()
plt.show()