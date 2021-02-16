# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 09:38:18 2021

@author: dhtmd
"""

import pandas as pd
infile = "sales_2013.xlsx"
outfile = "sales_2013_allamt.xlsx"
writer = pd.ExcelWriter(outfile)
df = pd.read_excel(infile,sheet_name=None, index_col=None)
row_output = []
for worksheet_name, data in df.items():
    print("===",worksheet_name,"===")
    data_value = data.loc[:,["Customer Name","Sale Amount"]]
    row_output.append(data_value)


filtered_row = pd.concat(row_output, axis=0, ignore_index=True)
filtered_row.to_excel(writer,sheet_name="sales_2013_allamt", index=False)
writer.save()