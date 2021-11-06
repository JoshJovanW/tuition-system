from classroom import Classroom
class Tutor:
    def __init__(self, name, age, subject, phoneNumber):
        self.name = name
        self.age = age
        self.subject = subject
        self.phoneNumber = phoneNumber
        self.classroom = ''

    def add_class_information(self, subject, charges, schedule):
        try:
            classroom = Classroom(subject, charges, schedule)
            self.classroom = classroom
            return "You have succesfully added the class information"
        
        except:
            return "An Error has occured. Please Try again."

    def update_class_information(self, element, information):
        try:
            if self.classroom != '':
                self.classroom.update_information(element, information)
            return f"The element {element} has been updated."

        except:
            return "Error, Class information has not been added. Please add the class information first."

    def view_profile(self):
        try:
            if self.classroom != '':
                self.classroom.see_students()
        except:
            return "Error, There are no students enrolled in this class."
