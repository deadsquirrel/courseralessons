# !/usr/bin/env/python
# -*- coding: utf-8 -*-
# example
# blank dialog with text field

from Tkinter import *
from Tkinter.filedialog import *
 
root = Tk()
txt = Text(root,width=40,height=15,font="12")
txt.pack()
 
op = askopenfilename()
 
root.mainloop() 
