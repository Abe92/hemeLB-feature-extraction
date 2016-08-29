# -*- coding: utf-8 -*-
"""
Date created : 27 August 2016
@author      : Aldy Rasyid Abe
@description : Data cleaning - USABLE
@update      : (1) 28 August 2016, still bugged don't use it
               (2) 29 August 2016, FIX. It is now able to remove all white-spaces!
"""

import pandas as pd

df = pd.read_csv('path/to/file.csv')
df_no_missing = df.dropna()
df_no_missing.to_csv(r'path/to/file.csv', header=True, index=None, sep=',', mode='a')

#import fileinput
# Approach 1
#with open (r'path/to/file.csv') as f:
#    for line in f:
#        cleanedLine = line.rstrip()
#        if cleanedLine: # is not empty
#            print(cleanedLine)
#            
# Approach 2
#for line in fileinput.FileInput(r'path/to/file.csv', inplace=1): 
#    if line.rstrip('\n'):
#        print (line)
#
#"""
#Notes for Approach 2
#"""
# inplace=1,
# The file is moved to a backup file and standard output  
# is directed to the input file 
# (if a file of the same name as the backup file already exists, 
# it will be replaced silently)
