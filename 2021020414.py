# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 17:17:30 2021

@author: dhtmd
"""

plainMsg = input("문자를 입력하세요 : ")
print(len(plainMsg))
print(plainMsg)
cipherMsg = "";
for i in range(0,len(plainMsg)):
    if(plainMsg[i] == "a"):
        cipherMsg += "'";
    elif(plainMsg[i] == "b"):
        cipherMsg += "~"
    elif(plainMsg[i] == "c"):
        cipherMsg += "!" 
    elif(plainMsg[i] == "d"):
        cipherMsg += "@"
    elif(plainMsg[i] == "e"):
        cipherMsg += "#"
    elif(plainMsg[i] == "f"):
        cipherMsg += "$"
    elif(plainMsg[i] == "g"):
        cipherMsg += "%"
    elif(plainMsg[i] == "h"):
        cipherMsg += "^"
    elif(plainMsg[i] == "i"):
        cipherMsg += "&"
    elif(plainMsg[i] == "j"):
        cipherMsg += "*"
    elif(plainMsg[i] == "k"):
        cipherMsg += "("
    elif(plainMsg[i] == "l"):
        cipherMsg += ")"
    elif(plainMsg[i] == "m"):
        cipherMsg += "-"
    elif(plainMsg[i] == "n"):
         cipherMsg += "_" 
    elif(plainMsg[i] == "o"):
        cipherMsg += "+"
    elif(plainMsg[i] == "p"):
        cipherMsg += "="
    elif(plainMsg[i] == "q"):
        cipherMsg += "|"
    elif(plainMsg[i] == "r"):
        cipherMsg += "["
    elif(plainMsg[i] == "s"):
        cipherMsg += "]"
    elif(plainMsg[i] == "t"):
        cipherMsg += "{"
    elif(plainMsg[i] == "u"):
        cipherMsg += "}"
    elif(plainMsg[i] == "v"):
        cipherMsg += ";"
    elif(plainMsg[i] == "w"):
        cipherMsg += ":"
    elif(plainMsg[i] == "x"):
        cipherMsg += ","
    elif(plainMsg[i] == "y"):
        cipherMsg += "."
    elif(plainMsg[i] == "z"):
        cipherMsg += "/"
    elif(plainMsg[i] == "1"):
        cipherMsg += "w"
    elif(plainMsg[i] == "2"):
        cipherMsg += "e"
    elif(plainMsg[i] == "3"):
        cipherMsg += "r"
    elif(plainMsg[i] == "4"):
        cipherMsg += "t"
    elif(plainMsg[i] == "5"):
        cipherMsg += "y"
    elif(plainMsg[i] == "6"):
        cipherMsg += "u"
    elif(plainMsg[i] == "7"):
        cipherMsg += "i"
    elif(plainMsg[i] == "8"):
        cipherMsg += "o"
    elif(plainMsg[i] == "9"):
        cipherMsg += "p"
    elif(plainMsg[i] == "0"):
        cipherMsg += "q"
print("암호화 문자 : ",cipherMsg)
print("복호화 ---")
plainMsg = cipherMsg;
cipherMsg = "";
for i in range(0,len(plainMsg)):
    if(plainMsg[i] == "'"):
        cipherMsg += "a";
    elif(plainMsg[i] == "~"):
        cipherMsg += "b"
    elif(plainMsg[i] == "!"):
        cipherMsg += "c" 
    elif(plainMsg[i] == "@"):
        cipherMsg += "d"
    elif(plainMsg[i] == "#"):
        cipherMsg += "e"
    elif(plainMsg[i] == "$"):
        cipherMsg += "f"
    elif(plainMsg[i] == "%"):
        cipherMsg += "g"
    elif(plainMsg[i] == "^"):
        cipherMsg += "h"
    elif(plainMsg[i] == "&"):
        cipherMsg += "i"
    elif(plainMsg[i] == "*"):
        cipherMsg += "j"
    elif(plainMsg[i] == "("):
        cipherMsg += "k"
    elif(plainMsg[i] == ")"):
        cipherMsg += "l"
    elif(plainMsg[i] == "-"):
        cipherMsg += "m"
    elif(plainMsg[i] == "_"):
         cipherMsg += "n" 
    elif(plainMsg[i] == "+"):
        cipherMsg += "o"
    elif(plainMsg[i] == "="):
        cipherMsg += "p"
    elif(plainMsg[i] == "|"):
        cipherMsg += "q"
    elif(plainMsg[i] == "["):
        cipherMsg += "r"
    elif(plainMsg[i] == "]"):
        cipherMsg += "s"
    elif(plainMsg[i] == "{"):
        cipherMsg += "t"
    elif(plainMsg[i] == "}"):
        cipherMsg += "u"
    elif(plainMsg[i] == ";"):
        cipherMsg += "v"
    elif(plainMsg[i] == ":"):
        cipherMsg += "w"
    elif(plainMsg[i] == ","):
        cipherMsg += "x"
    elif(plainMsg[i] == "."):
        cipherMsg += "y"
    elif(plainMsg[i] == "/"):
        cipherMsg += "z"
    elif(plainMsg[i] == "w"):
        cipherMsg += "1"
    elif(plainMsg[i] == "e"):
        cipherMsg += "2"
    elif(plainMsg[i] == "r"):
        cipherMsg += "3"
    elif(plainMsg[i] == "t"):
        cipherMsg += "4"
    elif(plainMsg[i] == "y"):
        cipherMsg += "5"
    elif(plainMsg[i] == "u"):
        cipherMsg += "6"
    elif(plainMsg[i] == "i"):
        cipherMsg += "7"
    elif(plainMsg[i] == "o"):
        cipherMsg += "8"
    elif(plainMsg[i] == "p"):
        cipherMsg += "9"
    elif(plainMsg[i] == "q"):
        cipherMsg += "0"
print("복호화 문자 : ",cipherMsg)