# this program demonstrates how buttons can call functions

from tkinter import *

def hello_world():
    """ This function prints hello world in the terminal. """
    
    print("Hello world")

def say_hello(name):
    """ This function receives the name and prints hello to that value. """
    
    print("Hello", name)
    
root = Tk()
root.title("Calling functions")

# this button calls the hello_world function by using command.
# note there are no brackets after the name of the function
# use this method if you are NOT passing a parameter to a function
hello_world_btn = Button(root, text="Say hello world", command=hello_world).grid()

# To pass a parameter to a function using a button, we use lambda
say_hello_btn = Button(root, text="Say hello", command= lambda: say_hello("Roberta")).grid(row=1)

root.mainloop()