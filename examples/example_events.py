# !/usr/bin/env/python
# -*- coding: utf-8 -*-
# example
# mouse events
# keyboard events


from Tkinter import *
# mouse events
def b1(event):
     root.title("Left mouse-button")
def b3(event):
     root.title("Right mouse-button")
def move(event):
     root.title("mouses movies")
 
# keyboard events
def exit_(event):
     root.destroy()
def caption(event):
     t = ent.get()
     lbl.configure(text = t)
 
root = Tk()

# mouse events
root.minsize(width = 500, height=400)
 
root.bind('<Button-1>',b1)
root.bind('<Button-3>',b3)
root.bind('<Motion>',move)
 


# keyboard events
'''
* <Return> - нажатие клавиши Enter;
* <space>- пробел;
* etc
Сочетания клавиш пишутся через тире. Например:
* <Control-Shift> - одновременное нажатие клавиш Ctrl и Shift.
'''
ent = Entry(root, width = 40)
lbl = Label(root, width = 80)
 
ent.pack()
lbl.pack()
 
ent.bind('<Return>',caption)
root.bind('<Control-z>',exit_)
 
root.mainloop() 
