# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 15:39:59 2021

@author: dhtmd
"""

def multi(v1,v2):
    list = []
    res1 = v1+v2
    res2 = v1-v2
    list.append(res1)
    list.append(res2)
    return list

def multiParam(* p):
    result = 0
    for i in p:
        result += i
    return result

hap,sub = 0,0
list = multi(100,200)
hap = list[0]
sub = list[1]
print(f"multi return : {hap}, {sub}")
print(f"multiParam() : {multiParam()}")
print(f"multiParam(10) : {multiParam(10)}")
print(f"multiParam(10,20) : {multiParam(10,20)}")
print(f"multiParam(10,20,30) : {multiParam(10,20,30)}")