# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 13:49:52 2021

@author: dhtmd
"""

import numpy as np
x = np.arange(10)
print(x)
print(x[:5]) #0 -> 4
print(x[5:]) #5 -> 끝
print(x[4:7]) #4 - >6
print(x[::2]) # 2씩 증가
print(x[1::2]) #1 부터 2씩 증가
print(x[1:8:3]) # 1 -> 7 3씩 증가
print(x[::-1]) # 역순

print("0 ~ 9 난수 4x5 배열 생성")

#a = np.random.randint(0,10,(4,5))
a = np.random.randint(10,size=(4,5))
print(a)

# 2x3 부분 배열 출력
print(a[:2,:3])

# 모든행 한개씩 걸쳐서 열 조회
print(a[:,::2])

# 행과 열 모두 역으로 조회
print(a[::-1,::-1])

# 열만 역으로 조회
print(a[:,::-1])