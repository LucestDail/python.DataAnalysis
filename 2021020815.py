# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 15:49:58 2021

@author: dhtmd
"""

class SuperClass:
    #raise NotImplementedError : 오버라이딩 안하면 예외 발생
    def method(self): # 추상 메서드
        raise NotImplementedError # 반드시 오버라이딩 해야함
#SubClass 클래스 생성하기. SuperClass의 하위 클래스
#부모클래스와 같은 맴버를 가진다.

class SubClass1(SuperClass):
    def method(self):
        print("SubClass1 에서 method 함수 오버라이")

sub1 = SubClass1()
sub1.method()
        