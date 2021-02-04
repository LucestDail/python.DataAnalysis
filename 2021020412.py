# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:36:53 2021

@author: dhtmd
"""

print("안녕하세요")

print("안녕하세요"[0])

print("안녕하세요"[4])

print("안녕하세요"[-1])

print("안녕하세요"[-2])

print("안녕하세요"[1:3])

print("안녕하세요"[:3])

print("안녕하세요"[3:])

print("안녕하세요"[::2])

print("안녕하세요"[::-1])

print("안녕하세요"[::-2])

print(len("안녕하세요"))

print("안녕하세요")

"""
a = input("문자열 입력 : ")
b = input("찾을 문자 입력 : ")
sum = 0
for i in range(0,len(a)):
    if(a[i] == b):
        sum += 1
        
print(f"{a} 에서 {b} 문자 갯수 : {sum}")
print(f"{b} 문자 갯수 : {a.count(b)}")
print(f"{b} 문자 인덱스값 : {a.index(b)}")
"""
arr = [10,20,30,40,50,60,70]
print(arr[:2])
print(arr[::2])
print(arr[1::2])
print(arr[::-2])
print(arr[5::-2])

sum = 0
for i in range(0,len(arr)):
    sum += arr[i]
print(f"전체합 : {sum}, 평균 : {sum/len(arr)}")