# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:12:28 2021

삼각형의 높이를 입력받은 후 삼각형을 출력하는 프로그램 작성

@author: dhtmd
"""

height = int(input("삼각형의 높이를 입력하세요 : "))
for i in range(0,height+1):
    print(" " * (height +1 - i),end="")
    print("*" * i,end="")
    print()
    
    
    
    
for i in range(0,height+1):
    print(" " * (height +1 - i),end="")
    print("*" * (2*i-1),end="")
    print(" " * (height + 1), end = "")
    print()