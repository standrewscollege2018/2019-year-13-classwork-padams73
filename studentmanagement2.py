# Student management program

class Student:
    """ This class contains information about students, setting their name and age. It also has functions
    for returning the name and age. """
    
    def __init__(self, name, age):
        """ This function sets the name and age for the new student. """
        
        self._name = name
        self._age = age

    def get_age(self):
        """ This function returns the age of the student. """
        
        return self._age

    def get_name(self):
        """ This function returns the name of the student. """
        
        return self._name

def display_info():
    """ This function prints out the names of all students. """
    
    print("{} is {} years old".format(student1.get_name(), student1.get_age()))
    print("{} is {} years old".format(student2.get_name(), student2.get_age()))

student1 = Student("Jack", 15)
student2 = Student("Jill", 16)

display_info()
