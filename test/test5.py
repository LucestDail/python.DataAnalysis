# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 14:29:29 2021

@author: dhtmd
"""

import pymysql
import matplotlib.pylab as plt
from matplotlib import rc
import pandas as pd
import random
rc('font', family="Malgun Gothic")
port_value = int(input("접속할 데이터베이스의 포트번호를 입력하세요 : "))
user_value = input("접속할 데이터베이스의 유저를 입력하세요 : ")
passwd_value = input("접속할 데이터베이스의 비밀번호를 입력하세요 : ")


conn = pymysql.connect(host="localhost", port=port_value, user=user_value, passwd=passwd_value, db="classdb",charset="utf8")

try:
    cur = conn.cursor()
    cur.execute("select * from board")
    board = {}
    for row in cur.fetchall():
        writer = row[2]
        date = row[6]
        if writer in board:
            curvalue = board[writer]
            board[writer] = curvalue+1
            pass
        else:
            board[writer] = 1
            
    xvalue = board.keys()
    yvalue = board.values()
    colors = []
    explode_set = []
    explode = []
    
    for i in range(0,len(xvalue)):
        #random generate color
        color = "#" + ("%06x" % random.randint(0, 0xFFFFFF))
        colors.append(color)
        #explode setting
        if i == 0:
            explode.append(0.1)
        else:
            explode.append(0)
            
    labels = xvalue
    sizes = yvalue
    plt.title("최다 글쓴이별 게시물건수")
    wedgeprops = {'width' : 0.7, 'edgecolor':'w','linewidth':0}
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90, wedgeprops=wedgeprops)
    plt.show()
finally:
    cur.close()
    conn.close()