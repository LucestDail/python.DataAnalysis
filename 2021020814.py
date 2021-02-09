# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 14:55:40 2021
생성자 : __init__(self, ...)
소멸자 : __del__(self)
문자열화 : __repr__(self)
+ : __add__
- : __sub__
< : __lt__
> : __bg__
== : __eq__
@author: dhtmd
"""

class Line:
    length = 0
    def __init__(self, length):
        self.length = length
        
        
    def __repr__(self):
        return f"선의 길이 : {self.length}"
    
    
    def __add__(self, other):
        print(" __add__ invoke")
        return self.length + other.length
    
    
    def __lt__(self, other):
        return self.length < other.length
    
    def __gt__(self, other):
        return self.length > other.length
    
    def __eq__(self, other):
        return self.length == other.length
    
    def __del__(self):
        print(self.length, " 제거")



myline1 = Line(100) #__init__ -> 객체생성시 호출되는 메소드
myline2 = Line(200)
print(myline1)#__repr__(self) : toString 메소드 기능
print(myline2)
print(f"선의 길이 합 : {myline1+myline2}")
if myline1.__lt__(myline2): #__lt__
    print(f"{myline1} < {myline2}")
elif myline1 == myline2: #__eq__
    print(f"{myline1} == {myline2}")
else:
    print(f"{myline1} > {myline2}")