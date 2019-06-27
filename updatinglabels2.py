# this program demonstrates how to change a label on the GUI by clicking a button

from tkinter import *

root = Tk()

def update_label():
    """ This function updates the value of the label. """
    
    label_var.set("You clicked the button")

# button to call a function that changes the label
update_btn = Button(root, text="Click me!", command=update_label).grid()

# set up the label
# start by setting the StringVar() to hold the label content
label_var = StringVar()
label_var.set("Click the button")

# now we add the label
label = Label(root, textvariable=label_var).grid()

root.mainloop()