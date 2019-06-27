# this program demonstrates how to get a value from an entry field and display it in a label

from tkinter import *

root = Tk()

def update_label():
    """ This function gets the entry field text and displays it in a label. """
    
    
    label_var.set(text_entered.get())
    
# add an entry field with a textvariable
# the text_entered variable holds the text that the user types into the entry field
text_entered = StringVar()
entry_field = Entry(root, textvariable=text_entered).grid()

# a button that calls the update_label function
update_button = Button(root, text="Click", command=update_label).grid()

# label that displays what we entered into the entry field
# label_var is initially empty so  nothing is displayed until button is clicked
label_var = StringVar()
label_var.set("")
label = Label(root, textvariable=label_var).grid()

root.mainloop()