import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import time
driver = webdriver.Chrome("C:/Users/dhtmd/Documents/pythonRepo/python.DataAnalysis/test/chromedriver")
result_list = []

for i in range(1,11) :

    driver.get("https://www1.president.go.kr/petitions/best?page=" + str(i))
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')


    for i in soup.select("#cont_view > div.cs_area > div > div > div.board.text > div.b_list.category > div.bl_body > ul > li"):
        print(i.find("div", class_="bl_subject").text[3:].strip())
        result_list.append(i.find("div", class_="bl_subject").text[3:])

    time.sleep(5)


driver.close()


# 엑셀부분
from openpyxl import Workbook
write_wb = Workbook()
write_ws = write_wb.active

for i in range(1,len(result_list)+1) :
    write_ws.cell(i, 1, result_list[i-1])

write_wb.save('bludhouse.xlsx')