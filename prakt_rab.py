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

varcomm = Label(root, text="Сколько штук?", font="Arial 14")
var=IntVar()
var.set(1)
rad0 = Radiobutton(root,text="0-10",variable=var,value=0)
rad1 = Radiobutton(root,text="11-20",variable=var,value=1)
rad2 = Radiobutton(root,text="21-30",variable=var,value=2) 
rad3 = Radiobutton(root,text="31-40",variable=var,value=3) 

lab.pack()
ent.pack()
comm.pack()
tex.pack()
varcomm.pack()


root.mainloop()
