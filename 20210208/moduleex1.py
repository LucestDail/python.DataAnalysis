# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 08:30:32 2021
@author: myung

moduleex1.py : 모듈 목록 출력하기
"""

import math
import sys

print(sys.builtin_module_names)  # 설정 모듈 목록 리턴
print(dir(__builtins__))  
print(dir(math))
