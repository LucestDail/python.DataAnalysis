# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 17:42:55 2021

@author: myung

fileex5.py : 이진파일 읽고 쓰기
"""
inFp, outFp = None, None 
inStr = ""

inFp=open("jeju1.gif", "rb")
outFp=open("jeju1bak.gif", "wb")

while True :
    inStr = inFp.read()
    if not inStr :
        break
    outFp.write(inStr)

inFp.close()
outFp.close()
print("바이너리 파일 복사")
