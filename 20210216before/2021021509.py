# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 12:14:51 2021
엑셀 파일 읽는 방법이 다릅니다...
xlsx : 
xls : 

@author: dhtmd
"""

import openpyxl #pip install openpyxl
filename = "sales_2015.xlsx"
book = openpyxl.load_workbook(filename)
sheet = book.worksheets[0]
data = []
for row in sheet.rows:
    line = []
    for l,d in enumerate(row):
        line.append(d.value)
    print(line)
    data.append(line)
print(data)
#enumerate : 리스트에서 데이터와 index 값을 제공
for i in range(0,len(data)):
    print(i+1," : ",data[i])
    
#개선된 포문처럼 해보고 싶다면...
for i,d in enumerate(data):
    print(i+1, " : " , d)