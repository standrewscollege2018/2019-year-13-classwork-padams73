# this program shows how to update a label using a function called by a button

from tkinter import *

root = Tk()
root.geometry('300x200')
def update_label():
    """ This function updates the label. """
    
    label_var.set("Double the number is "+str(entry_var.get()*2))

# add an entry field for user to type in content
# Always set the variable first, this stores whatever the user enters
entry_var = IntVar()
entry = Entry(root, textvariable = entry_var).grid()


# this button calls the update_label function
update_btn = Button(root, text="Click me", command=update_label).grid()

# Set up the label
# first we define the variable that will contain the label content
label_var = StringVar()
label_var.set("Click on the button")
# next we add the label, setting the textvariable
label = Label(root, textvariable=label_var).grid()


root.mainloop()