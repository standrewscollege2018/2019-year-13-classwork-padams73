""" This program demonstrates how to get the selection from a single selection listbox. When the button
is clicked a function prints the selection into the terminal as well as updating a label in the GUI. """

from tkinter import *

root = Tk()
root.geometry('300x300')

def display_selection():
    """ This function displays the selection. Since listbox curselection() returns a tuple (like a list)
    of results, we need to loop through it even though there is only one selection. Also, since it returns 
    the index of the item selected, we then go back to the list and get the name at that location. """
    
    for i in listbox.curselection():
        
        label_var.set(names[i])
        print(names[i])
                  
    

# we need a list of items to be displayed in the listbox
names = ["Archie", "Baz", "Chuck"]

# first, we set the listbox. Note that the grid() command MUST go on a separate line.
listbox = Listbox(root, selectmode=SINGLE)
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