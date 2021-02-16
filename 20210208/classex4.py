# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 08:30:32 2021
@author: myung
classex4.py : 상속예제 오버라이딩예제 다중상속 가능.
"""
class Car :
    speed = 0
    door = 3
    def upSpeed(self,value):
        self.speed += value
        print("현재 속도(부모클래스): %d" % self.speed)
        
class Sedan(Car):  # Car클래스의 하위 클래스
    pass           # Car 클래스의 멤버와 같다.

class Truck(Car):
    def upSpeed(self,value):  #150이상의 speed인 경우는 최대 150. 오버라이딩
        self.speed += value
        if self.speed > 150 :
            self.speed = 150
        print("현재 속도(자손클래스): %d" % self.speed)            

class Container :
    room = 1
    
class MovingCar(Container, Car) :  #다중 상속: 부모가 여럿인 상속 
    pass
            
sedan1 = Sedan()  #객체화
truck1 = Truck()  #객체화
print("트럭 :",end="")
truck1.upSpeed(200) #Truck의 upSpeed 메서드가 오버라이딩됨        
print("승용차 :",end="")
sedan1.upSpeed(200)        

mcar = MovingCar() #Container,Car 클래스를 상속받음.
mcar.upSpeed(60)
print("이동차량의 방갯수:",mcar.room,", 문의 갯수:",mcar.door)