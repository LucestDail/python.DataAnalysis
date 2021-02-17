# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:57:06 2021

@author: dhtmd
"""

import yaml
yaml_str = """
# 주석
# 정의
color_def:
    - &color1 "#FF0000" #&color1 : 변수, 참조값
    - &color2 "#00FF00"
    - &color3 "#0000FF"
# 별칭
color:
    title: *color1 #*color1 :&color1 지정된 
    body: *color2
    link: *color3
    div: *color1
"""
#yaml.load : yaml 형태의 문자열 => 리스트, 딕셔너리 형태로 변경
data = yaml.load(yaml_str, Loader=yaml.FullLoader)
print("title = ", data["color"]["title"])
print("body = ", data["color"]["body"])
print("link = ", data["color"]["link"])
print("div = ",data["color"]["div"])

yaml.dump(data,open("color.yaml","w"))