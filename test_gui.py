# -*- coding: utf-8 -*-
from Tkinter import *

def printer(event):
    print ("AND AGAIN 'Hello world!'")

def printer2(event):
    print ("Ha-Ha!'")
    
root = Tk()

'''
ent = Entry(root,width=20,bd=3)
'''

but = Button(root,
          text="Это кнопка", 
          width=30,height=5,
          bg="white",fg="red")


'''
tex = Text(root,width=40,
          font="Verdana 12",
          wrap=WORD)
'''

butt = Button(root,
          text="Это еще\n одна кнопка", 
          width=35,height=15,
          bg="yellow",fg="green")
'''
#examples:
but = Button(root, text="PRINTING")
but = Button(root,
          text="Это кнопка", #надпись на кнопке
          width=30,height=5, #ширина и высота
          bg="white",fg="blue") #цвет фона и надписи
'''

lab = Label(root, text="Это метка! \n Из двух строк.", font="Arial 18")

# click left button of mouse - <Button-1>
# relations (binding) events and function
but.bind("<Button-1>", printer)
butt.bind("<Button-1>", printer2)

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
but.pack()
butt.pack()

# visibility of window
root.mainloop()
