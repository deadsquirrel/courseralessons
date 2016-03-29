from Tkinter import *

class But_print:
    def __init__(self):
        self.but = Button(root)
        self.but["text"] = "PRINTING"
        # click left button of mouse - <Button-1>
        # relations (binding) events and function
        self.but.bind("<Button-1>", printer)
        # visibility of button
        self.but.pack()
    def printer(event):
        print ("AND AGAIN 'Hello world!'")

root = Tk()
obj = But_print()
# visibility of window
root.mainloop()
