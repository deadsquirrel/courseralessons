from Tkinter import *
 
root = Tk()
 
fra1 = Frame(root,width=500,height=100,bg="darkred")
fra2 = Frame(root,width=300,height=200,bg="green",bd=20)
fra3 = Frame(root,width=500,height=150,bg="darkblue")
fra4 = Frame(root,width=300,height=50,bg="blue")
fra5 = Frame(root,width=200,height=100,bg="yellow")
 
fra1.pack()
fra2.pack()
fra3.pack()
fra4.pack()
fra5.pack()

root.mainloop() 
