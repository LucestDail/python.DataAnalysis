# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 11:04:03 2021

@author: myung

listex3.py : 문자열 분리
"""
ss = "2021/02/05"
print("10년전 년도 출력하기")
list = ss.split("/")
print("10년전 :",int(list[0])-10 )

ss = "(홍길동)"  #   홍#길#동# 출력하기
for i in range(1,len(ss)-1) :
    print(ss[i],end="#")
print() 
# for문 사용 없이  동길홍 출력하기
print(ss[len(ss)-2:0:-1])

# ss 문자열이 (시작하지 않으면 ( 추가하기
#  ) 끝나지 않으면  ) 추가하기

ss = "(홍길동)"
if ss.startswith("(") == False :
    print("(", end="")
print(ss,end="")
if ss.endswith(")") == False :
    print(")")
    






