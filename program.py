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

    def staff_login(self, username, password):
        staff = Staff()
        if username == staff.username and password == staff.password:
            self.logged_in_as = 'staff'
            return "Successfully logged in as staff"
        
        else:
            return "Incorrect username or password. Try again"
        
    def register_tutor(self, name, age, subject, phoneNumber):
        tutor = Tutor(name, age, subject, phoneNumber)
        self.tutors[name] = tutor
        
        for tutor in self.tutors:
            print(tutor + "   :   " + self.tutors[tutor].subject)
        return f"\n\nSuccessfully registered tutor {name}"

    def register_student(self, name, ic, email, phoneNumber, address, grade, subjects):
        student = Student(name, ic, email, phoneNumber, address, grade, subjects)
        self.students[name] = student
        for student in self.students:
            print(student + "   :   " + self.students[student].email)
        return f"Succesfully registered student {name}"
    
    def update_student_subject(self, name):
        updated = False
        name_found = False
        for student in self.students:
            if name == student:
                print(f"Student {name}'s subjects are {self.students[name].subjects}")
                name_found = True
                
        if name_found == True:
            new_subject = input("What do you want to change?(max 3 format: math,science,economics)                 : ")
            new_subjects = new_subject.split(",")
            self.students[name].subjects = new_subjects
            updated = True
            return "Student subject updated"
        if updated == False:    
            return "Student not found. Please enter a valid name."
        
        
    def staff_menu(self):
        print("\nWelcome to Staff Menu\n" + "-" * 25)
        option = input("Select a Staff Menu: \n0. Log Out\n1. Register a tutor \n2. Register a student\n3. Update a student subject\n4. Search Payment made by Student\n")
        
        if option == "0":
            self.logged_in_as = ''

        elif option == "1":
            name = input("Tutor Name    : ")
            age = int(input("Tutor Age     : "))
            subject = input("Subject       : ")
            phoneNumber = input("Phone Number  : ")

            print(self.register_tutor(name, age, subject, phoneNumber))
            return "Successfully registered Tutor"

        elif option == "2":
            name = input("Student Name                    : ")
            ic = input("IC/Passport                     : ")
            email = input("Student Email                   : ")
            phoneNumber = input("Contact Number                  : ")
            address = input("Student Address                 : ")
            level = input("Level                           : ")
            subject = input("Subjects(max 3 format: math,science,economics)                 : ")

            subjects = subject.split(",")
            print(self.register_student(name,ic,email,phoneNumber,address,level,subjects))
            return "Succesfully registered Student"
        
        elif option == "3": 
            name = input("Student Name                    : ")
            print(self.update_student_subject(name))
            return "Successfully updated student subject"

        elif option == "4":
            name = input("Student Name                    : ")
            if self.students != {}:
                for students in self.students:
                    if name == students:
                        print(f"Here is the receipt for student {name}'s payments: \n")
                        for payment in self.students[name].payment:
                            print("-" + payment)
            

    def student_login(self, name):
        if self.students != {}:
            for students in self.students:
                if name == students:
                    self.logged_in_as = 'student'
                    self.logged_in_as_student = name
                    return f"Successfully logged in as student {name}."
        
        if self.logged_in_as != 'student':
            return "Error, failed to login. Please try again."

    def pay_tuition(self, amount):
        if self.logged_in_as == 'student':
            self.students[self.logged_in_as_student].pay_tuition_fees(amount)
            return f"Successfully paid RM{amount} to your tuition"

    def update_information(self, element, information):
        if self.logged_in_as == 'student':
            self.students[self.logged_in_as_student].update_information(element, information)
            print(f"name     : {self.students[self.logged_in_as_student].name}")
            print(f"ic       : {self.students[self.logged_in_as_student].ic}")
            print(f"email    : {self.students[self.logged_in_as_student].email}")
            print(f"contact  : {self.students[self.logged_in_as_student].phoneNumber}")
            print(f"address  : {self.students[self.logged_in_as_student].address}")
            print(f"grade    : {self.students[self.logged_in_as_student].grade}")
            print(f"subjects : {self.students[self.logged_in_as_student].subjects}\n")
            return "Succesfully updated the information"

    def check_class_schedule(self, name):
        if self.students != {}:
            for students in self.students:
                if name == students:
                    print(f"Class schedule for student {name}: \n")
                    for classes in self.students[name].classes:
                        print(f"{classes} :    {classes.schedule}")

    def student_menu(self):
        print("\nWelcome to Student Menu\n" + "-" * 25)
        option = input("Select a Student Menu: \n0. Log Out\n1. Pay tuition fees\n2. Update their information\n3. Check schedule of classes\n")
        
        if option == '0':
            self.logged_in_as =''

        if option == '1':
            amount = int(input("How much do you want to pay?(RM)    "))
            print(self.pay_tuition(amount))

        elif option == '2':
            print(f"name     : {self.students[self.logged_in_as_student].name}")
            print(f"ic       : {self.students[self.logged_in_as_student].ic}")
            print(f"email    : {self.students[self.logged_in_as_student].email}")
            print(f"contact  : {self.students[self.logged_in_as_student].phoneNumber}")
            print(f"address  : {self.students[self.logged_in_as_student].address}")
            print(f"grade    : {self.students[self.logged_in_as_student].grade}")
            print(f"subjects : {self.students[self.logged_in_as_student].subjects}\n")
    
            element = input("What element do you want to update? (email, phoneNumber, address) \n")
            information = input("What do you want to change it to? \n")
            print(self.update_information(element, information))
            
        elif option == '3':
            pass

    
    def tutor_login(self, name):
        if self.tutors != {}:
            for tutor in self.tutors:
                if name == tutor:
                    self.logged_in_as = 'tutor'
                    self.logged_in_as_tutor = name
                    return f"Successfully logged in as tutor {name}."
        
        if self.logged_in_as != 'tutor':
            return "Error, failed to login. Please try again."

    def add_class_information(self, subject, price, schedule):
        if self.logged_in_as == 'tutor':
            self.tutors[self.logged_in_as_tutor].add_class_information(subject, price, schedule)
            return "Class information Added"

    def update_class_information(self, element, information):
        if self.logged_in_as == 'tutor':
            self.tutors[self.logged_in_as_tutor].update_class_information(element, information)
            return "Updated class information"

    def view_student_profile(self):
        if self.logged_in_as == 'tutor':
            self.tutors[self.logged_in_as_tutor].view_profile()


    def tutor_menu(self):
        print("\nWelcome to Tutor Menu\n" + "-" * 25)
        option = input("Select a Student Menu: \n0. Log Out\n1. Add class information\n2. Update class information\n3. View Profiles of students\n")
         
        if option == "0":
            self.logged_in_as = ''
            self.logged_in_as_tutor = ''
        if option == "1":
            subject = input("subject name :      ")
            price = int(input("price :         "))
            schedule = input("schedule :       ")
            self.add_class_information(subject, price, schedule)
            
        elif option == "2":
            print(f"subject   : {self.tutors[self.logged_in_as_tutor].classroom.subject}")
            print(f"price     : {self.tutors[self.logged_in_as_tutor].classroom.price}")
            print(f"schedule  : {self.tutors[self.logged_in_as_tutor].classroom.schedule}")

            element = input("What element do you want to update? (email, phoneNumber, address) \n")
            information = input("What do you want to change it to? \n")
            self.update_class_information(element, information)

        elif option == "3":
            print("students : \n")
            self.tutors[self.logged_in_as_tutor].view_profile()
