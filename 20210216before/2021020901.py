# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 10:04:08 2021

@author: dhtmd
"""

import re

data = '''
    park 800905-1234567
    kim  700905-1234567
    choi 850101-a123456
'''

pat = re.compile("(\d{6,7})[-]\d{7}")
print(pat.sub("\g<1>-*******",data))

"""
    park 800905-*******
    kim  700905-*******
    choi 850101-a123456
    
    정규식에서 사용되는 기호
    1. () : 그룹화
    2. [] : 문자
    3. {} : 갯수
        - ca{2}t : a 문자가 2개인 경우 -> caat
    4. \d : 숫자
    5. \g<1> : 그룹 1번
    6. ? : 0 또는 1
        - cat?t : a 문자가 없거나 1개인 경우 -> ct, cat
    7. * : 0개 이상
        - ca*t : a 문자가 없거나 1개 이상인 경우 -> ct, cat, caat ...
    8. + : 1개 이상
        - ca+t : a 문자가 1개 이상인 경우 -> cat, caat, caaat ...    
    
"""