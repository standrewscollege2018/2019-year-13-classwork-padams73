# this program is an inefficient way of having two buttons count up or down

from tkinter import *
root = Tk()
root.title("Count up, count down")

def add():
    """ This function adds one to the number and prints it. """

    number += 1
    print(number)
    
def subtract():
    """ This function subtracts one from the number and prints it. """

    number -= 1
    print(number)

# set the starting value
number = 0
# add buttons
add_button = Button(root, text="Add 1", command=add).grid()
subtract_button = Button(root, text="Subtract 1", command=subtract).grid()

root.mainloop()