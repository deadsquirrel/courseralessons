# -*- coding: utf-8 -*-
from Tkinter import *
 
root = Tk()
 
tx = Text(root,width=40,height=30,font='14')
scr = Scrollbar(root,command=tx.yview)
tx.configure(yscrollcommand=scr.set)
 
tx.grid(row=0,column=0)
scr.grid(row=0,column=1)
root.mainloop() 
