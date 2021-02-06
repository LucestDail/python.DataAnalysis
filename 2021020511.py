# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:38:32 2021

@author: dhtmd
"""

def calc(var1,var2,oper):
    if(oper == "+"):
        return var1+var2
    elif(oper == "-"):
        return var1-var2
    elif(oper == "*"):
        return var1*var2
    elif(oper == "/"):
        return var1/var2
    else:
        print(f"{oper} : 지정된 연산자 아")
    return "오류"

oper = input("+,-,*,/ =>")
var1 = int(input("value1 => "))
var2 = int(input("value2 => "))
result_value = calc(var1,var2,oper)
print(f"result : {result_value}")