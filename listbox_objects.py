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

def display_selection():
    """ This function displays the selection. Since listbox curselection() returns a tuple (like a list)
    of results, we need to loop through it. Also, since it returns the indices of the item selected, 
    we then go back to the list and get the names at those locations. """
        
    # Then, loop through curselection() and add the names by calling the get_name function
    for i in listbox.curselection():
        
        # to put each selection on a new line, add \n after each name
        label_var.set(label_var.get() + pizzas[i].get_name() + "\n")
        # we add the price of the selected pizza(s) and add it to the total_cost
        total_cost.set(total_cost.get()+pizzas[i].get_price())
        print(pizzas[i].get_name())
                  
# list to store all pizza objects
pizzas = []

# Create the pizza objects
Pizza("Pepperoni", 20)
Pizza("Hawaiian", 15)
Pizza("Cheese", 12)

# first, we set the listbox. Note that the grid() command MUST go on a separate line.
listbox = Listbox(root, selectmode=MULTIPLE)
listbox.grid()

# next, we loop through the list and insert each item into the listbox. The END parameter appends the item
for pizza in pizzas:
    listbox.insert(END, pizza.get_name())

# Here is the button that, when clicked, will call the display_selection function
select_btn = Button(root, text="Click me", command=display_selection).grid()

# Set up the label to display the selection
# Since the label text will change, we use a StringVar to store the content
label_var = StringVar()
select_lbl = Label(root, textvariable=label_var).grid()

# The final label displays the total price of the items selected
# Because the label will change value, we use an IntVar to store the value
total_cost = IntVar()
total_cost.set(0)
cost_lbl = Label(root, textvariable=total_cost).grid(row=0, column=1)

root.mainloop()