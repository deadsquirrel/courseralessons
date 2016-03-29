# -*- coding: utf-8 -*-
from Tkinter import *

def printer(event):
    print ("AND AGAIN 'Hello world!'")
    
root = Tk()

but = Button(root,
          text="Apply", 
          width=30,height=5,
          bg="white",fg="green")

ent = Entry(root,width=20,bd=3)

tex = Text(root,width=40,
          font="Verdana 12",
          wrap=WORD)

lab = Label(root, text="Это метка! \n Из двух строк.", font="Arial 18")

# click left button of mouse - <Button-1>
# relations (binding) events and function
but.bind("<Button-1>", printer)


#radiobutton
var=IntVar()
var.set(1)
rad0 = Radiobutton(root,text="Первая",
          variable=var,value=0)
rad1 = Radiobutton(root,text="Вторая",
          variable=var,value=1)
rad2 = Radiobutton(root,text="Третья",
          variable=var,value=2) 
#flags
c1 = IntVar()
c2 = IntVar()
che1 = Checkbutton(root,text="Первый флажок",
          variable=c1,onvalue=1,offvalue=0)
che2 = Checkbutton(root,text="Второй флажок",
          variable=c2,onvalue=2,offvalue=0) 


#ListBox
r = ['Linux','Python','Tk','Tkinter']
lis = Listbox(root,selectmode=SINGLE,height=4)
for i in r:
     lis.insert(END,i)

     

# visibility of button
lab.pack()
ent.pack()
tex.pack()
but.pack()


# visibility of window
root.mainloop()
