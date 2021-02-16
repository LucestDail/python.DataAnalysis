# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:11:33 2021

@author: dhtmd
"""

import numpy as np
# 0~9 임의 수 10개 가진 배열 생성
x = np.random.randint(10,size=10)
x_sub = x[:2]
print(x)
print(x_sub)
x_sub[0] = 20 #부분 배열 변경하면 원본 배열도 변경됨
print(x)
print(x_sub)

#배열 복사
x_copy = x.copy()
x_copy[0] = 100
print(x)
print(x_copy)

#배열 재편성시 기존 배열과 재편성 배열의 요소가 같은 수여야 합니다
x2 = x.reshape(5,2)
print(x2)

#0 ~ 99 까지 임의의 수를 9개 배열 a 생성
# a 를 3x3 재편성 배열 b 생성
a = np.random.randint(100, size=9)
print(a)
b = a.reshape(3,3)
print(b)