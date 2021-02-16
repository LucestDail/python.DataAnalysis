# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:11:47 2021

@author: myung

tryex1.py : 예외 처리 예제
"""
mystr = "파이썬 공부 중입니다. 파이썬을 열심히 공부 합시다."
strpos= []
index = 0
'''
while True:
    index = mystr.find("파이썬",index)
    if index == -1 :
        break
    strpos.append(index)
    index += 1
'''
while True:
    try :
        index = mystr.index("파이썬",index)
        strpos.append(index)
        index += 1
    except :    
        break
print("파이썬 문자의 위치:",strpos,"문자의 갯수",len(strpos))