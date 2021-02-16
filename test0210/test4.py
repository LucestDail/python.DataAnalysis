# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 07:57:44 2021

@author: myung
"""

from tkinter import *

def select() :
    select = "당신은 " + str(r.get()) + "번 선택"
    show.config(text = select)
    
window = Tk() 

window.title("새로운 창")      
window.geometry("640x400+100+100")  

r = IntVar()
lb = Label(text="좋아하는 음식")
lb.pack()

r1 = Radiobutton(window,text='1.피자' ,variable=r,value="1", command=select)
r1.pack(anchor=W)
r2 = Radiobutton(window,text='2.스테이크' ,variable=r,value="2", command=select)
r2.pack(anchor=W)
r3 = Radiobutton(window,text='3.파스타' ,variable=r,value="3", command=select)
r3.pack(anchor=W)

show = Label(window)
show.pack()

window.mainloop() 