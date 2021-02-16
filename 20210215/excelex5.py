# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:30:34 2021

@author: myung

excelex5.py : pandas를 이용하여 excel 파일 읽고 쓰기.
"""
import pandas as pd

infile = "sales_2015.xlsx"
outfile = "sales_2015_pd.xlsx"
#read_excel(file이름,sheet이름,인덱스컬럼여부)
df = pd.read_excel(infile,"january_2015",index_col=None)
print(df)
#df_value : Sale Amount 컬럼의 값이 500.0보다 큰 값을 가지는 행을 조회.
df_value = df[df["Sale Amount"].astype(float) > 500.0] 
#xlsx 파일로 저장 
#writer : sales_2015_pd.xlsx 파일을 출력파일로 설정. openpyxl=> xlsx형태
writer = pd.ExcelWriter(outfile,engine="openpyxl")
#df_value 의 데이터를 writer파일에 jan_15_out sheet로 저장. 인덱스값 없음 
df_value.to_excel(writer,sheet_name="jan_15_out",index=False)
#파일로 생성.
writer.save()

