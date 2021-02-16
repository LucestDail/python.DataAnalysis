# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 15:27:42 2021

@author: myung

functionex3.py 
   1. 리턴값을 두개이상 반환 =>리스트로 반환
   2. 가변 매개변수 함
"""
def multi(v1,v2):
    list = []
    res1 = v1+v2  #합
    res2 = v1-v2  #차
    list.append(res1)
    list.append(res2)
    return list  #list[0]:합계, list[1]:차

def multiParam(* p) :  #가변매개변수 : 매개변수의 갯수 지정이 안됨. 
    result = 0
    for i in p :
        result += i
    return result    

hap,sub=0,0
list = multi(100,200)
hap = list[0]
sub = list[1]
print("multi 함수의 리턴: %d, %d " % (hap, sub))
print("multiParam()=",multiParam())  #0
print("multiParam(10)=",multiParam(10)) #10
print("multiParam(10,20)=",multiParam(10,20))  #30
print("multiParam(10,20,30)=",multiParam(10,20,30)) #60
