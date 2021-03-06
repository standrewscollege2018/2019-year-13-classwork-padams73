""" This program shows how to populate a listbox with the names of objects. It also allows the user
to select multiple items, then when a button is clicked it displays the name of the selected item(s).
It also displays a total price by adding prices of all items selected. """

from tkinter import *
from tkinter import messagebox
from collections import Counter

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
        order_list.append(pizzas[i].get_name())
    
    # this part resets the list and then gets the quantities of each pizza by using a Counter
    order.set("")
    count = Counter(order_list)
    # print(count)  # uncomment this line and you will see the dictionary returned by Counter() printed in Terminal
    
    # the Counter function returns a dictionary, so we need to loop through it and get the key and value,
    # adding them to the order StringVar, adding a \n to make sure they are on a new line.
    for (key, value) in count.items():
        order.set(order.get() + key + " (" + str(value) + ")" + "\n")

def reset_order():
    """ This function is called by the reset_btn, and resets total_cost to zero, and clears the order label.
    It uses a Tkinter messagebox to check whether the user actually wants to do this. 
    messagebox.askyesno() returns either True (if you click yes) or False. """
    
    if messagebox.askyesno("Warning!", "Are you sure you want to clear the order?"):
        total_cost.set(0)
        order.set("")
        del order_list[:]

root = Tk()
root.geometry('300x300')

    
# list to store all pizza objects
pizzas = []

# list to store items in the order
order_list = []

# Create the pizza objects
Pizza("Pepperoni", 20)
Pizza("Hawaiian", 15)
Pizza("Cheese", 12)

# Menu label
menu_lbl = Label(root, text="Menu", font=('Calibri', 14)).grid(row=0, column=0)

# Set up our listbox. Make sure you put the .grid() on a new line
listbox = Listbox(root, selectmode=MULTIPLE)
listbox.grid(row=1, column=0)

# loop through the list of pizza objects and get each name, inserting into the listbox
for p in pizzas:
    details = p.get_name() + " $" + str(p.get_price())
    listbox.insert(END, details)

# button to update the order
select_btn = Button(root, text="Select", command=update_order).grid()

# Label to display the total cost of the order
total_cost = IntVar()
total_cost.set(0)
cost_lbl = Label(root, textvariable=total_cost).grid(row=3)

# Label to display the summary of the order
summary_lbl = Label(root, text="Summary", font=('Calibri', 14)).grid(row=0, column=1, sticky=N)
order = StringVar()
order_lbl = Label(root, textvariable=order).grid(row=1, column=1, sticky=N)

# Button to reset the order
reset_btn = Button(root, text="Reset order", command=reset_order).grid(row=4, column=0)

root.mainloop()