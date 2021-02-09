# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 11:05:56 2021

@author: dhtmd
"""

infp = None
inStr = ""
"""
open("파일이름","파일모드","인코딩방식")
파일모드
    "r" : 읽기 모드
    "w" : 쓰기 모드, 파일 존재시 내용 변경
    "a" : 쓰기 모드, 파일 존재시 내용 추가
    "t" : 텍스트 모드
    "b" : 이진 모드
"""
infp = open("2021020902.py","rt",encoding="UTF8")
while True:
    inStr = infp.readline() # 한줄 읽어서 inStr 변수 저장
    if inStr == None or inStr == "": #EOF(End Of File)  상태일 경우
        break
    print(inStr, end="")
infp.close()