# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:06:12 2021

@author: dhtmd
"""

inFp, outFp = None, None
inStr = ""
infile = input("input : ")
outfile = input("output : ")
inFp = open(infile, "r", encoding = 'utf-8')
outFp = open(outfile, "w", encoding='utf-8')

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)
    
inFp.close()
outFp.close()
print("\n 복사 완료")