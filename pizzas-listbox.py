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

def update_order():
    """ This function gets the selected pizzas, retrieves their prices and adds them to the total cost."""
    
    for i in listbox.curselection():
        total_cost.set(total_cost.get() + pizzas[i].get_price())

root = Tk()
root.geometry('300x300')

    
# list to store all pizza objects
pizzas = []

# Create the pizza objects
Pizza("Pepperoni", 20)
Pizza("Hawaiian", 15)
Pizza("Cheese", 12)

# Set up our listbox. Make sure you put the .grid() on a new line
listbox = Listbox(root, selectmode=EXTENDED)
listbox.grid()

# loop through the list of pizza objects and get each name, inserting into the listbox
for p in pizzas:
    listbox.insert(END, p.get_name())

# button to update the order
select_btn = Button(root, text="Select", command=update_order).grid()

# Label to display the total cost of the order
total_cost = IntVar()
total_cost.set(0)
cost_lbl = Label(root, textvariable=total_cost).grid()

root.mainloop()