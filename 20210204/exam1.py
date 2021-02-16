# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 12:01:19 2021

@author: myung
exam1.py : 금액을 입력받아 동전(500,100,50,10,1)으로 바꿔 주는 프로그램 작성하기
           동전의 갯수를 최소개로한 각각의 동전의 갯수를 구하는 프로그램 작성하기
"""
money = int(input("금액을 입력해주세요 : "))
print("500원 동전의 갯수:",money//500,"개")
money = money % 500
print("100원 동전의 갯수:",money//100,"개")
money %= 100
print("50원 동전의 갯수:",money//50,"개")
money %= 50
print("10원 동전의 갯수:",money//10,"개")
money %= 10
print("1원 동전의 갯수:",money,"개")