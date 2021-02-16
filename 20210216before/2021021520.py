# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 09:42:42 2021
sales_2013.xlsx 파일의 모든 sheet의 열이 Customer Name, Sale Amount 컬럼만
sales_2013_allamt.xlsx 파일로 저장하기
@author: dhtmd
"""

import pandas as pd
infile="sales_2013.xlsx"
outfile="sales_2013_allamt.xlsx"
writer = pd.ExcelWriter(outfile)
df = pd.read_excel(infile,sheet_name=None, index_col=None)
for worksheet_name, data in df.items():
    print("===",worksheet_name,"===")
    data_value = data.loc[:,["Customer Name","Sale Amount"]]
    data_value.to_excel(writer, sheet_name=worksheet_name, index=False)
writer.save()