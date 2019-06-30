# This program demonstrates how to create a listbox using Tkinter

from tkinter import *

root = Tk()
root.geometry('300x200')

# we need a list of items to be displayed in the listbox
names = ["Archie", "Baz", "Chuck"]

# first, we set the listbox. Note that the grid() command MUST go on a separate line.
listbox = Listbox(root, selectmode=SINGLE)
listbox.grid()

# next, we loop through the list and insert each item into the listbox. The END parameter appends the item
for name in names:
    listbox.insert(END, name)

root.mainloop()