# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 13:58:16 2021

@author: dhtmd
"""

class Car:
    color = ""
    speed = 0
    num = 0
    count = 0
    def __init__(self):
        self.speed = 0 #인스턴스 변수
        Car.count += 1 #클래스 변수 : 클래스명, 변수명
        self.num = Car.count #인스턴스 변수
        
    def printMessage(self):
        print(f"색상 : {self.color}, 속도 : {self.speed}, 번호 : {self.num}, 생산번호 : {self.count}")


myCar1, myCar2, myCar3 = None, None, None
myCar1 = Car()
#myCar1.color = "빨강"
myCar1.speed = 30
myCar1.printMessage()

myCar2 = Car()
#myCar2.color = "노랑"
myCar2.speed = 60
myCar2.printMessage()

myCar3 = Car()
#myCar3.color = "파랑"
myCar3.speed = 10
myCar3.printMessage()

print("==========")
Car.count += 10
print(f"생산번호 : {myCar1.count}")
print(f"생산번호 : {myCar2.count}")
print(f"생산번호 : {myCar3.count}")

myCar4 = Car("검정")
myCar4.printMessage()