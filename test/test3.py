# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 14:29:15 2021

@author: dhtmd
"""

word_list = {}
while True:
    inputValue = input("영어단어를 입력하세요(종료:종료) :")
    if inputValue == "종료":
        print(word_list)
        break
    if inputValue in word_list:
        print(f"{inputValue} 의 한글 뜻: {word_list[inputValue]}")
    else:
        print(f"{inputValue} 없음")
        word_input_check = input("등록된 단어가 아닙니다. 추가하시겠습니까?(y/n)")
        if word_input_check == "y":    
            word_input = input(f"{inputValue}의 한글 단어를 입력하세요")
            word_list[inputValue] = word_input
        else:
            pass