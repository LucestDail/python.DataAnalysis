# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:56:10 2021

@author: myung

test6.py : 화면에서 숫자를 입력받아 야구 게임하기
"""
import random 
 
list1=[]
set = set(list1)
while len(set) < 4 :   #중복데이터 배제
    rnum = random.randrange(0,10)  #0 ~9까지의 임의의 수
    set.add(rnum)
list1 = list(set)  #순서 유지
print(list1)  #컴퓨터가 저장한 수
cnt = 0
while True :
    number = input("서로다른 4자리 숫자를 입력하세요: ")
    cnt += 1
    strike = 0
    ball = 0
    for n in number:
        num = int(n)
        if list1.count(num)  == 1:  #list1 값에 num 값의 갯수. 존재.
            if number.find(n) == list1.index(num):  #위치 같은 경우
                strike += 1
            else:
                ball += 1
                
    if(strike == 4) :
        break                
    else :
        print("Strike:", strike, "Ball:", ball)

print(cnt,"번만에 맞췄습니다.")

  

