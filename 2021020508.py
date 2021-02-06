# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 13:47:40 2021

set 집합 클래스

@author: dhtmd
"""

set1 = {1,2,3,4,5}

print(set1)

set2 = {1,2,3,4,5,1,2,3,4,5}

print(set2)

set3 = {5,6,7,8}

print(f"set1 & set3 : {set1 & set3}")
print(f"set1.intersection(set3) : {set1.intersection(set3)}")
print(f"set1|set3 : {set1|set3}")
print(f"set1.union(set3) : {set1.union(set3)}")