# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 12:08:16 2021

touple practice

@author: dhtmd
"""

tpl = (10,20,30)
print(tpl)
#tpl.append(10)
list1 = list(tpl)
list1.append(40)
tpl = tuple(list1)
print(tpl)
print(f"len(tpl) : {len(tpl)}")
print(f"tpl[1:3] : {tpl[1:3]}")
print(f"tpl[:3] : {tpl[:3]}")
print(f"tpl[2:] : {tpl[2:]}")
print(f"tpl[::2] : {tpl[::2]}")
print(tpl[0],tpl[1],tpl[2])

a,b,c,d = tpl
print(a,b,c,d)