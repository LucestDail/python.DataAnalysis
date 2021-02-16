# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 17:42:18 2021

@author: myung

test8.py :
    1 부터 1000 까지의 홀수의 합계 계산시 최초로 1000이 넘는 
    숫자는 구하는 프로그램을 작성해 보자.
"""
hap,i = 0,0  
for i in range(1,101,2) :
    hap += i  
    if hap >= 1000 :
         break  
print("1~100의 홀수의 합에서 최초로 1000이 넘는 위치 : %d, 합계: %d" % (i,hap))