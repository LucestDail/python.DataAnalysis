# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:06:13 2021

@author: myung

dbex3.py : usertable의 내용을 화면 출력하기
"""
import sqlite3

con, cur = None, None
row = None
con = sqlite3.connect("iddb")
cur = con.cursor()

cur.execute("select * from usertable")
item_list = cur.fetchall()  #모든 레코드 조회 => 리스트 리
for it in item_list :
   print(it)
print()

cur.execute("select * from usertable")
while True :
    row = cur.fetchone()  #한개의 레코드만 조회
    if row == None :
        break
    print("%5s %15s %15s %d" % (row[0],row[1],row[2],row[3]))    
con.close()

