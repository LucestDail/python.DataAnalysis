# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 13:50:47 2021

@author: dhtmd
"""

class Car:
    color = ""
    speed = 0
    def __init__(self, v1, v2):
        self.color = v1
        self.speed = v2
    def upSpeed(self, value):
        self.speed += value
    def downSpeed(self, value):
        self.speed =+ value

myCar1 = Car("빨강", 30)
myCar2 = Car("노랑", 60)
myCar3 = Car("파랑", 10)

print(f"자동차1의 색상은 {myCar1.color} 이며 현재 속도는 {myCar1.speed} 입니다.")
print(f"자동차1의 색상은 {myCar2.color} 이며 현재 속도는 {myCar2.speed} 입니다.")
print(f"자동차1의 색상은 {myCar3.color} 이며 현재 속도는 {myCar3.speed} 입니다.")