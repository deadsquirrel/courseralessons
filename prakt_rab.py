# -*- coding: utf-8 -*-
from Tkinter import *

    
root = Tk()
'''
but = Button(root,
          text="Печать", 
          width=30,height=5,
          bg="white",fg="red")
'''

lab = Label(root, text="Ваш адрес:", font="Arial 16")

ent = Entry(root,width=20,bd=3)
comm = Label(root, text="Комментарий:", font="Arial 16")

tex = Text(root,width=20,height=6,
          font="Verdana 12",
          wrap=WORD) 


lab.pack()
ent.pack()
comm.pack()
tex.pack()

root.mainloop()
