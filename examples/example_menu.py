# !/usr/bin/env/python
# -*- coding: utf-8 -*-
# example
# 

from Tkinter import *
root = Tk()
 
m = Menu(root) #создается объект Меню на главном окне
root.config(menu=m) #окно конфигурируется с указанием меню для него
fm.add_command(label="New",command=new_win)

fm = Menu(m) #создается пункт меню с размещением на основном меню (m)
m.add_cascade(label="File",menu=fm) #пункту располагается на основном меню (m)
fm.add_command(label="Open...") #формируется список команд пункта меню
#fm.add_command(label="New")
fm.add_command(label="New",command=new_win)
fm.add_command(label="Save...")
#fm.add_command(label="Exit")
fm.add_command(label="Exit",command=close_win)
 
hm = Menu(m) #второй пункт меню
m.add_cascade(label="Help",menu=hm)
hm.add_command(label="Help")
#hm.add_command(label="About")
hm.add_command(label="About",command=about) 
 
nfm = Menu(fm)
fm.add_cascade(label="Import",menu=nfm)
nfm.add_command(label="Image")
nfm.add_command(label="Text")

def new_win():
     win = Toplevel(root)
 
def close_win():
     root.destroy()
 
def about():
     win = Toplevel(root)
     lab = Label(win,text="Это просто программа-тест \n меню в Tkinter")
     lab.pack() 
 

root.mainloop() 
