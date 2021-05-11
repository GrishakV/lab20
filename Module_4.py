#!/usr/bin/env python3
# -*- config: utf-8 -*-

from tkinter import *

root = Tk()

c = Canvas(root, width=800, height=800, bg='white')
c.pack()

c.create_polygon(400, 100, 100, 300, 700, 300, fill='lightblue', outline='lightblue')
c.create_rectangle(200, 300, 600, 700, fill='lightblue', outline='lightblue')
c.create_oval(650, 50, 750, 150, fill='yellow', outline='yellow')

a = 0
while a < 1000:
    c.create_arc(a, 675, a+25, 930,
                 start=180, extent=-100,
                 style=ARC, outline='darkgreen',
                 width=3)
    a += 25

root.mainloop()
