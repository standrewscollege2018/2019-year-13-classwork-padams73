# this program demonstrates how to use optionmenus

from tkinter import *

root = Tk()
root.geometry('300x200')

# List of names to display in option menu
names = ["John", "James", "Steve"]

# Set up option menu
# start with variable to store what has been selected
# you can set the initial selection value
selected_name = StringVar()
selected_name.set(names[0])

# When we create the OptionMenu we need to set the location, selected variable, and the list to display
names_menu = OptionMenu(root, selected_name, *names).grid()


root.mainloop()