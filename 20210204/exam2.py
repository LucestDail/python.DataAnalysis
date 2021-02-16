# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 12:05:44 2021

@author: myung

exam2.py : 초를 입력받아 몇시간 몇분 몇초인지 출력하기
"""

second = int(input("초를 입력해주세요"))
print(second//3600,"시간",end=" ")
second %= 3600
print(second//60,"분",second%60,"초")
