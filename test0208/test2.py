# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 17:36:53 2021

@author: myung

test2.py : 
 입력된 자연수가 홀수인지 짝수인지 판별해 주는 함수를 람다식을 이용하여 작성해 보자.
"""

num = int(input("자연수를 입력하세요"))
if ((lambda x: True if x % 2 == 1 else False)(num)) :
    print(num,"숫자는 홀수 입니다.")
else :
    print(num,"숫자는 짝수 입니다.")
