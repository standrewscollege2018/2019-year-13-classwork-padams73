# This file covers a basic intro to Object Orientation

class Enemy:
    """ The Enemy class are the objects you will battle in the game. They store health and have
    functions that decrease their health and attack others. """
    
    def __init__(self, name, life):
        """ This functions automatically runs when a new instance is created.
        It sets the life of the enemy. """
    
        self._name = name
        self._life = life
        
    
    def attack(self, damage):
        """ This function is called when the enemy is attacked. It prints a message and 
        decreases _life by 1. """
        
        print("Ouch!")
        self._life -= damage
        
    def checkLife(self):
        """ This functions checks how much life the object has left. If zero it prints I am dead,
        otherwise it displays the life left"""
        
        if self._life <= 0:
            print("I am dead")
        else:
            print("{} has {} life left".format(self._name, self._life))
            
# To create an instance of a Class, we just set up a variable
enemy1 = Enemy("Dr Evil", 5)
enemy2=  Enemy("Gru", 10)

# to call a class function, we use the variable name followed by a dot, then the function name (dot syntax)
enemy1.attack(2)
enemy1.checkLife()

enemy2.attack(1)
enemy2.checkLife()
