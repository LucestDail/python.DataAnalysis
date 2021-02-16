# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 13:36:11 2021

@author: dhtmd
"""
import numpy as np

print("0 부터 9 까지 정수 10개의 요소를 0으로 채운 배열 생성")
a = np.zeros(10,dtype=int)
print(a)

print("3행 5열의 요소를 1으로 채운 배열 생성")
b = np.ones((3,5))
print(b)

print("0 - 20 까지의 수를 2씩 증가시킨 값을 배열 생성")
c = np.arange(0,21,2)
print(c)

print("0과 1 사이의 일정한 각격의 5개의 값을 가진 배열 생성")
d = np.linspace(0,1,5)
print(d)

print("3행 5열짜리 배열 값을 3.14로 채우기")
e = np.full((3,5),3.14)
print(e)