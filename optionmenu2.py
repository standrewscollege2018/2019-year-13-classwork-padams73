# this program demonstrates how to create an option menu

from tkinter import *

root = Tk()
root.geometry('300x200')

# we need a list of items to display in the option menu
names = ["Angus", "Toby", "Liam", "Des"]

# Set up the option menu
# Start by defining a variable to hold whatever is selected
selected_name = StringVar()
# Set the initial value
selected_name.set(names[0])
# Add the option menu. We need to set the location, name of variable holding selection, name of list
name_menu = OptionMenu(root, selected_name, *names).grid()


root.mainloop()