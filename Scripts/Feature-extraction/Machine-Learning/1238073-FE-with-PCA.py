# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 23:41:34 2016
@author: Aldy Rasyid Abe
@description: Feature Extraction machine learning with PCA
              *PCA - Principal Component Analysis, a linear dimensionality reduction
@credits: Jason Brownlee
          (http://machinelearningmastery.com/feature-selection-machine-learning-python/)
"""

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

## Load data set
data = pd.read_csv('path/to/file.csv')

## Convert it to numpy arrays
X = data.values

## Scaling the values
X = scale(X)
pca = PCA(n_components=number_of_columns)
pca.fit(X)

## The amount of variance that each principle components explains
var = pca.explained_variance_ratio_

## Cumulative variance explained
var1 = np.cumsum(np.round(pca.explained_variance_ratio_, decimals=4) *100)
print(var1)

## Plot the result - optional but quite beneficial
# The plotting snippet is yet to be perfected to clearly display the interesting component(s) of the data
plt.plot(var1)
plt.xlabel('Principal component')
plt.ylabel('Cumulative proportion of variance explained')
plt.title('Source: dataset-used')
plt.grid(True)
plt.legend()
plt.show()

## The componentsof the principal axes in feature space,
## representing the directions of maximum variance in the data
comp = pca.components_
print("Principal axes in feature space sorted by the explained_variance_", comp)

## The output of the comp = pca.components_
#[[  1.17288469e-02   4.93393183e-02   5.80570453e-02   5.16606096e-02
#    4.98622388e-01  -3.43274110e-01  -5.00284770e-01  -5.00142755e-01
#   -3.52845007e-01]
# [  6.56161923e-04   6.92608382e-01   8.46725545e-02   7.00097336e-01
#   -2.95440072e-02  -6.87945441e-02   4.37424960e-02   4.18713555e-02
#    1.17112434e-01]
# [ -1.61868747e-02   1.47221446e-01  -7.94437936e-01   5.24924920e-02
#    1.04966797e-01   5.21999013e-01  -8.84164104e-02  -8.79894656e-02
#   -2.12405577e-01]
# [  9.97184007e-01  -4.78816377e-04  -3.18338410e-02  -5.45345051e-03
#    1.09219113e-02   4.24862257e-03  -1.34371374e-02  -5.41026617e-03
#    6.50655509e-02]
# [ -7.10000854e-02  -1.44148518e-02  -3.36381911e-01  -8.47529439e-02
#    1.44216018e-01  -2.40237962e-01  -1.72473296e-01  -1.74781377e-01
#    8.57675488e-01]
# [  1.19423500e-02  -1.53759996e-02  -4.90062496e-01   1.32602285e-02
#   -2.46439681e-01  -7.37549006e-01   1.97665582e-01   1.99935618e-01
#   -2.74821559e-01]]

## The data used for this experiment is planeOutTopFirst
