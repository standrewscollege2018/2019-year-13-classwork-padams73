# This file provides an introduction to creating GUIs using the Tkinter library

# to start, we import the Tkinter library
from tkinter import *

# create the root window for our GUI
root = Tk()
# we can set attributes for the root window such as title and size
root.title("Intro to Tkinter")
root.geometry('600x400')
# to change the background colour, use root.configure
root.configure(background='#123456')

# create a label
# we can configure the text by setting the bg colour, fg (text) colour, font, and so on
welcome_label = Label(root, text="Welcome to Tkinter!", bg='#123456', fg='#ffffff', font=('Calibri', 20)).grid(row=0, columnspan=2)

# create a basic login form
# to align grid content, we use sticky, with N, E, S, W for top, right, bottom, left
user_label = Label(root, text="Username", bg='#123456', fg='#ffffff', font=('Calibri', 14)).grid(row=1, column=0, sticky=W)
user_entry = Entry(root).grid(row=1, column=1)
pass_label = Label(root, text="Password", bg='#123456', fg='#ffffff', font=('Calibri', 14)).grid(row=2, column=0, sticky=W)
pass_entry = Entry(root).grid(row=2, column=1)

# to ensure the program runs indefinitely, start running a loop
root.mainloop()
