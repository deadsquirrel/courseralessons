# -*- coding: utf-8 -*-
from Tkinter import *
 
root = Tk()
 
fra1 = Frame(root,width=500,height=100,bg="darkred")
fra8 = Frame(root,width=500,height=50,bg="red")
fra2 = Frame(root,width=200,height=20,bg="green",bd=20)
fra3 = Frame(root,width=6500,height=150,bg="darkblue", bd = 30)
fra4 = Frame(root,width=187,height=50,bg="blue")
fra7 = Frame(root,width=450,height=50,bg="lightblue")
fra5 = Frame(root,width=200,height=100,bg="yellow")
fra6 = Frame(root,width=200,height=50,bg="darkgreen")
fra10 = Frame(root,width=400,height=15,bg="black")
fra9 = Frame(root,width=200,height=50,bg="brown")
fra11 = Frame(root,width=500,height=50,bg="black")
fra12 = Frame(root,width=400,height=50,bg="grey")
fra13 = Frame(root,width=400,height=50,bg="lightyellow")
fra14 = Frame(root,width=400,height=50,bg="white")
fra15 = Frame(root,width=400,height=50,bg="orange")
fra16 = Frame(root,width=375,height=37,bg="violet")
fra17 = Frame(root,width=375,height=37,bg="pink")
fra187 = Frame(root,width=375,height=37,bg="purple")
fra1897 = Frame(root,width=375,height=90,bg="red")


ent1 = Entry(fra2,width=20)
ent2 = Entry(fra3,width=30)

#Свойства:
#    orient определяет направление шкалы;
#    length – длина шкалы в пикселях;
#    from_ и to – с какого значения шкала начинается и каким заканчивается
# (т. е. диапазон значений);
#    tickinterval – интервал, через который отображаются метки для шкалы;
#    resolution - минимальная длина отрезка, на которую пользователь может
# передвинуть движок.
sca1 = Scale(fra3,orient=HORIZONTAL,length=300,
          from_=0,to=100,tickinterval=10,resolution=5)
sca2 = Scale(fra7,orient=VERTICAL,length=400,
          from_=1,to=2,tickinterval=0.1,resolution=0.1) 


fra1.pack()
fra8.pack()
fra2.pack()
fra6.pack()
fra3.pack()
fra4.pack()
fra7.pack()
fra5.pack()
fra9.pack()
fra10.pack()
fra11.pack()
fra12.pack()
fra13.pack()
fra15.pack()
fra14.pack()
fra16.pack()
fra17.pack()
fra187.pack()
fra1897.pack()

ent1.pack()
ent2.pack()
sca1.pack()
sca2.pack()

root.mainloop()
