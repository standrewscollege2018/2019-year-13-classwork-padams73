# Student management program

class Student:
    """ This class contains information about students, setting their name and age. It also has functions
    for returning the name and age. """
    
    def __init__(self, name, age, phone, gender, classes):
        """ This function sets the name and age for the new student. """
        
        self._name = name
        self._age = age
        self._phone = phone
        self._enrolled = True
        self._gender = gender
        self._classes = classes
        # add Student to list of all students
        student_list.append(self)

    def get_age(self):
        """ This function returns the age of the student. """
        
        return self._age

    def get_name(self):
        """ This function returns the name of the student. """
        
        return self._name

    def get_enrolled(self):
        """ This function returns whether a student is enrolled. """
        
        return self._enrolled

    def display_details(self):
        """ This function displays all of the details of a student, nicely formatted. """
        
        print("\n-----------------------")
        print("Student: {}".format(self._name))
        print("Age: ", self._age)
        
        

def print_names():
    """ This function loops through student_list and prints out the names of all students. """
    
    for s in student_list:
        print(s.get_name())

def display_enrolled():
    """ This function gets all details about all students."""

    for s in student_list:
        if s.get_enrolled():
            s.display_details()

# student_list will store all Student objects
student_list = []

Student("Jack", 15, "27512343", "Male", ["DVC", "MTH"])
Student("Jill", 16, "35673214", "Female", ["MTH", "AGR"])


display_enrolled()
