# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 13:45:13 2021
xlsx 파일 모든 sheet 읽기
@author: dhtmd
"""

import openpyxl
filename = "sales_2015.xlsx"
book = openpyxl.load_workbook(filename)
#book.worksheets : excel 파일의 모든 sheet 반환
for i, sheet in enumerate(book.worksheets):
    print(book.sheetnames[i])
    data=[]
    for r,row in enumerate(sheet.rows):
        line=[]
        for i,c in enumerate(row):
            line.append(c.value)
        print(r+1," : ",line)
        data.append(line)
        