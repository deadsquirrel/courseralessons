# !/usr/bin/python
# example
# mouse event
# -*- coding: utf-8 -*-


from Tkinter import *
def b1(event):
     root.title("Left mouse-button")
def b3(event):
     root.title("Right mouse-button")
def move(event):
     root.title("mouses movies")
 
root = Tk()
root.minsize(width = 500, height=400)
 
root.bind('<Button-1>',b1)
root.bind('<Button-3>',b3)
root.bind('<Motion>',move)
 
root.mainloop() 
