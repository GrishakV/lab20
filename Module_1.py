#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *


def lb1move(event):
    select = list(lb1.curselection())
    select.reverse()
    for i in select:
        lb2.insert(0, lb1.get(i))
        lb1.delete(i)


def lb2move(event):
    select = list(lb2.curselection())
    select.reverse()
    for i in select:
        lb1.insert(0, lb2.get(i))
        lb2.delete(i)


shoplist = ['apple', 'bananas', 'carrot', 'bread', 'butter', 'meat', 'potato', 'milk', 'tomato', 'pineapple']

root = Tk()

lb1 = Listbox(width=30, height=15, selectmode=EXTENDED)
lb2 = Listbox(width=30, height=15, selectmode=EXTENDED)
btn1 = Button(text=">>>")
btn2 = Button(text="<<<")

lb1.grid(row=0, column=0, rowspan=4)
lb2.grid(row=0, column=3, rowspan=4)
btn1.grid(row=1, column=1, columnspan=2, sticky=S)
btn2.grid(row=2, column=1, columnspan=2, sticky=N)

for i in shoplist:
    lb1.insert(END, i)

btn1.bind('<Button-1>', lb1move)
btn2.bind('<Button-1>', lb2move)

root.mainloop()
