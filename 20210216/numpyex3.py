# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 12:06:58 2021

@author: dhtmd
"""

import numpy as np

a = np.arange(12).reshape(3,4)
print("a : ",a)
print("sumaxis0 : ",a.sum(axis=0)) #0 -> 컬럼 기준
print("sumaxis1 : ",a.sum(axis=1))

print("maxaxis1 : ",a.max(axis=1)) #1 -> 행 기준
print("maxaxis0 : ",a.max(axis=0))
print("minaxis1 : ",a.min(axis=1))
print("minaxis0 : ",a.min(axis=0))
print("cumsumaxis1 : ",a.cumsum(axis=1))
print("cumsumaxis0 : ",a.cumsum(axis=0))
b = np.arange(3)
print(b)
print(np.exp(b))
print(np.sqrt(b))
c = np.array([2,-1,4])
print(c)
print(b+c)
print(np.add(b,c))

# 평균0, 표준편차1, 정규분포 (3x3) 생성
d = np.random.normal(0,1,(3,3))
print(d)

e = np.random.randint(0,10,(3,3))
print(e)