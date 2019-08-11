""" This program shows how to populate a listbox with the names of objects. It also allows the user
to select multiple items, then when a button is clicked it displays the name of the selected item(s).
It also displays a total price by adding prices of all items selected. """

from tkinter import *
from tkinter import messagebox

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

def reorder():
    """ This function sorts the list of pizzas by price. It gets the price by calling get_price() and 
    once the list is sorted it calls the update_label function to change the display. """
    
    pizzas.sort(key=lambda x: x.get_price(), reverse=False)
    update_label()
    


def update_label():
    """ This function updates the list_of_pizzas variable, changing the list that is displayed in the
    label. """
    
    list_of_pizzas.set("")
    for pizza in pizzas:
        list_of_pizzas.set(list_of_pizzas.get() + pizza.get_name() + str(pizza.get_price()) + "\n")

root = Tk()
root.geometry('300x300')

    
# list to store all pizza objects
pizzas = []

# Create the pizza objects
Pizza("Pepperoni", 20)
Pizza("Hawaiian", 15)
Pizza("Cheese", 12)

# Label to display the pizzas
list_of_pizzas = StringVar()
pizza_lbl = Label(root, textvariable=list_of_pizzas).grid(row=0, column=1, sticky=N)

# Button to reorder the list
reset_btn = Button(root, text="Re-order list", command=reorder).grid(row=3, column=0)

update_label()
root.mainloop()