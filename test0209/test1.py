# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:58:14 2021

@author: myung

test1.py : sql 실행
"""
import pymysql 

conn = pymysql.connect(host="localhost", port=3307, 
                       user="scott", passwd="1234",
                       db="classdb", charset="utf8")
cur = conn.cursor()
try :
    while True :
        sql = input("sql 입력하세요=========\n")
        if sql=="" :
           break
        cur.execute("select count(*) from (" + sql + ") a")
        row = cur.fetchone()
        print("조회 레코드수:",row[0],",조회 컬럼수:",end="")        
        cur.execute(sql)
        row = cur.fetchone()
        print(len(row))
        cur.execute(sql)
        for row in cur.fetchall() :
            print(row)
finally :            
    cur.close()
    conn.close();
