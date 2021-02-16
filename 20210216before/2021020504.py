# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 11:04:11 2021
문자열 분리
@author: dhtmd
"""
ss = "2021/02/05"

print(ss)
list = ss.split("/")
print(f"10년전 : {int(list[0])-10}")

ss = "(홍길동)"
for i in range(1,4):
    print(f"{ss[i]}#",end="")
print()  
print(ss[len(ss)-2:0:-1])
print(f"{ss[3]}#{ss[2]}#{ss[1]}#")

ss = "홍길동"
if (ss.startswith("(") == False):
    print("(",end="")
print(ss,end="")
if(ss.endswith(")") == False):
    print(")")