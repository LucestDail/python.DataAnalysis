# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 16:56:22 2021

@author: dhtmd
"""


nation_list = {"한국" : "서울","미국" : "워싱턴"}


while True:
    inputValue = input("나라 이름을 입력하세요('종료' 입력시 프로그램 종료) : ")
    if(inputValue == "종료"):
        break
    if inputValue in nation_list:
        print(f"{inputValue} => {nation_list[inputValue]}")
    else:
        print(f"{inputValue} 없음")
        nation_input = input("등록합니다. 수도를 입력하세요 : ")
        nation_list[inputValue] = nation_input