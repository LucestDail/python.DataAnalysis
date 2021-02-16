# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 13:43:22 2021

@author: dhtmd
"""

import sqlite3
con, cur = None, None
data1, data2, data3, data4 = "","","",""
con = sqlite3.connect("iddb") #db 연결 객체
cur = con.cursor()
cur.executescript('''
            drop table if exists usertable;
            create table usertable (id char(4) primary key,
                                    username char(15),
                                    email char(15),
                                    birthyear int
                                    )
            ''')
            
while True:
    data1 = input("id : ")
    if data1 == "":
        break
    data2 = input("username : ")
    data3 = input("email : ")
    data4 = input("birthday : ")
    sql = "insert into usertable values ('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 + ")"
    cur.execute(sql)
    con.commit()
    
con.close()