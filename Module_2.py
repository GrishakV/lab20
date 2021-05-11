#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *

root = Tk()

ent1 = Entry()
lb1 = Listbox()

ent1.pack()
lb1.pack()
ent1.bind('<Return>', lambda e:  lb1.insert(0, ent1.get()))
lb1.bind('<Double-Button-1>', lambda e: ent1.insert(0, lb1.get(lb1.curselection())))

root.mainloop()
