# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:56:31 2021

@author: dhtmd
"""

class Rect:
    width = 0
    height = 0
    def __init__(self, v1, v2):
        self.width = v1
        self.height = v2
    
    def area_len(self):
        return self.width * self.height
    
    def round_len(self):
        return 2*(self.width + self.height)
    
    def __lt__(self, other):
        return self.area_len() < other.area_len()
    
    def __gt__(self, other):
        return self.area_len() > other.area_len()
    
    def __eq__(self, other):
        return self.area_len() == other.area_len()
    
    def __repr__(self):
        return f"({self.width}, {self.height}),넓이 : {self.area_len()}, 둘레 : {self.round_len()}"
    
#myRect1 = Rect(2,9)
#myRect2 = Rect(3,6)

#myRect1 = Rect(4,4)
#myRect2 = Rect(3,6)

myRect1 = Rect(4,5)
myRect2 = Rect(3,6)

print(myRect1)
print(myRect2)

if myRect1 > myRect2:
    print(f"{myRect1.area_len()} > {myRect2.area_len()}")
elif myRect1 == myRect2:
    print(f"{myRect1.area_len()} == {myRect2.area_len()}")
else :
    print(f"{myRect1.area_len()} < {myRect2.area_len()}")