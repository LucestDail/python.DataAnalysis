# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 08:30:32 2021
@author: myung
classex3.py : 클래스멤버, 인스턴스 멤버
"""
class Car :
    color = ""
    speed = 0
    num = 0
    count = 0
    def __init__(self,v=""):
        self.color = v
        self.speed = 0  #인스턴스 변수
        Car.count += 1  #클래스 변수 : 클래스명.변수명
        self.num = Car.count #인스턴스 변수
        
    def printMessage(self):
        print("색상:%s, 속도:%dkm, 번호:%d, 생산번호:%s" % 
          (self.color,self.speed,self.num,Car.count),end="") 
           
mycar1,mycar2 = None, None #null, 참조 객체 없음.
mycar1 = Car()  #객체화. num=1
mycar1.speed = 30
mycar1.printMessage()
print()
mycar2 = Car()  #객체화 num=2
mycar2.speed = 50
mycar2.printMessage()
print()
#Car.count += 10
print("생산번호:%d" % (mycar1.count))
print("생산번호:%d" % (mycar2.count))
mycar3 = Car("빨강")  #객체화. 오류 발생. 생성자 없음.
mycar3.printMessage()
