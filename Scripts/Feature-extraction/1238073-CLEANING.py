# -*- coding: utf-8 -*-
"""
Date created : 27 August 2016
@author      : Aldy Rasyid Abe
@description : Data cleaning - POSTPONED
"""

import fileinput

# Approach 1
with open (r'D:\\Python\In\csv\new_planeOutTopFirst.txt') as f:
    for line in f:
        cleanedLine = line.strip()
        if cleanedLine: # is not empty
            print(cleanedLine)
            
# Approach 2
for line in fileinput.FileInput(r'D:\\Python\In\csv\new_planeOutTopFirst.txt', inplace=1):
    if line.rstrip('\n'):
        print (line)