# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 13:58:04 2021

@author: dhtmd
"""

import operator
dic,list = {},[]
dic =  {"a" : "에이", "b" : "비", "c" : "씨", "d" : "디", "e" : "이"}
list = sorted(dic.items(), key=operator.itemgetter(0),reverse=True)
print(list)

list = sorted(dic.items(), key=operator.itemgetter(0),reverse=False)
print(list)

list = sorted(dic.items(), key=operator.itemgetter(1))
print(list)