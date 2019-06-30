""" This program demonstrates how to get the selection from a multiple selection listbox. When the button
is clicked a function prints the selections into the terminal as well as updating a label in the GUI. """

from tkinter import *

root = Tk()
root.geometry('300x300')

def display_selection():
    """ This function displays the selection. Since listbox curselection() returns a tuple (like a list)
    of results, we need to loop through it. Also, since it returns the indices of the item selected, 
    we then go back to the list and get the names at those locations. """
        
    # First, clear the old label value
    label_var.set("") 
    # Then, loop through curselection() and add the names
    for i in listbox.curselection():
        
        # to put each selection on a new line, add \n after each name
        label_var.set(label_var.get() + names[i] + "\n")
        print(names[i])
                  
    
# we need a list of items to be displayed in the listbox
names = ["Archie", "Baz", "Chuck"]

# first, we set the listbox. Note that the grid() command MUST go on a separate line.
listbox = Listbox(root, selectmode=MULTIPLE)
listbox.grid()

# next, we loop through the list and insert each item into the listbox. The END parameter appends the item
for name in names:
    listbox.insert(END, name)

# Here is the button that, when clicked, will call the display_selection function
select_btn = Button(root, text="Click me", command=display_selection).grid()

# Set up the label to display the selection
# Since the label text will change, we use a StringVar to store the content
label_var = StringVar()
label_var.set("Select someone")
select_lbl = Label(root, textvariable=label_var).grid()

root.mainloop()