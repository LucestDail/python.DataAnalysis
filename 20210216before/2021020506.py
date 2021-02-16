# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 11:51:41 2021

@author: dhtmd
"""

thing = {"a" : "A", "b" : "b", "c" : "C", "d" : "D", "e" : "E"}
for i in thing.keys():
    print(f"{i} => {thing[i]}")
    
keyValue = input("key 입력 : ")
if keyValue in thing:
    print(f"{keyValue} => {thing[keyValue]}")
else:
    print(f"{keyValue} 없")



try:
    print(f"{keyValue} : {thing[keyValue]}")
except:
    print(f"{keyValue} 없음")