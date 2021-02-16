# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 10:08:52 2021

1. try 문 수행 중 오류가 발생하면 except 구문 실행됨
오류가 없는 경우 else 구문 실행
2. 오류 발생시 무시하고, 어떤 구문도 실행 되지 않도록 할때
pass 예약어 사용 가


@author: dhtmd
"""

try:
    age=int(input("age value input : "))
except:
    print("not a age value")
else:
    if age <= 19:
        print("not adult")
    else:
        print("adult")
        

try:
    f=open("no such file","r")
except FileNotFoundError:
    pass