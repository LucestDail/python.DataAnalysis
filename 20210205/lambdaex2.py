# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:01:04 2021

@author: myung

lambdaex2.py : 람다식을 이용한 리스트 처리
"""

myList=[1,2,3,4,5]

def add10(num):
    return num+10

for i in range(len(myList)) :
    myList[i] = add10(myList[i])
print(myList) 

add=lambda num:num+10
for i in range(len(myList)) :
#    myList[i] = add(myList[i])
    myList[i] = (lambda num:num+10)(myList[i])
print(myList) 
    