""" This program shows how to populate a listbox with multiple columns. It uses ttk and the treeview widget."""

from tkinter import *
from tkinter import ttk

class Pizza():
    """ Objects in this class have two attributes, name and price. """
    
    def __init__(self, name, price):
        """ Set up the new object with a name and price. Also add the pizza to the pizzas list. """
        
        self._name = name
        self._price = price
        pizzas.append(self)

    def get_name(self):
        """ Returns the name of the pizza. """
        
        return self._name
    
    def get_price(self):
        """ Returns the price of the pizza. """
        
        return self._price


root = Tk()
root.geometry('300x300')

    
# list to store all pizza objects
pizzas = []

# Create the pizza objects
Pizza("Pepperoni", 20)
Pizza("Hawaiian", 15)
Pizza("Cheese", 12)

# set up the treeview widget.
# make sure you grid() it on a different line or it won't work
tree = ttk.Treeview(root, columns=('Pizza', 'Price'))
tree.column('Pizza', width=100, anchor='w')
tree.heading('Pizza', text='Pizza')
tree.column('Price', width=50, anchor='w')
tree.heading('Price', text='Price')
tree.grid()

# to add object names to the listbox we use insert(), looping through the list and call the get_name function
number = 1
for p in pizzas:
    
    tree.insert('', 'end', number, text=number)
    tree.insert(number, 0, p.get_name(), text=p.get_name())
    number += 1



# Add a label to display the total cost
# It will need an IntVar() to store the cost
total_cost = IntVar()
total_cost.set(0)
cost_lbl = Label(root, textvariable=total_cost).grid()

root.mainloop()