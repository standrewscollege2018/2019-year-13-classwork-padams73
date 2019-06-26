# this program is an inefficient way of having two buttons count up or down

from tkinter import *
root = Tk()
root.title("Count up, count down")

def change_number(change):
    """ This function changes the number and prints it. """
    
    global number
    number += change
    print(number)
    
# set the starting value
number = 0
# add buttons
add_button = Button(root, text="Add 1", command= lambda: change_number(1)).grid()
subtract_button = Button(root, text="Subtract 1", command= lambda: change_number(-1)).grid()

root.mainloop()