# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 15:51:10 2021

@author: myung

lambdaex1.py : 람다식으로 함수 구현 
"""
def hap(num1,num2) :
    res = num1 + num2
    return res

print(hap(10,20))

hap1=lambda num1,num2:num1+num2  #람다식으로 작성된 함수 
print(hap1(10,20))

#람다 방식으로 곱셈 출력하기
mul=lambda num1,num2:num1*num2  #람다식으로 작성된 함수 
print(mul(10,20)) #200

#매개변수의 기본값 설정하기
hap2 = lambda num1=0,num2=1:num1+num2
print(hap2())  #1
print(hap2(100))  #num1=100, num2=1 앞자리의 매개변수로 설정됨.
print(hap2(100,200))