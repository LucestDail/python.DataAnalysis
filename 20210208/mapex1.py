# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 08:30:32 2021

@author: myung

mapex1.py : map : 리스트의 각각의 요소를 변경함
"""
before = ["2021","02","08"]
print(type(before[0])) #문자열 
print(before)
#before의 요소 각각을 int 형변환한 후 다시 list 객체로 생성 
after = list(map(int,before))
print(type(after[0])) #int
print(after)
print(int("123"))