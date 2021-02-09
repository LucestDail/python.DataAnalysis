# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 17:10:55 2021

@author: dhtmd
"""

input_value = input("주민등록번호를 입력하세요(111111-1111111) => ")
try:
    checker = input_value.split("-")[1][0]
    if(checker == "1" or checker == "3"):
        print("남자입니다.")
    elif(checker == "2" or checker == "4"):
        print("여자입니다.")
    else:
        print("내국인아님")
except:
    print("입력 오류")