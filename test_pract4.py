# -*- coding: utf-8 -*-
from Tkinter import *

root = Tk()

fra1 = Frame(root,width=350,height=100,bg="light green", bd=20)
fra2 = Frame(root,width=150,height=100,bg="dark green", bd=20)


sca1 = Scale(fra1,orient=HORIZONTAL,length=300,
             from_=0,to=100,tickinterval=10,resolution=10)
#sca2 = Scale(root,orient=VERTICAL,length=400,
#          from_=1,to=2,tickinterval=0.1,resolution=0.1)

ent1 = Entry(fra2,width=10)

fra1.pack()
sca1.pack()
fra2.pack()
ent1.pack()
#sca2.pack()
root.mainloop() 
