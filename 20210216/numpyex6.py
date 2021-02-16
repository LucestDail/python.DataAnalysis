# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:44:15 2021

@author: dhtmd
배열의 연결 및 분할
"""

import numpy as np
x = np.array([[1,2,3],[4,5,6]])
y = np.array([[3,2,1],[6,5,4]])
print(x)
print(y)

print(np.concatenate([x,y],axis=0)) #행으로 연결
print(np.concatenate([x,y],axis=1)) #열으로 연결

x = np.array([[1,2,3],[4,5,6]])
y = np.array([[3,2,1],[6,5,4],[3,2,1]])
z = np.array([[7],[10]])
print(x)
print(y)
print(z)

print(np.vstack([x,y]))
print(np.hstack([x,z]))

x = np.arange(16).reshape((4,4))
print(x)
upper, lower = np.vsplit(x,[2])
print(upper)
print(lower)

left, right = np.hsplit(x,[2])
print(left)
print(right)