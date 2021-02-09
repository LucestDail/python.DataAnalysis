# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 15:02:43 2021

@author: dhtmd
"""
import pymysql
conn = pymysql.connect(host="localhost", port=59753, user="root", passwd="159753", db="classdb",charset="utf8")
try:
    cur = conn.cursor()
    cur.execute("select * from item")
    for row in cur.fetchall():
        print(type(row),row)
finally:
    cur.close()
    conn.close()