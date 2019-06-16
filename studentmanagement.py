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

    def get_classes(self):
        """ This function returns the class list of the student. """
    
        return self._classes       

    def display_details(self):
        """ This function displays all of the details of a student, nicely formatted. """
        
        print("\n-----------------------")
        print("Student: {}".format(self._name))
        print("Age: ", self._age)
        print("Phone: ", self._phone)
        classlist = ""
        for c  in self._classes:
            classlist += c + " "
        print("Classes: ", classlist)
        
        

def print_names():
    """ This function loops through student_list and prints out the names of all students. """
    
    for s in student_list:
        print(s.get_name())

def display_enrolled():
    """ This function gets all details about all students by looping through the student_list list and
    calling the display_details function for each student that is enrolled."""

    for s in student_list:
        if s.get_enrolled():
            s.display_details()

def check_age():
    """ This function asks the user to enter an age and it returns details of all enrolled students
    who are that age or older. """
    
    age = int(input("Enter age of student:"))
    for student in student_list:
        if student.get_age() >= age:
            student.display_details()


def generate_students():
    """ This function imports students from myRandomStudents.csv. """
    
    import csv
    with open('myRandomStudents.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile)
        for line in filereader:
            classes=[]
            i=4
            while i in range(4, 9):
                classes.append(line[i])
                i+=1
            Student(line[0], int(line[1]), line[2],line[3], classes)

def class_counter():
    """ This function returns the number of students belonging to the selected class. """
    
    class_code = input("What class are you looking for? ")
    counter = 0
    for s in student_list:
        if class_code in s.get_classes():
            counter += 1
    print("Class count: ", counter)

# student_list will store all Student objects
student_list = []

# create student records
Student("Jack", 15, "27512343", "Male", ["DVC", "MTH"])
Student("Jill", 16, "35673214", "Female", ["MTH", "AGR"])

generate_students()
class_counter()
