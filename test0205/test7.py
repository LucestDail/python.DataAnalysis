# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 17:38:32 2021

@author: myung

test7.py : 
  화씨온도= (( 9 / 5) * 섭씨온도) + 32 인 경우 섭씨 -20 ~ 50 도까지를 
  화씨 온도로 변경하여 작성하기
"""

for c in range(-20,51) :
   print("섭씨온도",c,":화씨온도:",((9 / 5) * c) + 32)

