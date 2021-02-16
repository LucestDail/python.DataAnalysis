# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 13:57:58 2021

@author: myung

dictionaryex3.py : 정렬하기
"""
import operator
dic,list = {},[]
dic = {"Thomas":"토마스","Edward":"에드워드","Henry":"헨리",
       "Gothen":"고든","James":"제임스"}
print(dic.items())
# sorted : 정렬 함수 
#dic.items() : (키,값)쌍인 객체. tuple객체들의 리스트. 정렬을 위한 데이터값 
#operator.itemgetter(0) : 정렬의 기준 객체 설정 .
#    0 : 튜플의 첫번째 객체로 설정 
#   reverse=True : 내림차순 정렬, 기본값 : False
list = sorted(dic.items(), key=operator.itemgetter(0),reverse=True)
print(list)
print("영문이름으로 정렬하기========= ")
list = sorted(dic.items(), key=operator.itemgetter(0),reverse=False)
print(list)
print("한글 이름으로 정렬하기========= ")
list = sorted(dic.items(), key=operator.itemgetter(1))
print(list)
print("한글 이름으로 역순 정렬하기========= ")
list = sorted(dic.items(), key=operator.itemgetter(1),reverse=True)
print(list)

