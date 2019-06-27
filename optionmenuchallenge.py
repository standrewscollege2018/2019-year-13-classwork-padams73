# option menu challenge - starter code

from tkinter import *

# set up root window
root = Tk()
root.title("Option menu challenge")
root.geometry('300x200')

def update_label():
    """ This function updates the label, stating which name was selected in the option menu.
    It does this by getting the value of the selection from the selected_name StringVar and 
    adding it to the label_var. """
    
    # add code here to update the label_var variable (which is displayed in our label)
    

# The list of names
names_list = ["James", "John", "Joanne"]

# Set up the option menu
# Start by setting the selected_name StringVar. Set the initial value to the first value of names_list

# Set up the option menu, with selected_name as the selected variable and names_list as the list to display


# The select_button calls the update_label function
select_button = Button(root, text="Select and press", command=update_label).grid()

# Set up the label
# Start by setting label_var as a StringVar and then setting the initial value to "Select a name"
label_var = StringVar()

# Set up the label, with label_var as the textvariable


# set mainloop so programs runs indefinitely
root.mainloop()