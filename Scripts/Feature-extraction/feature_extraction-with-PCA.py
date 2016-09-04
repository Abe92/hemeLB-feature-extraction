# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 23:41:34 2016
@author: Aldy Rasyid Abe
@description : Feature Extraction machine learning with PCA
               *PCA - Principal Component Analysis, a linear dimensionality reduction
"""

import pandas as pd
from sklearn.decomposition import PCA

## load data
file = "path/to/file.txt"
names = ['step',
         'grid_x',
         'grid_y',
         'grid_z',
         'velocity(0)',
         'velocity(1)',
         'velocity(2)',
         'magnitudes',
         'pressure']
df = pd.read_csv(file, names=names)
array = df.values
X = array[:,0:8]
Y = array[:,8]

## feature extraction
pca = PCA(n_components=3)
fit = pca.fit(X)

## summarize components
print("Explained Variance: ", fit.explained_variance_ratio_) 
print(fit.components_)
