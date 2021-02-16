# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 16:59:15 2021

@author: myung
test5.py : 년도를 입력받아 윤년인지 평년인지 출력하기
"""
year = int(input("년도를 입력하세요 : "))

if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)) :
	print(year," : 윤년")
else :
    print(year," : 평년")