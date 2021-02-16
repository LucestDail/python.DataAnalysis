# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 17:03:31 2021
1. sales_2013.xlsx 파일 중 Purchase Date 컬럼 값이 01/24/2013
01/31/2013인 행만 sales_2013_01.xlsx 파일로 저장하기
@author: dhtmd
"""

import pandas as pd
infile = "sales_2013.xlsx"
outfile = "sales_2013_01.xlsx"
df = pd.read_excel(infile,sheet_name="january_2013", index_col=None)
select_date = ['01/24/2013','01/31/2013']
df_value = df[df['Purchase Date'].isin(select_date)]
print(df_value)
writer = pd.ExcelWriter(outfile,engine="openpyxl") 
df_value.to_excel(writer, sheet_name="jan_13_output",index=False)  
writer.save()