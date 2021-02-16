# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 14:38:16 2021

@author: dhtmd
"""

class Car:
    speed = 0
    door = 3
    def upSpeed(self, value):
        self.speed += value
        print(f"현재 속도(부모클래스) : {self.speed}")
class Sedan(Car):
    pass

class Truck(Car):
    def upSpeed(self,value):
        self.speed += value
        if self.speed > 150:
            self.speed = 150
        print(f"현재 속도(자손클래스) : {self.speed}")
class Container:
    room = 1
class MovingCar(Container, Car):
    pass

sedan1 = Sedan()
truck1 = Truck()
print(f"트럭 : {truck1.upSpeed(200)}")
print(f"승용차 : {sedan1.upSpeed(200)}")
mcar = MovingCar()
mcar.upSpeed(60)
print(f"이동차량의 방갯수 : {mcar.room}, 문의 갯수 : {mcar.door}")