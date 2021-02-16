# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 14:56:17 2021

@author: myung

functionex2.py : 전역 변수 사용하기
"""

def func1() :
    global gval #gval 변수는 전역변수로 선언된 변수로 사용함.
    a = 20   #지역변수  func1 함수에서만 사용되는 변수
    b = 1000 #지역변수. func1 함수에서만 사용되는 변수  
    gval = 200 #전역변수 gval 값을 100에서 200으로 변경
    print("func1() 함수 호출함",gval,a,b) #200 20 1000. 전역변수,지역변수,지역변수값 출력

def func2() :
    print("func2() 함수에서 func1() 함수를 호출함")
    func1()
    print("전역 변수 gval 값=",gval,a) #전역변수값 출력
    #print(b) #오류    


gval = 100  #전역변수 => 모든 함수에서 접근이 가능한 변수
a = 10      #전역변수

if __name__ == '__main__' : #프로그램의 시작. main함
    func2()
