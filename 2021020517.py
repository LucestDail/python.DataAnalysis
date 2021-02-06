# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:12:15 2021

@author: dhtmd
"""

mystr = "파이썬 공부 중입니다. 파이썬 열심히 공부 합시다..."
strpos = []
index = 0
while True:
    try:
        index = mystr.index("파이썬",index)
        strpos.append(index)
        index += 1
    except:
        break
    
print("파이썬 문자의 위치 : ",strpos," 문자의 갯수 : ",len(strpos))