# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 10:12:29 2021

@author: myung
listex2.py : 리스트 함
"""
mylist = [30,10,20]
# %s : 문자열을 지정하는 형식지정문자
print("리스트:%s" % mylist)
mylist.append(40)
print("mylist.append(40) 리스트:%s" % mylist)
#pop : LIFO(stack) 관련 함수. 
print("pop() 메서드 결과:%s" % mylist.pop())
print("pop() 메서드 후 리스트 :%s" % mylist)

mylist.sort()
print("mylist.sort() 후 리스트 : %s" % mylist)
mylist.reverse()  #역순 재배치
print("mylist.reverse() 후 리스트 : %s" % mylist)

print("20값의 위치 : %d" % mylist.index(20)) #20값의 인덱스값 리턴
mylist.insert(2,222)
print("mylist.insert(2,222) 후 리스트 : %s" % mylist)
mylist.remove(222)  #222 값을 제
print("mylist.remove(222) 후 리스트 : %s" % mylist)
mylist.extend([77,77,99])  #리스트 추가 
print("mylist.extend([77,77,99]) 후 리스트 : %s" % mylist)
print("77값의 갯수 : %d" % mylist.count(77)) # 77요소의 갯수 리턴
#mylist의 요소 중 200값이 없다. 실행 오류 발생 
#print("200값의 위치 : %d" % mylist.index(200)) #200값의 인덱스값 리턴
# list 객체에는 find 메서드 없다. 오류 발생 
#print("20값의 위치 : %d" % mylist.find(20)) #20값의 인덱스값 리턴
