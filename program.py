from staff import Staff
from tutor import Tutor
from student import Student

class Program:
    def __init__(self):
        self.tutors = {}
        self.students = {}
        self.logged_in_as = ''
        self.logged_in_as_student = ''
        self.logged_in_as_tutor = ''

    def staff_login(self, id, password):
        staff = Staff()
        if id == staff.username and password == staff.password:
            self.logged_in_as = 'staff'
            return "Successfully logged in as staff"
    
    def staff_menu(self):
        print("\nWelcome to Staff Menu\n" + "-" * 25)
        print("Select a Staff Menu: \n0. Log Out\n1. Register a tutor \n2. Register a student\n3. Update a student subject\n4. Search Payment made by Student\n")

    def register_tutor(self, name, age, subject, phoneNumber):
        tutor = Tutor(name, age, subject, phoneNumber)
        self.tutors[name] = tutor

    def register_student(self, name, ic, email, phoneNumber, address, grade, subjects):
        student = Student(name, ic, email, phoneNumber, address, grade, subjects)
        self.students[name] = student
    
    def update_student_subject(self, name, subjects):
        updated = False
        for student in self.students:
            if name == student:
                self.students[name].subject = subjects
                updated = True
                return "Student subject updated"
        
        if updated == False:
            return "Student name not found. Please enter a valid student"

    def student_login(self, name):
        if self.students != {}:
            for students in self.students:
                if name == students:
                    self.logged_in_as = 'student'
                    self.logged_in_as_student = name
                    return f"Successfully logged in as student {name}."
        
        if self.logged_in_as != 'student':
            return "Error, failed to login. Please try again."

    def student_menu(self):
        print("\nWelcome to Student Menu\n" + "-" * 25)
        print("Select a Student Menu: \n0. Log Out\n1. Pay tuition fees\n2. Update their information\n3. Check schedule of classes\n")
    
    def pay_tuition(self, amount):
        if self.logged_in_as == 'student':
            self.students[self.logged_in_as_student].pay_tuition_fees(amount)
            return f"Successfully paid RM{amount} to your tuition"

    def update_information(self, element, information):
        if self.logged_in_as == 'student':
            self.students[self.logged_in_as_student].update_information(element, information)
    
    def tutor_login(self, name):
        if self.tutors != {}:
            for tutor in self.tutors:
                if name == tutor:
                    self.logged_in_as = 'tutor'
                    self.logged_in_as_tutor = name
                    return f"Successfully logged in as tutor {name}."
        
        if self.logged_in_as != 'tutor':
            return "Error, failed to login. Please try again."

    def tutor_menu(self):
        print("\nWelcome to Tutor Menu\n" + "-" * 25)
        print("Select a Student Menu: \n0. Log Out\n1. Add class information\n2. Update class information\n3. View Profiles of students\n")
   
    def add_class_information(self, subject, price, schedule):
        if self.logged_in_as == 'tutor':
            self.tutors[self.logged_in_as_tutor].add_class_information(subject, price, schedule)

    def update_class_information(self, element, information):
        if self.logged_in_as == 'tutor':
            self.tutors[self.logged_in_as_tutor].update_class_information(element, information)

    def view_student_profile(self):
        if self.logged_in_as == 'tutor':
            self.tutors[self.logged_in_as_tutor].view_profile()
