# !/usr/bin/env/python
# -*- coding: utf-8 -*-
# example
# blank dialog

from Tkinter import *
from Tkinter.filedialog import *
 
root = Tk()
op = askopenfilename()
sa = asksaveasfilename()
 
root.mainloop()
