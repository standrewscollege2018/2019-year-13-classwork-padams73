# Student management program

class Student:
    """ This class contains information about students, setting their name and age. It also has functions
    for returning the name and age. """
    
    def __init__(self, name, age, phone, gender, classes):
        """ This function sets the name and age for the new student. """
        
        self._name = name
        self._age = age
        self._enrolled = True
        self._phone = phone
        self._gender = gender
        self._classes = classes
        
        # add new student to student_list
        student_list.append(self)

    def get_age(self):
        """ This function returns the age of the student. """
        
        return self._age

    def get_name(self):
        """ This function returns the name of the student. """
        
        return self._name

    def get_phone(self):
        """ This function returns the phone of the student. """
        
        return self._phone
    
    def get_gender(self):
        """ This function returns the name of the student. """
        
        return self._gender
    
    def get_classes(self):
        """ This function returns the name of the student. """
        
        return self._classes    

    def info_summary(self):
        """ This function displays all the information for a student in a nicely formatted way. """
        
        print("------------------------")
        print("Student:", self._name)
        print(self._classes)


def display_info():
    """ This function loops through student_list and prints out the names of all students. """
    
    for student in student_list:
        print(student.get_name())

def display_enrolled():
    """ This function displays details of all enrolled students. """
    
    for student in student_list:
        if student.get_enrolled():
            print(student.get_name())

# list to store all student objects
student_list = []

# add new students
Student("Jack", 15, 271234567, "Male", ["MTH", "SCI"])
Student("Jill", 16, 219876787, "Female", ["AGR", "DVC"])

display_info()