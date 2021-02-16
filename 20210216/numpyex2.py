# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 11:41:05 2021

@author: dhtmd
"""

import numpy as np

a = np.array([20,30,40,50])
b = np.arange(4)

print(a)
print(b)
print(a-b)
print(a**2)
print(a<35)

c = np.array([[1,1],[0,1]])
d = np.array([[2,0],[3,4]])
print(c+d)
print(np.linalg.inv(d))
#행렬곱(단순)
print(c*d)
# 일반적인 행렬 곱
print(c@d)
print(c.dot(d))

e = np.ones((2,3), dtype=int)
print(e)
print(3*e)

f = np.ones(3,dtype=np.int32)
g = np.linspace(0,np.pi,3)
print(f.dtype, ",", g.dtype)
h = f + g
print(h)
print(h.dtype)