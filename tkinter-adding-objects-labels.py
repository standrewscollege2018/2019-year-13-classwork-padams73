""" This program shows how to add a new object using an Entry field, updating the label displaying
all of the objects. """

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

def add_pizza():
    """ This function adds a new Pizza object. It then calls the update_label() function. """
    
    Pizza(new_name.get(), new_price.get())
    update_label()

def update_label():
    """ This function updates the label, displaying all pizzas. """
    
    pizza_lbl_content.set("")
    # loop through the list of pizzas, get the names, and add them to the label variable
    for p in pizzas:
        pizza_lbl_content.set(pizza_lbl_content.get() + p.get_name() + " $" + str(p.get_price()) + "\n")
           

root = Tk()
root.geometry('300x300')

    
# list to store all pizza objects
pizzas = []

# Create the pizza objects
Pizza("Pepperoni", 20)
Pizza("Hawaiian", 15)
Pizza("Cheese", 12)

# Labels and entry fields to type in new Pizza name and price
new_pizza_lbl = Label(root, text="New pizza name").grid(row=0, column=0)
new_price_lbl = Label(root, text="New pizza price").grid(row=1, column=0)
new_name = StringVar()
new_price = IntVar()
new_pizza_entry = Entry(root, textvariable=new_name).grid(row=0, column=1)
new_price_entry = Entry(root, textvariable=new_price).grid(row=1, column=1)

# Button to call the update_label() function
update_btn = Button(root, text="Add pizza", command=add_pizza).grid(row=2)

# set up label
# because the content is dynamic, we need a variable to contain the content
pizza_lbl_content = StringVar()
 
pizza_lbl = Label(root, textvariable=pizza_lbl_content).grid(row=3)

# When program starts we call the update_label() function to display all pizzas on the menu
update_label()

root.mainloop()