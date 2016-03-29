# -*- coding: utf-8 -*-
from Tkinter import *

def printer(event):
    print ("AND AGAIN 'Hello world!'")

root = Tk()
but = Button(root)
but["text"] = "Печать"
'''
#examples:
but = Button(root, text="PRINTING")
but = Button(root,
          text="Это кнопка", #надпись на кнопке
          width=30,height=5, #ширина и высота
          bg="white",fg="blue") #цвет фона и надписи
'''

# click left button of mouse - <Button-1>
# relations (binding) events and function
but.bind("<Button-1>", printer)

# visibility of button
but.pack()

# visibility of window
root.mainloop()
