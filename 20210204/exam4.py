# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 14:06:37 2021

@author: myung
exam3.py : 
숫자를 입력받아 입력수까지 합을 출력하기
숫자를 입력받아 입력수까지 짝수합을 출력하기
"""

num=int(input("숫자를 입력하세요 : "))
sum=0;
for i in range(1,num+1) :
    sum += i
print("1부터",num,"까지의 합:",sum)    

sum=0
#for i in range(0,num+1,2) :
#    sum += i
for i in range(1,num+1) :
    if(i%2==0) :
        sum += i
print("1부터",num,"까지의 짝수 합:",sum)    
