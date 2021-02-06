# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 15:52:59 2021

@author: dhtmd
"""

def hap(num1, num2):
    res = num1 + num2
    return res

print(hap(10,20))

hap1 = lambda num1,num2:num1+num2
print(hap1(10,20))

mul = lambda num1,num2:num1*num2
print(mul(10,20))

hap2 = lambda num1=0,num2=1:num1+num2
print(hap2())
print(hap2(100))
print(hap2(100,200))