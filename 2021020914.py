# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 17:02:57 2021
1. 콘솔에 sql 구문을 입력하면 mariadb의 테이블들을 이용하여 결과를 출력할 수 있도록 프로그램 작성하기

   [결과]

sql 구문을 입력하세요 : select * from student
@author: dhtmd
"""
import pymysql

sqlquery = input("sql 구문을 입력하세요 : ")
conn = pymysql.connect(host="localhost", port=59753, user="root", passwd="159753", db="classdb",charset="utf8")
try:
    cur = conn.cursor()
    cur.execute(sqlquery)
    for row in cur.fetchall():
        print(type(row),row)
finally:
    cur.close()
    conn.close()