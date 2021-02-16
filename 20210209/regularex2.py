'''
Created on Tue Feb  9 08:32:11 2021
@author: myung
regularex2.py : 정규식 예제 2. 정규화 모듈 사용하기
'''
import re  #정규식을위한 모

data = '''
   park 80090-1234567
   kim  700905-1234567
   choi 850101-a123456
'''
pat = re.compile("(\d{6,7})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))
"""
  park 8009050-*******
   kim  700905-*******
   choi 850101-a123456
"""
"""
  정규식에서 사용되는 기호
  1. () : 그룹화
  2. [] : 문자
  3. {n} : n개 갯수
        ca{2}t : a 문자가 2개
           "ct"  : false
           "cat" : false
           "caat" : true
           "caaaat" : false
     {n,m} : n개이상 m개 이하 갯수
        ca{2,5}t : a 문자가 2개
           "ct"  : false
           "cat" : false
           "caat" : true
           "caaaat" : true
           "caaaaaaat" : false
        
  4. \\d: 숫자
  5. \g<n> : n번째 그룹
  6. ?  : 0 또는 1
         ca?t : a문자가 없거나 1개인경우
           "ct"  : true
           "cat" : true
           "caaaat" : false
  7. *  : 0개이상
         ca*t : a문자가 0개이상
           "ct"  : true
           "cat" : true
           "caaaat" : true
  8. +  : 1개이상
         ca+t : a문자가 1개이상
           "ct"  : false
           "cat" : true
           "caaaat" : true
  
"""