# this file demonstrates how to create buttons for each item in a list
# also how to send different parameters to a function

from tkinter import *
# we need to import partial to get the buttons to work
from functools import partial

def print_team(selected_team):
    """ Prints name of selected team. """
    
    print("You selected", selected_team)

root = Tk()
root.title("Buttons in loop")
root.geometry('600x400')

team_list = ["Crusaders", "Chiefs", "Blues", "Highlanders", "Hurricanes"]

col = 0
for team in team_list:
    # to send parameters to a function from a button within a loop, we use partial
    # this takes two inputs: the name of the function, and the variable
    button = Button(root, text=team, width=15, command=partial(print_team, team)).grid(row=0,column=col)
    col += 1



root.mainloop()