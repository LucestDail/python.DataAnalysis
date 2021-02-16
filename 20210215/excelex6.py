# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:49:31 2021

@author: myung
excelex6.py : pandas를 이용하여 xlsx 파일 읽기
      1. xlsx 파일의 모든 sheet를 읽기
"""
import pandas as pd

infile = "sales_2015.xlsx"
df = pd.read_excel(infile,sheet_name=None,index_col=None)
row_output = []  #모든  sheet의 데이터 저장
#df.items() : sheet의 정보들.
# worksheet_name : sheet 이름
# data : sheet의 데이터
for worksheet_name,data in df.items() :
    print("===",worksheet_name,"===")
    row_output.append(data[data["Sale Amount"].replace("$","").
                           replace(",","").astype(float) > 200.0])
"""
pd.concat : row_output 를 여러개의 데이터를 연결하기 

  axis=0 : row에 연결
  axis=1 : column에 연결
"""    
filtered_row = pd.concat(row_output,axis=0,ignore_index=True)
#filtered_row : 모든  sheet의에서 주어진 조건에 맞는 데이터 저
writer = pd.ExcelWriter("sales_all_2015.xlsx",engine="openpyxl")
filtered_row.to_excel(writer,sheet_name="sale_2015",index=False)    
writer.save()
