# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 10:15:00 2021

@author: dhtmd
"""

import codecs
filename = "jeju1.csv"
csv = codecs.open(filename, "r", "utf8").read()
data = [] #한줄 분리한 내용 저장
rows = csv.split("\r\n") #line 분리 리스트 생성
for row in rows:
    if row == "":continue
    cells = row.split(",")
    data.append(cells)
outfp = open("jeju1.txt","w",encoding="utf8")
for c in data:
    print(c[0], c[1], c[2])
    outfp.write(" ".join(map(str,c)) + "\n")
outfp.flush()
outfp.close()