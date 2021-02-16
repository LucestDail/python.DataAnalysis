# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:22:20 2021

@author: myung

test1.py 

삼각형의 높이를  입력받은 후  삼각형을 출력하는 프로그램을 작성

삼각형의 높이를 입력하세요 : 5


    *
   **
  ***
 ****
*****

     
    *
   ***
  *****
 *******
*********

"""
row = int(input("삼각형의 높이를 입력하세요"))

for i in range(1,row+1) :
    print(" "*(row-i),end="")
    print("*"*i)
    
print()
for i in range(0,row+1) :
    print(" "*(row-i),end="")
    print("*"*(i*2-1))

print()
for i in range(row,0,-1) :
    print(" "*(row-i),end="")
    print("*"*i)

