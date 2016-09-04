# -*- coding: utf-8 -*-
"""
Date created : 27 August 2016
@author      : Aldy Rasyid Abe
@description : Data cleaning - remove Not-a-Number values
"""

import pandas as pd

df = pd.read_csv('path/to/file.csv')
rm_nan = df.dropna()
rm_nan.to_csv(r'path/to/file.csv', header=True, index=None, sep=',', mode='a')
