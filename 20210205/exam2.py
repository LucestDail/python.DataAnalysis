# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:19:17 2021

@author: myung

exam2.py : 간단한 계산기 함수 
"""
def calc(v1,v2,op):
    result = 0
    if op =='+' :
        result = v1 + v2
    elif op=='-' :   
        result = v1 - v2
    elif op=='*' :   
        result = v1 * v2
    elif op=='/' :   
        result = v1 / v2
    return result

oper = input("연산자를 선택하세요:(+,-,*,/) =>")
var1 = int(input("첫번째 수=>"))
var2 = int(input("두번째 수=>"))
res = calc(var1,var2,oper)
#print("계산: %d %s %d = %f" % (var1,oper,var2,res))
print("계산:",var1,oper,var2,"=",res)
res = calc(10.5,3.4,"+")
print("계산:",10.5,"+",3.4,"=",res)

res = calc(10,3.4,"+")
print("계산:",10,"+",3.4,"=",res)