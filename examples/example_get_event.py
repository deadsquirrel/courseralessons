# !/usr/bin/env/python
# -*- coding: utf-8 -*-
# example
# get-method for processing different types of data.


def display(event):
     v = var.get()
     if v == 0:
          print ("Включена первая кнопка")
     elif v == 1:
          print ("Включена вторая кнопка")
     elif v == 2:
          print ("Включена третья кнопка")
 
but = Button(root,text="Получить значение")
but.bind('<Button-1>',display) 
