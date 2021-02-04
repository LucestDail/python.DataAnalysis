# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 11:13:04 2021

@author: dhtmd
"""

a = int(input("값1 입력 : "))
b = int(input("값2 입력 : "))
result = a + b
print(f"{a} + {b} = {a+b}100")

print("안녕하세요", end=" : ")
print("홍길동 입니다.")

print("{0:d} {1:5d} {2:05d}".format(100,200,300))
print("{2:d} {1:5d} {0:05d}".format(100,200,300))

print("abc" + "abc" + "abc")
print("abc" , "abc" ,"abc")
print("abc"*3)

print("문자열" + "문자열")
print("""
      문
      자
      열""")