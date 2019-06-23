# This file gives a basic introduction to creating a GUI in Python using Tkinter

# Start by importing the tkinter library
from tkinter import *
# create the root window
root = Tk()
# we can set attributes for the root window
root.title("Intro to Tkinter")
root.geometry('600x400')
# to change the background colour, use root.configure
root.configure(background='fuchsia')

# Create a label
# Note that width is in the number of characters, not percentage or pixels
the_label = Label(root, text="Welcome to Tkinter", fg='fuchsia', bg='#123456', width=30)
# to make widgets appear we can use either pack() or grid()
# grid() takes row and column location as parameters. We can also set widgets to span multiple columns
the_label.grid(row=0, column=0, columnspan=2)

# Creating a username and password form
# By default, widgets align to the centre in columns, so use sticky to change alignment.
# We use compass bearings, N, E, S and W for top, right, bottom and left
user_label = Label(root, text="Username").grid(row=1, column=0, sticky=W)
pass_label = Label(root, text="Password").grid(row=2, column=0, sticky=W)

user_entry = Entry(root).grid(row=1, column=1, sticky=W)
pass_entry = Entry(root).grid(row=2, column=1, sticky=W)

# To keep the program running we need to set the root window run indefinitely
root.mainloop()