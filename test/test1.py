# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 14:28:52 2021

@author: dhtmd
"""

height = int(input("삼각형의 높이를 입력하세요=>"))
for i in range(height,0,-1):
    print(" " * (height +1 - i),end="")
    print("*" * (2*i-1),end="")
    print(" " * (height + 1), end = "")
    print()