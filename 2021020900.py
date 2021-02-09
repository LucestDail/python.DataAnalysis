# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 09:44:02 2021

@author: dhtmd
"""

data = '''
    park 800905-1234567
    kim  700905-1234567
    choi 850101-a123456
'''

result = []
for line in data.split("\n"):
    word_result=[]
    for word in line.split(" "):
        #isdigit : 숫자인 경우 true
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
        #join: list의 요소를 연결
    result.append(" ".join(word_result))
print("\n".join(result))

instr="123"
instr="A"
if instr.isdigit():
    print(f"{instr} : 숫자")
elif instr.isalpha():
    print(f"{instr} : 문자")
elif instr.isalnum():
    print(f"{instr} : 숫자+문자")
elif instr.islower():
    print(f"{instr} : 소문자")
elif instr.isupper():
    print(f"{instr} : 대문자")
elif instr.isspace():
    print(f"{instr} : 공백")
else:
    print("몰라레후")