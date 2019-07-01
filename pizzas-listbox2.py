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
    """ This function gets the indices of the selected pizza(s), then gets the price for each one and
    adds it to the total_cost variable. """
    
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

# set up out listbox. selectmode can be SINGLE, MULTIPLE or EXTENDED.
# make sure you grid() it on a different line or it won't work
listbox = Listbox(root, selectmode=SINGLE)
listbox.grid()

# to add object names to the listbox we use insert(), looping through the list and call the get_name function
for p in pizzas:
    detail = p.get_name() + " $" + str(p.get_price())
    listbox.insert(END, detail)

# Add a button to update the cost of the order
# It will need to call a function that takes the selected pizza and gets its price, adding it to total_cost
select_btn = Button(root, text="Select", command=update_order).grid()

# Add a label to display the total cost
# It will need an IntVar() to store the cost
total_cost = IntVar()
total_cost.set(0)
cost_lbl = Label(root, textvariable=total_cost).grid()

root.mainloop()