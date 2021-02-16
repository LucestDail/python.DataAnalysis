# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 14:51:49 2021
ssec1804.xls 파일에서 1.남자 sheet, 1.여자 sheet 내용을 
ssec1804mf.xls 파일에 남자, 여자 sheet 데이터로 저장하기
@author: dhtmd
"""

from xlrd import open_workbook
from xlwt import Workbook

def makesheet(output_sheet):
    for row_index in range(worksheet.nrows):
        for column_index in range(worksheet.ncols):
            output_sheet.write(row_index,column_index, worksheet.cell_value(row_index, column_index))
        #print(worksheet.cell_value(row_index, column_index))
        

infile = "ssec1804.xls"
outfile = "ssec1804mf.xls"
worksheet = None #전역 변수
outworkbook = Workbook()#빈 데이터. 출력될 xls 파일의 내용
output_sheet_male = outworkbook.add_sheet("남자") #outworkbook 에 남자 sheet 추가
output_sheet_female = outworkbook.add_sheet("여자") #outworkbook 에 여자 추가
#workbook : ssec1804.xls 의 모든 데이터
with open_workbook(infile) as workbook: #worksheet : 1.남자 데이터
    worksheet = workbook.sheet_by_name("1.남자")
    makesheet(output_sheet_male)
    worksheet = workbook.sheet_by_name("1.여자")
    makesheet(output_sheet_female)
outworkbook.save(outfile)