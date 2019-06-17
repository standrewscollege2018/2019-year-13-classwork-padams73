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

# list to store all student objects
student_list = []

# add new students
Student("Jack", 15, 271234567, "Male", ["MTH", "SCI"])
Student("Jill", 16, 219876787, "Female", ["AGR", "DVC"])

generate_students()
check_age()