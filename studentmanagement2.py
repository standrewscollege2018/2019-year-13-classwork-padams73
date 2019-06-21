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

    def get_enrolled(self):
        """ This function returns whether a student is enrolled or not. """
        
        return self._enrolled   

    def info_summary(self):
        """ This function displays all the information for a student in a nicely formatted way. """
        
        print("------------------------")
        print("Student:", self._name)
        print("Age: ", self._age)
        print("Phone: ", self._phone)
        # format list of classes before we print it out
        classlist = ""
        for c in self._classes:
            classlist += c + " "
        print("Classes: ", classlist)


def display_info():
    """ This function loops through student_list and prints out the names of all students. """
    
    for student in student_list:
        print(student.get_name())

def display_enrolled():
    """ This function displays details of all enrolled students. """
    
    for student in student_list:
        if student.get_enrolled():
            student.info_summary()

def check_age():
    """ This function displays the details of all students who match the age selected. """
    
    # get user to enter age
    age = int(input("Enter age: "))
    # loop through student_list and called info_summary() for all students with that age
    for student in student_list:
        if student.get_age() == age:
            student.info_summary()

def class_count():
    """ This function counts how many students belong to a selected class. """
    
    counter = 0
    class_code = input("Enter class code: ")
    for student in student_list:
        if class_code in student.get_classes():
            counter += 1
    print("Class count:", counter)

def class_list():
    """ This function displays the names of all students belonging to a selected class. """
    
    # get class code to search for
    class_code = input("Enter class code: ")
    # set counter starting value
    counter = 0
    # loop through student list and check if students belong to the class
    for student in student_list:
        if class_code in student.get_classes():
            counter += 1
            print(student.get_name())
    print("Class count: ", counter)

def search():
    """ This function enables the user to search for a student by name. It returns all info about
    the student. It also returns results for any student name that contains the search criteria. """
    
    search_name = input("Enter name of student: ")
    counter = 0
    for student in student_list:
        if search_name.lower() in student.get_name().lower():
            student.info_summary()
            counter += 1
    print("{} result(s) found".format(counter))
                
    
def generate_students():
    """ This function imports details for students from myRandomStudents.csv. """
        
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

def add_student():
    """ This function creates a new student object. It gets the attributes from the user, including a
    list of classes they belong to, then calls the Student class. """
    
    new_name = input("Enter name: ")
    new_age = int(input("Enter age: "))
    new_phone = input("Enter phone number: ")
    new_gender = input("Enter gender (either Male or Female): ")
    new_classes = []
    print("Enter class codes")
    for i in range(5):
        new_class = input("Class {}:".format(i+1))
        new_classes.append(new_class)
    Student(new_name, new_age, new_phone, new_gender, new_classes)
    # Clear the new_classes list for the next student to be added
    new_classes =[]


# list to store all student objects
student_list = []

# add new students
Student("Jack", 15, 271234567, "Male", ["MTH", "SCI"])
Student("Jill", 16, 219876787, "Female", ["AGR", "DVC"])
generate_students()

"""This code runs the menu system that enables us to select which function to run
It runs repeatedly until the user selects Quit, when keep_running is set to False
and the program ends. """
keep_running = True
while keep_running == True:
    # Display user options
    print("1. Search for a student")
    print("2. Get class list")
    print("3. Age search")
    print("4. Add new student")
    print("5. Quit")
    # Use try and except to check that we are getting valid inputs from the user
    try:
        user_selection = int(input("Enter choice:"))
        if user_selection == 1:
            search()
        elif user_selection == 2:
            class_list()
        elif user_selection == 3:
            check_age()
        elif user_selection == 4:
            add_student()
        elif user_selection == 5:
            keep_running = False
        else:
            print("Error! You must enter a number from 1-4")
        
    except ValueError:
        print("Error! Please enter an integer from 1-4")
        
    
    
    


