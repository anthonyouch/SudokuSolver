from tkinter import *
from time import sleep
root = Tk()

e = Entry(root)
e.insert(0, "Enter your name")
e.pack()

root.update()

def myClick():
    name = e.get()
    response = Label(root, text="Hello " + name)
    response.pack()

myButton = Button(root, text="Enter your name!", command=myClick)

myButton.pack()
root.mainloop()