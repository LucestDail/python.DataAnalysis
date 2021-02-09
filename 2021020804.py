# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 10:34:35 2021

@author: dhtmd
"""

def genFun(num):
    for i in range(10, num+10):
        yield i
        print(i, "return")

print(list(genFun(5)))

for data in genFun(5):
    print("main print : ", data)