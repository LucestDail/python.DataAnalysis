# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 15:33:40 2021

@author: dhtmd
"""

import pymysql
conn = pymysql.connect(host="localhost", port=59753, user="root", passwd="159753", db="classdb",charset="utf8")
cur = conn.cursor()
cur.execute("drop table items")
cur.execute('''
            create table items(
                item_id integer primary key auto_increment,
                name varchar(300),
                price integer
                )
            ''')
data = [("banana",3000),("mango",30000),("apple",10000)]
for i in data:
    cur.execute("insert into items (name,price) values (%s, %s)",i)
conn.commit()
print("==========")
cur.execute("select * from items")
for row in cur.fetchall():
    print(row)
    
print("==========")
cur.execute("select * from items where price >= %s and price <= %s",(3000,10000))
for row in cur.fetchall():
    print(row)
    
print("==========")
cur.execute("delete from items where price = %s",(30000))
cur.execute("select * from items")
for row in cur.fetchall():
    print(row)
cur.close()
conn.close()