# -*- coding: utf-8 -*-
"""
Date created : 12 August 2016
@author      : Aldy Rasyid Abe
@description : Statistics
"""

import pandas as pd

## Pandas configuration
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

## Descriptive statistics

# Time-steps
time_summary = time_step.describe(percentiles=[.05, .25, .75, .95])
print("Time-steps","\n",time_summary)

# Lattice point X
x_summary = gridx.describe(percentiles=[.05, .25, .75, .95])
print("Lattice-point X","\n",x_summary)

# Lattice point Y
y_summary = gridy.describe(percentiles=[.05, .25, .75, .95])
print("Lattice-point Y","\n",y_summary)

# Lattice point Z
z_summary = gridz.describe(percentiles=[.05, .25, .75, .95])
print("Lattice-point Z","\n",z_summary)

# Magnitudes
magnitude_summary = magnitude.describe(percentiles=[.05, .25, .75, .95])
print("Magnitudes","\n",magnitude_summary)

# Pressure
pressure_summary = pressure.describe(percentiles=[.05, .25, .75, .95])
print("Pressure","\n",pressure_summary)