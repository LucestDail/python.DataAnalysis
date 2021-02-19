# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 14:29:22 2021

@author: dhtmd
"""
import pymysql
import matplotlib.pyplot as plt 
import pandas as pd
from matplotlib import font_manager, rc

port_value = int(input("접속할 데이터베이스의 포트번호를 입력하세요 : "))
user_value = input("접속할 데이터베이스의 유저를 입력하세요 : ")
passwd_value = input("접속할 데이터베이스의 비밀번호를 입력하세요 : ")
conn = pymysql.connect(host="localhost", port=port_value, user=user_value, passwd=passwd_value, db="classdb",charset="utf8")

try:
    cur = conn.cursor()
    cur.execute("select * from board")
    board = {}
    for row in cur.fetchall():
        date = row[6].strftime("%Y%m%d")
        if date in board:
            curvalue = board[date]
            board[date] = curvalue+1
            pass
        else:
            board[date] = 1
    print(board)
    #xvalue = df_value["Customer Name"].tolist()
    xvalue = board.keys()
    #yvalue = df_value["Sale Amount"].tolist()
    yvalue = board.values()
    x_index = range(len(xvalue))
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ax1.bar(x_index,yvalue,align="center",color="darkblue")
    ax1.xaxis.set_ticks_position("bottom")
    ax1.yaxis.set_ticks_position("left")
    plt.xticks(x_index, xvalue, rotation=0,fontsize="small")
    plt.xlabel("게시글 작성 건수")
    plt.ylabel("글 작성일")
    plt.title("최근 등록 게시물 건수")
    plt.savefig("bar_plot.png",dpi=400,bbox_inches="tight")
    plt.show()
finally:
    cur.close()
    conn.close()