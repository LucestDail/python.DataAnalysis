# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:07:04 2021

@author: myung
exam5.py : 삼각형의 높이를  입력받은 후  삼각형을 출력하는 프로그램을 작성

삼각형의 높이를 입력하세요 : 3
 
 *
 **
 *** 
 
 ***
 **
 *
 
"""
h = int(input("삼각형의 높이를 입력하세요 :"))
for i in range(1,h+1) :
    print("*"*i)
print()
for i in range(h,0,-1) :
    print("*"*i)
