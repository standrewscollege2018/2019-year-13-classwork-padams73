# this program demonstrates a button calling a function

from tkinter import *

def print_hello_world():
    """ This function prints hello world. """
    
    print("Hello world")

def hello(name):
    
    print("Hello", name)

root = Tk()
root.title("Hello world")

# add button to call function
# we use command to call the function
button = Button(root, text="Say hello", command=print_hello_world).grid()

# to send a parameter to a function we use lambda
hello_button = Button(root, text="Hello name", command= lambda: hello("Bob")).grid(row=1)

root.mainloop()