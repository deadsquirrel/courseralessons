#lesson 11

from Tkinter import *
from Tkinter.filedialog import *
import fileinput
 
def _open():
     op = askopenfilename()
     for l in fileinput.input(op):
          txt.insert(END,l)
 
root = Tk()
 
m = Menu(root)
root.config(menu=m)
 
fm = Menu(m)
m.add_cascade(label="File",menu=fm)
fm.add_command(label="Open...",command=_open)
 
txt = Text(root,width=40,height=15,font="12")
txt.pack()

# add
def _save():
     sa = asksaveasfilename()
     letter = txt.get(1.0,END)
     f = open(sa,"w")
     f.write(letter)
     f.close()

root.mainloop() 
