# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 10:34:08 2021

@author: dhtmd
"""

import re

str = "The quick brown fox jumps over the lazy dog Te Thhe Thhhe."
str_list = str.split() #공백으로 단어 분리
print(str_list)
#T 로 시작, 0개 이상 h, e 로 끝나느 패턴
pattern = re.compile("Th*e")
count = 0
for word in str_list:
    if pattern.search(word): #패턴에 맞는지 확인
        count += 1
print("result 1 : {1:s}:{0:d} ".format(count,"갯수"))

pattern = re.compile("Th*e", re.I)#re.I 대소문자 구분 없이
count = 0
for word in str_list:
    if pattern.search(word): # 패턴에 맞는지 확인
        count += 1
print("result 2 : {1:s}:{0:d} ".format(count,"갯수"))

print("result 3 : ", end=" ")
for word in str_list:
    if pattern.search(word):
        print(word, end=",")
print()

#(?P<match_word>Th*e) : 대소문자 구분없이 Th*e 패턴을 match_word 라는 패턴그룹으로
pattern = re.compile("(?P<match_word>Th*e)",re.I)
print("result 4 : ",end=" ")
for word in str_list:
    if pattern.search(word):
        print("{0}".format(pattern.search(word).group("match_word")),end=",")
print()


#pattern.sub : 값을 치환함, Th*e 패턴을 a 로 치환하기
pattern = re.compile("Th*e")
print("result 5 : {0}".format(pattern.sub("a", str)))
print("result 5 : ",pattern.sub("a",str))