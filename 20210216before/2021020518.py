# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:35:16 2021

@author: dhtmd
"""

def fibo(fiboNum):
    if(fiboNum == 0):
        return 0    
    elif(fiboNum == 1):
        return [0]
    elif(fiboNum == 2):
        return [0,1]
    else:
        fibo_list = [0,1,1] 
        for i in range(3,fiboNum):
            fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
        return fibo_list


fiboNum = int(input("피보나치 수열 출력하기. : "))
print(fibo(fiboNum))