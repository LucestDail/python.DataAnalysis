# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 09:47:29 2021

자바,컬렉션 === 파이썬
list   ======== list
map    ======== dictionary(키벨류의 쌍)
set    ======== set
                touple(상수화된 리스트, 변경불가 리스트)


@author: dhtmd
"""

a = [0,0,0,0]
b = []
suma = 0
sumb = 0
print(b,len(b))
for i in range(0,len(a)):
    a[i] = int(input(str(i+1) + "번째 값 : "))
    suma += a[i]
    b.append(a[i])
    sumb += b[i]
print(a)
print(b,len(b))