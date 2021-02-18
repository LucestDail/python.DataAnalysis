# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 21:40:43 2021

@author: dhtmd
"""
import time
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome("C:/Users/dhtmd/Documents/pythonRepo/python.DataAnalysis/20210218/chromedriver")
time.sleep(2)
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
id = "dhtmdgussksm"
driver.execute_script("document.getElementsByName('id')[0].value='"+id+"'")
pw = "epdlfnti135"
driver.execute_script("document.getElementsByName('pw')[0].value='"+pw+"'")
driver.find_element_by_xpath('//*[@id="log.login"]').click()
time.sleep(2)
driver.get("https://order.pay.naver.com/home?tabMenu=SHOPPING")
time.sleep(2)

items_name_driver = driver.find_elements_by_css_selector("div.goods_info > a > p.name")
items_price_date_driver = driver.find_elements_by_css_selector("div.goods_info > a > ul > li")
items_name = []
items_price_date = []
items_price = []
items_date = []
items_collection=[]
#driver -> str
for name in items_name_driver:
    items_name.append(name.text)
for price_date in items_price_date_driver:
    items_price_date.append(price_date.text)    


#price_date -> price, date
for i in range(0,len(items_price_date)):
    if i%2 == 0:
         items_price.append(items_price_date[i])
    else:
        items_date.append(items_price_date[i])

items_collection=[]
for (name,price,date) in zip(items_name, items_price, items_date):
    items_collection.append(
        {
            'name' : name,
            'price' : price,
            'date' : date
            }
        )
data = pd.DataFrame(items_collection)
print(data)
data.to_csv('items_collection.csv',index=False)
driver.quit()