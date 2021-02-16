# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 09:31:20 2021

@author: dhtmd
"""

from tkinter import *

def button_pressed(r):
    value = number_entry.get()
    if(r == "="):
        result = eval(value)
        print("수식",eval(value),"=",result)
        number_entry.delete(0,END)
        number_entry.insert(0,result)
    elif(r == "AC"):
        number_entry.delete(0,END)
    else:
        number_entry.insert(END,r)
        
#입력란
window = Tk()
window.title("calculator")
window.geometry("500x300")
number_entry = Entry(window, width=30,justify=RIGHT)
number_entry.grid(row=0, columnspan=4)
#버튼 배치 
Button(window, width=10, text="7",command=lambda:button_pressed("7")).grid(row=1,column=0)
Button(window, width=10, text="8",command=lambda:button_pressed("8")).grid(row=1,column=1)
Button(window, width=10, text="9",command=lambda:button_pressed("9")).grid(row=1,column=2)
Button(window, width=10, text="/",command=lambda:button_pressed("/")).grid(row=1,column=3)
Button(window, width=10, text="4",command=lambda:button_pressed("4")).grid(row=2,column=0)
Button(window, width=10, text="5",command=lambda:button_pressed("5")).grid(row=2,column=1)
Button(window, width=10, text="6",command=lambda:button_pressed("6")).grid(row=2,column=2)
Button(window, width=10, text="*",command=lambda:button_pressed("*")).grid(row=2,column=3)
Button(window, width=10, text="1",command=lambda:button_pressed("1")).grid(row=3,column=0)
Button(window, width=10, text="2",command=lambda:button_pressed("2")).grid(row=3,column=1)
Button(window, width=10, text="3",command=lambda:button_pressed("3")).grid(row=3,column=2)
Button(window, width=10, text="+",command=lambda:button_pressed("+")).grid(row=3,column=3)
Button(window, width=10, text="AC",command=lambda:button_pressed("AC")).grid(row=4,column=0)
Button(window, width=10, text="0",command=lambda:button_pressed("0")).grid(row=4,column=1)
Button(window, width=10, text="=",command=lambda:button_pressed("=")).grid(row=4,column=2)
Button(window, width=10, text="-",command=lambda:button_pressed("-")).grid(row=4,column=3)

window.mainloop()