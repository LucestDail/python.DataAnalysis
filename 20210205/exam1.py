# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:34:19 2021

@author: myung
exam1.py : 
   aa,bb 리스트를 생성하고, 
   aa 리스트는 0부터 짝수 100개를 저장하고
   bb 리스트는 aa 배열의 역순으로 값을 저장하기.
   aa[0] ~ aa[9], bb[99]~bb[90] 값을 출력하기
"""
aa = []
bb = []
value = 0
#aa 리스트에 100개의 짝수 추가 
for i in range(0,100) :
    aa.append(value)
    value += 2
#bb 리스트는 aa의 역순으로 저
for i in range(0,len(aa)) :
    bb.append(aa[99-i])

for i in range(0,10) :
    print("aa[%2d]=%2d" % (i,aa[i]), end=",")
print()    
#for i in range(-1,-11,-1) :
#    print("bb[%2d]=%2d" % (i+100,bb[i]), end=",")    
for i in range(99,89,-1) :
    print("bb[%2d]=%2d" % (i,bb[i]), end=",")    
