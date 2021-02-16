# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 13:48:39 2021

@author: dhtmd
"""

i, j = 0,0
for i in range(2,10):
    for j in range(2,10):
        print(f"{j} X {i} = {i*j}", end="\t")
        if(j == 9):
            print()