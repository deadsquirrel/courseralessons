from Tkinter import *

def printer(event):
    print ("AND AGAIN 'Hello world!'")

root = Tk()
but = Button(root)
but["text"] = "PRINTING"
#but = Button(root, text="PRINTING")


# click left button of mouse - <Button-1>
# relations (binding) events and function
but.bind("<Button-1>", printer)

# visibility of button
but.pack()

# visibility of window
root.mainloop()
