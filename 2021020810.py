# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 13:34:08 2021

@author: dhtmd
"""

class Car:
    color = ""
    speed = 0
    def upSpeed(self, value):
        self.speed += value
    def downSpeed(self, value):
        self.speed =+ value
myCar1 = Car()
myCar1.color = "빨강"
myCar1.speed = 0

myCar2 = Car()
myCar2.color = "노랑"
myCar2.speed = 0

myCar3 = Car()
myCar3.color = "파랑"
myCar3.speed = 0

myCar1.upSpeed(30)
print(f"자동차1의 색상은 {myCar1.color} 이며 현재 속도는 {myCar1.speed} 입니다.")

myCar2.upSpeed(60)
print(f"자동차1의 색상은 {myCar2.color} 이며 현재 속도는 {myCar2.speed} 입니다.")

myCar3.upSpeed(10)
print(f"자동차1의 색상은 {myCar3.color} 이며 현재 속도는 {myCar3.speed} 입니다.")