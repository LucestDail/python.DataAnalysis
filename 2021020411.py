# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:05:34 2021

@author: dhtmd
"""

import random

rnum = random.randrange(1,100)
i = 1
while True:
    a = int(input("input : "))
    if a > rnum:
        print("down")
    elif a < rnum:
        print("up")
    else:
        print("right")
        break
    i = i + 1
print(f"{i} try")