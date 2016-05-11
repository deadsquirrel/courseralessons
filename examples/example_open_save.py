# for python3 
# module filediialog for python3
# lesson 11


from tkinter import *
from tkinter.filedialog import *
 
root = Tk()
op = askopenfilename()
sa = asksaveasfilename()
 
root.mainloop()
