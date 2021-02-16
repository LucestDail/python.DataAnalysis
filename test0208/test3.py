# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 15:21:52 2021

@author: myung

test3.py : Rect 클래스 구현하기
     가로,세로를 멤버변수로.
     넓이,둘레를 구하는 멤버 함수를 가지는 Rect 클래스 구현하기
     클래스의 객체를 print 시 : 
     (가로,세로),넓이:xxx,둘레:xxx가 출력
           
     두개의 Rect 객체를 
      if rect1 > rect2 ...
      elif rect1 < rect2 ...
      elif rect1 == rect2 ... 구문이 가능하도록 Rect 클래스 구현하기
"""

class Rect :
    width = 0 
    height = 0 
    
    def area(self):  
        return self.width * self.height

    def length(self):  
        return  (self.width + self.height) * 2
    
    def __init__(self,width=0,height=0) : #생성
        self.width = width
        self.height = height
    def __repr__(self) :   # \ 다음줄 연결 
        return "(%d,%d),넓이:%d,둘레:%d" % \
            (self.width,self.height,self.area(),self.length())
    
    def __lt__(self,other):   
         return self.area() < other.area()

    def __gt__(self,other):   
       return self.area() > other.area()

    def __eq__(self,other):  
       return self.area() == other.area()   
    
if __name__ == "__main__" :
     rect1 = Rect(10,20)
     rect2 = Rect(10,10)
     print(rect1)
     print(rect2)
     if rect1 > rect2 :
         print(rect1.area(),"더 큰 사각형 입니다.")
     elif  rect1 < rect2 :  
         print(rect2.area(),"더 큰 사각형 입니다.")
     elif rect1 == rect2 :
         print(rect1.area(),"=",rect2.area(),"같은 크기의 사각형 입니다.")
        
    