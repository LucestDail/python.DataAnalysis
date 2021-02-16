# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 10:41:12 2021

@author: dhtmd
"""

import numpy as np
a = np.arange(16).reshape(4,4)
#np.arrange(16) : 0 ~ 15 까지의 수
#reshape(4,4) : 4행 4열 배열로 설정
print(a)
print(a.shape) #(4,4)
print(a.ndim) #2차원
print(a.dtype.name) #a 배열 요소들의 자료형
print(a.itemsize) #a 배열 요소의 크기
print(a.size) #a 배열 요소들 갯수
print(type(a)) #a 배열 타입 : numpy.ndarray
b = np.array([6,7,8])
print(b)
print(type(b))
print(b.dtype)

#배열
c = np.array([1.2, 3.5, 5.1])
print(c.dtype)

#튜플
d= np.array([(1.5,2,3),(4,5,6)])
print(d)
print(d.dtype)

#리스트
e = np.array([[1,2],[3,4]])
print(e)
print(e.dtype)
print(e.size)
e = np.array([[1,2],[3,4]], dtype=complex)
print(e.dtype)
print(e.size)

#3x4 2차원배열 생성, 0 초기화(zeros)
f = np.zeros((3,4))
print(f)
print(f.dtype)

#3차원 배열 생성
g = np.ones((2,3,4))
print(g)
print(g.size)
print(g.dtype)

#3차원 배열 정수형으로 생성
g = np.ones((2,3,4),dtype=np.int16)
print(g)
print(g.size)
print(g.dtype)

print()
#arrange 함수 이용 10~29 까지 수중 5의 배수로만 이루어진 배열
"""
input_array = []
for i in range(10,29):
    if i%5 == 0:
        input_array.append(i)
        
h = np.array(input_array)
"""
h = np.arange(10,30,5)
print(h)
print(h.dtype)

#arange(i,j,k) : i 부터 j 까지 k 단위로 증가하는 배열 생성
i = np.arange(0,2,0.3)
print(i)
print(i.dtype)

#arange(i,j,k) : i 부터 j 까지 k 등분
j = np.linspace(0,2,9)
print(j)
print(j.dtype)

print(np.pi)
#0 ~ 2pi 수를 100개 가져오기
k = np.linspace(0,2*np.pi,100)
print(k)

print(np.arange(10000).reshape(100,100))