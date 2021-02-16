# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 14:51:40 2021

@author: myung
exam1.py : ssec1804.xls 파일에서 1.남자,1.여자 sheet의 데이터를 
           ssec1804mf.xls 파일에 남자,여자 sheet의 데이터로 저장하기 
"""
from xlrd import open_workbook
from xlwt import Workbook

def makesheet(output_sheet): # output_sheet_female : "여자"인  sheet
    for row_index in range(worksheet.nrows) : 
        for column_index in range(worksheet.ncols) :
            output_sheet.write(row_index, column_index,
             worksheet.cell_value(row_index, column_index))
#        print(worksheet.cell_value(row_index, column_index))

infile = "ssec1804.xls"
outfile = "ssec1804mf.xls"
worksheet = None  #전역변수
outworkbook = Workbook() #빈데이터. 출력될 xls 파일의 내용
output_sheet_male = outworkbook.add_sheet("남자") #outworkbook에 남자 sheet 추가
output_sheet_female = outworkbook.add_sheet("여자") #outworkbook에 여자 sheet 추가 
#workbook : ssec1804.xls 의 모드 데이터 
with open_workbook(infile) as workbook :
    #worksheet : 1.남자 sheet 데이터 
    worksheet = workbook.sheet_by_name("1.남자")
    makesheet(output_sheet_male)
    worksheet = workbook.sheet_by_name("1.여자")
    makesheet(output_sheet_female)
outworkbook.save(outfile)