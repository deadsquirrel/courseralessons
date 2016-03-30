# -*- coding: utf-8 -*-
from Tkinter import *

    
def printer(event):
    print ("ok")
    
root = Tk()

but = Button(root,
             text="Отправить", font="Arial 16",
          width=20,height=2,
          bg="#74")

but.bind("<Button-1>", printer)

lab = Label(root, text="Ваш адрес:", font="Arial 16")

ent = Entry(root,width=20,bd=3)
comm = Label(root, text="Комментарий:", font="Arial 16")

tex = Text(root,width=20,height=6,
          font="Verdana 12",
          wrap=WORD)

varcomm = Label(root, text="Сколько штук?", font="Arial 12")
ccomm = Label(root, text="Какого цвета?", font="Arial 12")
var=IntVar()
var.set(1)
rad0 = Radiobutton(root,text="0-10",variable=var,value=0)
rad1 = Radiobutton(root,text="11-20",variable=var,value=1)
rad2 = Radiobutton(root,text="21-30",variable=var,value=2) 
rad3 = Radiobutton(root,text="31-40",variable=var,value=3) 

c1 = IntVar()
c2 = IntVar()
c3 = IntVar()
c4 = IntVar()
che1 = Checkbutton(root,text="RED",bg = "red",font = "Arial 12",
          variable=c1,onvalue=1,offvalue=0)
che2 = Checkbutton(root,text="BLUE",bg = "blue",font = "Arial 12",
          variable=c2,onvalue=2,offvalue=0) 
che3 = Checkbutton(root,text="GREEN",bg = "green",font = "Arial 12",
          variable=c1,onvalue=1,offvalue=0)
che4 = Checkbutton(root,text="YELLOW",bg = "yellow",font = "Arial 12",
          variable=c2,onvalue=2,offvalue=0) 


lab.pack()
ent.pack()
comm.pack()
tex.pack()
but.pack()
varcomm.pack()
rad0.pack()
rad1.pack()
rad2.pack()
rad3.pack()
ccomm.pack()
che1.pack()
che2.pack()
che3.pack()
che4.pack()

root.mainloop()
