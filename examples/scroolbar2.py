# -*- coding: utf-8 -*-
from Tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

mainloop()


'''
from Tkinter import *
 
root = Tk()
 
tx = Text(root,width=10,height=10,font='14')
scr = Scrollbar(root,command=tx.yview)
tx.configure(yscrollcommand=scr.set)
 
tx.grid(row=0,column=0)
scr.grid(row=0,column=1)

root.mainloop()
'''
