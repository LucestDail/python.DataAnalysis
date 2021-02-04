# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 18:09:53 2021
서력 기원 연수가 4로 나누어 떨어지는 해는 윤년으로 한다. ...
서력 기원 연수가 4, 100으로 나누어 떨어지는 해는 평년으로 한다. ...
서력 기원 연수가 4, 100, 400으로 나누어 떨어지는 해는 윤년으로 둔다.
@author: dhtmd
"""
try:
    inputValue = int(input("년도를 입력하세요 : "))
    if(inputValue%4 == 0):
        if(inputValue%100 == 0):
            if(inputValue%400 == 0):
                print(f"{inputValue} : 윤년")
            else:
                print(f"{inputValue} : 평년")
        else:
            print(f"{inputValue} : 윤년")
            
    else:
        print(f"{inputValue} : 평년")
except: 
    print("연도를 입력해주세요.")