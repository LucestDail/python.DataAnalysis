# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 11:38:30 2021

@author: dhtmd
"""

from tkinter import *


def fa():
    if e2.get() != "":
        e2.delete(0,len(str(e2.get())))
    e2.insert(0,c_to_f(e1.get()))


def c_to_f(c_value):
    return ((9/5) * float(c_value)) +32

def af():
    if e1.get() != "":
        e1.delete(0,len(str(e1.get())))
    e1.insert(0,f_to_c(e2.get()))


def f_to_c(f_value):
    return (float(f_value)-32) * 5/9


window = Tk()
window.title("섭씨를 화씨로 변경")
window.geometry("500x200")
window.resizable(False, False)

l1 = Label(window, text="섭씨")
l2 = Label(window, text="화씨")

l1.pack()
l2.pack()
l1.place(x=100,y=0)
l2.place(x=100,y=20)
e1 = Entry(window)
e2 = Entry(window)
e1.pack()
e2.pack()
b1 = Button(window,text="섭씨 -> 화씨", command=fa)
b1.pack()
b2 = Button(window,text="화씨 -> 섭씨", command=af)
b2.pack()
window.mainloop()