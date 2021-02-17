# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 15:02:19 2021

@author: dhtmd
"""

import yaml #pip install pyYAML
import json
yaml_str = """
    Date: 2021-02-17
    PriceList:
        -
            item_id: 1000
            name: banana
            color: yellow
            price: 800
        -
            item_id: 1001
            name: orange
            color: orange
            price: 1400
        -
            item_id: 1002
            name: Apple
            color: red
            price: 2400
"""
data = yaml.load(yaml_str,Loader=yaml.FullLoader)
print(type(data))
print(data["Date"],"과일 가격")
for item in data["PriceList"]:
    print(item["name"],item["price"])
    
#yaml_str 문서를 json 형태의 문자열로 변경하고 동일한 결과 나오도록
print("yaml_str 문서를 json 형태의 문자열로 변경하고 동일한 결과 나오도록")
json_format = """{
 "Date": "2021-02-17",
 "PriceList": [
     {"item_id": 1000,
      "name": "banana",
      "color": "yellow",
      "price": 800
      },
     {"item_id": 1001,
      "name": "orange",
      "color": "orange",
      "price": 1400
      },
     {"item_id": 1002,
      "name": "Apple",
      "color": "red",
      "price": 2400
      }
     ]
}"""
str_to_json = json.loads(json_format)
print(str_to_json["Date"],"과일가격")
for item in str_to_json["PriceList"]:
    print(item["name"],item["price"])