# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 13:58:47 2021

@author: myung
excelex3.py : xls 파일 읽기
  xlsx : openpyxl 모듈 사용
  xls  : xlrd 모듈 사용 => excel파일 읽기 모듈
"""
from xlrd import open_workbook
infile = "ssec1804.xls"
workbook = open_workbook(infile) #xls 파일 
print("sheet 의 갯수",workbook.nsheets)
#workbook.sheets() : sheet들 정보 저장
#worksheet : 한개의 sheet 데이터 저장 
for worksheet in workbook.sheets() :
    print("worksheet 이름:",worksheet.name)
    print("행의 수:",worksheet.nrows)
    print("컬럼의 수:",worksheet.ncols)
    #해당 sheet의 데이터 출
    for row_index in range(worksheet.nrows) :
        for column_index in range(worksheet.ncols) :
#worksheet.cell_value(행인덱스,열인덱스) : excel 파일의 셀 데이터            
            print(worksheet.cell_value(row_index,column_index),
                       ",",end="")
        print()    
#        pass
