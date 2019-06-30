# this program shows how to combine objects with a TKinter label

from tkinter import *
root = Tk()
root.geometry('300x300')

class Pizza():
    """ Pizza objects have two attributes, name and price. """
    
    def __init__(self, name, price):
        """ This function creates a new pizza object and assigns the name and price attributes. """
        
        self._name = name
        self._price = price
        pizzas.append(self)
        
    def get_name(self):
        
        return self._name

pizzas = []
Pizza("Pepperoni", 20)
Pizza("Hawaiian", 15)

# set up the label
label_var = StringVar()
label_text = ""
for pizza in pizzas:
    label_text = label_text + pizza.get_name() + "\n"
label_var.set(label_text)
pizza_label = Label(root, textvariable=label_var).grid()


root.mainloop()