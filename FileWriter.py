#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 19:42:36 2020

@author: oseunghyeon
"""

from operator import itemgetter
import sys
import glob
import os

myLetters = ['a','b','c','d']
maxIndex = len(myLetters)
outputFile = sys.argv[1]
filewriter = open(outputFile,'w')
for indexValue in range(len(myLetters)):
    if indexValue < (maxIndex-1):
        filewriter.write(myLetters[indexValue]+'\t')
    else:
        filewriter.write(myLetters[indexValue]+'\n')
filewriter.close()