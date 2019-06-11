# This is another introduction to Object Orientation

class Enemy:
    """ This class contains all the enemies that we will fight. It has attributes for life and name,
    as well as functions that decrease its health and check its life. """
    
    def __init__(self, name, life):
        """ The init function runs automatically when a new object is created. It sets the name and
        life of the new object. """
    
        self._name = name
        self._life = life
        
    
    def attack(self, damage):
        """ This function runs when the enemy is attacked. It prints Ouch and decreases life by 1. """
        
        print("Ouch")
        self._life -= damage
        
    def checkLife(self):
        """ This function checks the amount of life left. If less than zero it prints I am dead, 
        otherwise it prints the life left. """
        
        if self._life <= 0:
            print("I am dead")
        else:
            print(self._name, "Life:", self._life)
            
# To create an instance of a class, we set it as a variable
enemy1 = Enemy("Dr Evil", 10)
enemy2 = Enemy("Gru", 5)

# To call a function, we use "dot syntax", the name of the variable followed by a dot and then the function
enemy1.attack(5)
enemy1.checkLife()

        