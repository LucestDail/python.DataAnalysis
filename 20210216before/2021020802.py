# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 10:03:33 2021

@author: dhtmd
"""

try:
    a=[1,2]
    print(a[1])
    4/1
    b=int("a")
except (ZeroDivisionError, IndexError) as e:
    print(e)
except ValueError :
    print("정수값만 가능합니다")