# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 17:37:45 2021

@author: myung
test3.py : 텍스트 파일 복사하기
"""

inFp, outFp = None, None 
inStr = ""
infile = input("원본파일의 이름을 입력하세요 : ")
outfile = input("복사본파일의 이름을 입력하세요 : ")
inFp=open(infile, "r",  encoding='utf-8')
outFp=open(outfile, "w",  encoding='utf-8')

inList = inFp.readlines() #text모드에서만 사용가능한 함수.
for inStr in inList :
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("\n복사완료")
