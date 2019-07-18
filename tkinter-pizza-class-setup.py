""" This program shows how to populate a listbox with the names of objects. It also allows the user
to select multiple items, then when a button is clicked it displays the name of the selected item(s).
It also displays a total price by adding prices of all items selected. """

from tkinter import *

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


root.mainloop()