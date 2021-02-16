# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 08:30:32 2021

@author: myung

yieldex1.py : 함수의 종료 없이 ,yield로 값 리턴
"""

def genFun(num) :
    for i in range(10, num + 10) :
        yield i  #i변수의 값을 전달. 리턴하지 않음.
        print(i, "값 반환")

        
print(list(genFun(5)))

for data in genFun(5) :
    print("main에서 출력 : " , data)
