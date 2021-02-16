# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:06:37 2021
sales_2015.xlsx 파일 읽어서 1월 고객별 판매 금액 막대그래프로 출력하기
@author: dhtmd
"""

import matplotlib.pyplot as plt 
import pandas as pd
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font',family=font_name) #현재 폰트 변경

infile="../sales_2015.xlsx"
df = pd.read_excel(infile,"january_2015",index_col=None)
df_value = df.loc[:,["Customer Name","Sale Amount"]]
plt.style.use("ggplot")
xvalue = df_value["Customer Name"].tolist()
yvalue = df_value["Sale Amount"].tolist()
x_index = range(len(xvalue))
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.bar(x_index,yvalue,align="center",color="darkblue")
ax1.xaxis.set_ticks_position("bottom")
ax1.yaxis.set_ticks_position("left")
plt.xticks(x_index, xvalue, rotation=0,fontsize="small")
plt.xlabel("고객")
plt.ylabel("판매금액")
plt.title("고객별 판매금액")
plt.savefig("bar_plot.png",dpi=400,bbox_inches="tight")
plt.show()