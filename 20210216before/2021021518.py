# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 20:37:49 2021
january_2013 시트에
Customer Name, Sale Amout 컬럼만 뽑아내서 저장하기
@author: dhtmd
"""

import pandas as pd
infile = "sales_2013.xlsx"
outfile = "sales_2013_amt.xlsx"
df = pd.read_excel(infile,"january_2013",index_col=None)
df_value = df.loc[:,["Customer Name","Sale Amount"]]
writer = pd.ExcelWriter(outfile)
df_value.to_excel(writer, sheet_name="january_2013",index=False)  
writer.save()