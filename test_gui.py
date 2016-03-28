from Tkinter import *

root = Tk()
but = Button(root)
but["text"] = "Печать"

def printer(event):
    print ("Как всегда очередной 'Hello world!'")

# click left button of mouse - <Button-1>
# relations (binding) events and function
but.bind("<Button-1>", printer)

# visibility of button
but.pack()

# visibility of window
root.mainloop()
