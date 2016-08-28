# -*- coding: utf-8 -*-
"""
Date created : 27 August 2016
@author      : Aldy Rasyid Abe
@description : Data cleaning - POSTPONED
@update      : 28 August 2016, still bugged don't use it
"""

import fileinput

# Approach 1
with open (r'path/to/file.csv') as f:
    for line in f:
        cleanedLine = line.strip()
        if cleanedLine: # is not empty
            print(cleanedLine)
            
# Approach 2
for line in fileinput.FileInput(r'path/to/file.csv', inplace=1): 
    if line.rstrip('\n'):
        print (line)

"""
Notes for Approach 2
"""
# inplace=1,
# The file is moved to a backup file and standard output  
# is directed to the input file 
# (if a file of the same name as the backup file already exists, 
# it will be replaced silently)
