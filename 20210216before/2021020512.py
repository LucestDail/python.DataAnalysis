# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:54:20 2021

@author: dhtmd
"""

def getSum(target):
    return sum(target)

def getMean(target):
    if(len(target) == 0):
        return 0
    else:
        return sum(target) / len(target)


list = [2,3,3,4,4,5,5,6,6,8]
print(f"getSum(list) : {getSum(list)}")
print(f"getMean(list) : {getMean(list)}")

list = []
print(f"getSum(list) : {getSum(list)}")
print(f"getMean(list) : {getMean(list)}")

list = (2,3,3,4,4,5,5,6,6,7,7)
print(f"getSum(list) : {getSum(list)}")
print(f"getMean(list) : {getMean(list)}")