# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 09:47:36 2021

@author: dhtmd
"""

import sys #cli 모듈
input_file = sys.argv[1]
output_file = sys.argv[2]
with open(input_file, 'r', newline="", encoding="utf8") as filereader:
    with open(output_file, 'w', newline="", encoding="utf8") as filewriter:
        header = filereader.readline()
        print(type(header))
        header = header.strip()#공백 제
        print(header)
        header_list = header.split(",")# , 기준 분리
        print(header_list)
        #map(str, header_list) : header_list 리스트의 요소들을 문자열로 변환
        filewriter.write(",".join(map(str, header_list)) + "\r\n")
        for row_list in filereader:#입력 스트림에서 파일을 한줄씩 읽기
            filewriter.write(row_list)