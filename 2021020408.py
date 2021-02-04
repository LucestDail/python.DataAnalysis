# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:15:26 2021

@author: dhtmd
"""

target = int(input("값 입력 : "))
print(target)
sum = 0
evensum = 0
oddsum = 0
for i in range(0,target):
    sum = i + sum
    if(i%2 == 0):
        evensum = evensum + i
    elif(i%2 == 1):
        oddsum = oddsum + i
print(f"{target} 까지의 총합 : {sum}, 짝수합 : {evensum}, 홀수합 : {oddsum}")