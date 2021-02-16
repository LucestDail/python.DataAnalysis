# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:56:10 2021

@author: myung

whileex1.py : while 구문 연습
"""
num=1
while num <= 5:
    print(num,end="")
    num +=1

print()
#for 구문으로 변경
for num in range(1,6) :
    print(num,end="")