# for python3 
# module filediialog for python3
# lesson 11


from tkinter import *
from tkinter.filedialog import *
import fileinput 
root = Tk()

txt = Text(root,width=40,height=15,font="12")
txt.pack()

op = askopenfilename()
#sa = asksaveasfilename()
for i in fileinput.input(op):
    txt.insert(END,i)
    
root.mainloop()
