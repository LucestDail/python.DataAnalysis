# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 17:14:05 2021

@author: dhtmd
"""

import random

random_target = ""
while True:
    for i in range(0,4):
        random_target += str(int(random.random() * 10))
    if(len(random_target) == 4):
        print(f"랜덤 생성 완료 : {random_target}")
        break
    
    
counter = 0
while True:
    counter += 1
    check_target = input("서로다른 4자리 숫자를 입력하세요 : ")
    strike = 0
    ball = 0
    for i in range(0,len(random_target)):
        if(check_target[i] == random_target[i]):
            strike += 1
        else:
            ball += 1
    if(strike == 4):
        print(f"정답입니다. {counter} 번 만에 맞췄습니다")
        break
    else:
        print(f"strike : {strike}, ball : {ball}")