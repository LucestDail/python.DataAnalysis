# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:44:30 2021

@author: dhtmd
"""

def factorial(inputValue):
    returnValue = 1
    for i in range(1,inputValue+1):
        returnValue *= i
    return returnValue


def sigma(inputValue):
    returnValue = 0
    for i in range(0,inputValue+1):
        returnValue += i
    return returnValue


inputValue = int(input("value : "))
if(inputValue%2 == 0):
    print(factorial(inputValue))
else:
    print(sigma(inputValue))
