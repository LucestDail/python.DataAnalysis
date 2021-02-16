# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 14:30:48 2021

@author: myung
excelex4.py : xls 파일을 읽고 쓰기
"""
from xlrd import open_workbook #excel 파일 읽기 위한 모듈
from xlwt import Workbook      #excel 파일을 쓰기 위한 모듈 pip install xlwt

infile = "ssec1804.xls" #원본데이터
outfile ="ssec1804out.xls" #복사데이터 (하나의 sheet만 저장)

outworkbook = Workbook()  #비어있는 xls 파일

out_sheet = outworkbook.add_sheet("전체증감") #출력한 xls파일에 sheet 추가. 이름설정 

#open_workbook(infile) : 원본데이터 xls파
with open_workbook(infile) as workbook :
    #worksheet : 원본 xls파일의 sheet의 이름이 "1.전체증감" sheet 데이터 
    worksheet = workbook.sheet_by_name("1.전체증감")
    for rindex in range(worksheet.nrows) :
#out_sheet.write(rindex,cindex,원본cell) : 원본cell의 데이터를 rindex,cindex
#                                         의 데이터로 저장         
        for cindex in range(worksheet.ncols) :
            out_sheet.write(rindex,cindex,
            worksheet.cell_value(rindex,cindex))
            print(worksheet.cell_value(rindex,cindex))

#outworkbook의 데이터를 ssec1804out.xls파일로 저
outworkbook.save(outfile)  