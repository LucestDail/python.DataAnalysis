# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 08:30:32 2021
@author: myung
classex1.py : 클래스 예제
"""
# 기본 생성자 : __init__(self) : => 생성자를 구현하지 않으면 자동으로 제공되는 생성자
#                pass
# self : 자바의 this(자기참조변수:자신객체의 멤버를 표현시 사용되는 예약어)
class Car :    #클래스
    color = ""  # 멤버변수
    speed = 0  #  멤버변수
    def upSpeed(self, value):  # 멤버메서드
        self.speed += value
    def downSpeed(self, value):  # 멤버메서드
        self.speed -= value
myCar1 = Car()  # 객체화. 생성자 호출됨. 기본생성자 호출
myCar1.color = "빨강"
myCar1.speed = 0
myCar2 = Car()
myCar2.color = "노랑"
myCar2.speed = 0
myCar3 = Car()
myCar3.color = "파랑"
myCar3.speed = 0
myCar1.upSpeed(30)
print("자동차1의 색상은 %s 이며, 현재 속도는 %dkm 입니다." % 
               (myCar1.color, myCar1.speed))

myCar2.upSpeed(60)
print("자동차2의 색상은 %s 이며, 현재 속도는 %dkm 입니다." % 
               (myCar2.color, myCar2.speed))
myCar3.upSpeed(10)
print("자동차3의 색상은 %s 이며, 현재 속도는 %dkm 입니다." % 
               (myCar3.color, myCar3.speed))