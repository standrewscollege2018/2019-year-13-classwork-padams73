# this program is a more efficient way of having two buttons count up or down

from tkinter import *
from functools import partial
root = Tk()
root.title("Count up, count down")

def change_number(change):
    """ This function changes the number and prints it. """
    
    global number
    number += change
    print(number)
    
# set the starting value
number = 0
# list of values to change number by
values = [1, -1,5,-5]

# add buttons
for value in values:
    # Setting some text to appear on each button
    textdisplay = "Change by "+str(value)
    button = Button(root, text=textdisplay, command=partial(change_number,value)).grid()

root.mainloop()