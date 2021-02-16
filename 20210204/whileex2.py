# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:04:22 2021

@author: myung
whileex2.py : 랜덤함수를 사용하여 숫자 맞추기
컴퓨터가 1부터 99사이의 임의의 수를 저장하고, 숫자를 입력받아
컴퓨터가 저장한 수 맞추기. 숫자를 입력한 건수를 화면에 출력하
"""
import random #난수값 구하기 위한 모듈
#컴퓨터 저장 숫자 
rnum = random.randrange(1,100) #1부터 99까지의 임의의 75
i=1
#True : 예약어. true boolean 형
#False : 예약어 false boolean 

while True :  #무한반복
    a = int(input("숫자를 입력하세요 : ")) #50
    if a > rnum :
        print("작은수 입니다")
    elif a < rnum :
        print("큰수 입니다.")        
    else :
        print("정답입니다.")
        break   #반복문을 벋어남
    i = i+1
print("%d번만에 맞췄습니다" % i)    
