# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 13:39:30 2021

@author: dhtmd
"""

import tkinter as tk


def calculate(event):
    value = tk.Entry.get(display)
    if value != "":
        result = eval(value)
        display.delete(0,tk.END)
        display.insert(0,result)
        
def clear(event):
    display.delete(0,tk.END)


window = tk.Tk()
window.title("계산기")
window.geometry("300x300")

display = tk.Entry(window, width=20)
display.pack()

b1 = tk.Button(window, text="=", width = 5)
b1.bind("<Button-1>", calculate)
b1.pack()

b_c = tk.Button(window, text = "C", width = 5)
b_c.bind("<Button-1>",clear)
b_c.pack()

window.bind("<Return>", calculate)
window.bind("<Escape>", clear)

window.mainloop()