# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 10:10:49 2021
 네이버 셀레니움
@author: dhtmd
"""

import time
from selenium import webdriver
driver = webdriver.Chrome("C:/Users/dhtmd/Documents/pythonRepo/python.DataAnalysis/20210218/chromedriver")
time.sleep(5)
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
id = input("네이버 아이디를 입력하세요 : ")
driver.execute_script("document.getElementsByName('id')[0].value='"+id+"'")
pw = input("네이버 비밀번호를 입력하세요 : ")
driver.execute_script("document.getElementsByName('pw')[0].value='"+pw+"'")
driver.find_element_by_xpath('//*[@id="log.login"]').click()
time.sleep(5)
driver.get("https://devosh.herokuapp.com/")