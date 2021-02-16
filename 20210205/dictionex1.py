# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 11:37:01 2021

@author: myung

dictionaryex1.py : dictionary 예제.
"""
singer = {}  #dictionary 객체로 초기
#       키       value
singer['이름']='트와이스'  #{"이름":"트와이스"}
singer['구성원수']=9      #{"이름":"트와이스","구성원수":9}
singer['데뷔곡']='우아하게'
singer['소속사']='JYP'
# i : key
for i in singer.keys() :  #키들만 조
    print("%s=>%s" % (i,singer[i]))
print("singer 자료형:",type(singer))
print("singer:",singer)
print("singer.keys() 자료형:",type(singer.keys()))
print("singer.keys():",singer.keys())
print(list(singer.keys()))


